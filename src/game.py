"""Game Loop"""

# This is just for readability's sake
import textwrap
from openai import OpenAI
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from actions import process_user_choice, AVAILABLE_ACTIONS
from character import Character
from location import Location
from world import World
from utils.templates import flow_on_choices_template, initial_scene_template, flow_scene_template, scene_system_message, choices_system_message
from utils.prompt import chat_with_gpt, SESSION_MESSAGES
from utils.mappers import scene_mapper, choice_mapper
from utils.playthroughs import create_temp_story_file, write_scene_and_choice, save_playthrough_as_file, wipe_temp_file
from utils.structures import SceneStructure, ChoicesStructure
from utils.playthroughs import show_background_data


def choice_selection(choices: list[tuple], world: World) -> str:
    """Function to get user input for the choice"""

    updated_choices = [choices[i][0] for i in range(len(choices))]
    selection = None

    for i, choice in enumerate(updated_choices, start=1):
        print(f"{i}. {choice}\n")

    while not selection:
        user_input = input("> ")
        if user_input == "INFO":
            show_background_data(world)
            continue
        if user_input.lower().strip() == "save":
            #save this playthrough
            save_playthrough_as_file(world, choices)
            print("Playthrough saved")
            print("Make a selection")
            continue
        if not user_input.isdigit():
            print("Please enter a number")
            continue
        user_input = int(user_input)

        if user_input <= len(choices) and user_input > 0:
            selection = choices[user_input - 1]
        else:
            print("Invalid number")


    return selection


def display_initial_scene(client: OpenAI, location: Location, world: World) -> None:

    """Function to display the scene the player is in"""
    scene = chat_with_gpt(
        client=client,
        system_message=scene_system_message(),
        user_message=initial_scene_template(location.name, location.description,
                                    [world.items[item_id] for item_id in location.items],
                                    [world.characters[character_id] for character_id in location.characters if (world.characters[character_id]).playable is not True]),
        context=True,
        tokens=500,
        structure= SceneStructure
    )

    mapped_scene = scene_mapper.create_scene_from_json(scene)
    mapped_scene = mapped_scene.split(". ")
    print()
    for para in mapped_scene:
        print(f"{textwrap.fill(para, 100)}.\n")
    print()

def display_scene(client: OpenAI, location: Location, world: World, most_recent_choice: str) -> None:
    """Function to display the scene the player is in"""
    scene = chat_with_gpt(
        client=client,
        system_message=scene_system_message(),
        user_message=flow_scene_template(location.name, location.description,
                                    [world.items[item_id] for item_id in location.items],
                                    [world.characters[character_id] for character_id in location.characters if (world.characters[character_id]).playable is not True],
                                    most_recent_choice,
                                    world.key_events),
        context=True,
        tokens=500,
        structure= SceneStructure
    )

    mapped_scene = scene_mapper.create_scene_from_json(scene)
    mapped_scene = mapped_scene.split(". ")
    print()
    for para in mapped_scene:
        print(f"{textwrap.fill(para, 100)}.\n")
    print()
  
def visualise_locations(locations: list[Location], style="graphic") -> None:
    """Function to visualise the locations in the game
    Args:
        locations (list[Location]): list of Location objects
        style (str): style of visualisation, either "graphic" or "text"
    """
    if style == "graphic":
        # Create a graph from the locations
        edge_list = pd.concat(
            [pd.DataFrame([[location.name, neighbor.name]], columns=["Loc1", "Loc2"]) for location in locations for neighbor in location.neighbors], ignore_index=True)
        graph = nx.from_pandas_edgelist(edge_list, "Loc1", "Loc2")
        # get the old positions of the nodes
        old_pos = {location.name: (location.coords[0], location.coords[1]) for location in locations if location.coords is not None}
        pos = None
        if old_pos == {}:
            pos = nx.spring_layout(graph)
        else:
            # get a new layout that adds the old positions
            pos = nx.spring_layout(graph, pos=old_pos, fixed=old_pos.keys())
        # update the positions of the locations
        for location in locations:
            if location.coords is None:
                location.coords = pos[location.name]
        nx.draw(graph, pos, with_labels=True)
        plt.show()
    elif style == "text":
        print('not implemented yet')

def game_loop(player: Character, world: World, client: OpenAI) -> None:
    """The main game loop, defines what happens after every user choice"""
        # create the temp file to store the story
    create_temp_story_file()
    wipe_temp_file()
    game_over = False

    player_choice = None

    while not game_over:

        current_location = world.locations[player.current_location]
        # Displays the Scene for the user to view
        if player_choice is None:
            display_initial_scene(client, current_location, world)
        else:
            display_scene(client, current_location, world, player_choice[0])


        choices = chat_with_gpt(
            client=client,
            system_message=choices_system_message(),
            user_message=flow_on_choices_template(
                4, world.tropes, world.theme, world.key_events, [f"{neighbor.name}({neighbor.id_})" if neighbor is not None else None for neighbor
                in current_location.neighbors], [world.characters[cid] for cid in current_location.characters],
                [world.items[iid] for iid in current_location.items], AVAILABLE_ACTIONS, [world.items[iid] for iid in player.inventory.keys()]),
            context=True,
            tokens=500,
            temp=0.2,
            structure=ChoicesStructure
        )
        mapped_choices = choice_mapper.create_choices_from_json(choices)

        #BIG DEBUG INFO BLOCk
        for choice in mapped_choices:
            # THE way a choice is laid out is a tuple in the form of (description, dict, action_performed)
            print(f"DEBUG CHOICE INFO: {choice}")
        #------ END DEBUG

        # Returns the tuple choice of (desc, id)
        player_choice = choice_selection(mapped_choices, world)
        SESSION_MESSAGES.append({"role": "user", "content": f"I choose to: {player_choice[0]}"})

        process_user_choice(player_choice[1], [client, world, player, current_location], player_choice[2])
