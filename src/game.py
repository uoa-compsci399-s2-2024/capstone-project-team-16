"""
Game Loop
"""

# This is just for readability's sake
import textwrap

import openai
from openai import OpenAI
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from actions import process_user_choice, AVAILABLE_ACTIONS
from character import Character
from location import Location
from world import World
from utils.templates import (flow_on_choices_template, initial_scene_template, flow_scene_template,
                             scene_system_message, choices_system_message, flow_scene_template_new_beat)
from utils.prompt import chat_with_gpt, SESSION_MESSAGES
from utils.mappers import scene_mapper, choice_mapper
from utils.playthroughs import save_playthrough_as_file
from utils.structures import SceneStructure, ChoicesStructure
from utils.playthroughs import show_background_data
from utils.story_beats import BEATS, change_beat


def choice_selection(choices: list[tuple], world: World) -> tuple:
    """
    Function to get user input for the choice

    :param list[tuple] choices: A lst of all the choices available
    :param World world: World object
    :return: A tuple containing the choice the user made
    :rtype: tuple
    """

    updated_choices = [choices[i][0] for i in range(len(choices))]
    selection = None

    for i, choice in enumerate(updated_choices, start=1):
        print(f"{i}. {choice}\n")

    while not selection:
        user_input = input("> ")
        if user_input.strip().lower() == "info":
            show_background_data(world)
            continue
        if user_input.lower().strip() == "save":
            # save this playthrough
            save_playthrough_as_file(world, choices)
            print("Playthrough saved")
            print("Make a selection")
            continue
        if user_input.lower().strip() == "map":
            # show the location map
            visualise_locations([world.locations[location_id] for location_id in world.locations], style="graphic")
            print("Make a selection")
            continue
        if not user_input.isdigit():
            print("Please enter a number")
            continue
        user_input = int(user_input)

        if len(choices) >= user_input > 0:
            selection = choices[user_input - 1]
        else:
            print("Invalid number")

    return selection


def display_initial_scene(client: OpenAI, location: Location, world: World) -> None:
    """
    Function to display the scene the player is in

    :param OpenAI client: OpenAI client
    :param Location location: Location of the scene
    :param World world: The current World object
    :rtype: None
    """
    scene = None
    tokens = 500
    while not scene:
        try:
            scene = chat_with_gpt(
                client=client,
                system_message=scene_system_message(),
                user_message=initial_scene_template(location.name,
                                                    location.description,
                                                    [world.items[item_id] for item_id in location.items],
                                                    [world.characters[character_id] for character_id in
                                                     location.characters if
                                                     (world.characters[character_id]).playable is not True],
                                                    list(BEATS.keys())[world.curr_story_beat],
                                                    list(BEATS.values())[world.curr_story_beat]),
                context=True,
                tokens=tokens,
                structure=SceneStructure)
        except openai.LengthFinishReasonError:
            print("Token Count Error, Not provided enough tokens... increasing token count and retrying")
            tokens += 500
        except openai.APIConnectionError:
            print("API CONNECTION ERROR ... Retrying")

    mapped_scene = scene_mapper.create_scene_from_json(scene)
    mapped_scene = mapped_scene.split(". ")
    print()
    for para in mapped_scene:
        print(f"{textwrap.fill(para, 100)}.\n")
    print()


def display_scene(client: OpenAI, location: Location, world: World, most_recent_choice: str) -> None:
    """
    Function to display the scene the player is in

    :param OpenAI client: OpenAI client
    :param Location location: Location of the scene
    :param World world: The current World object
    :param str most_recent_choice: The most recent choice the user has made
    :rtype: None
    """
    scene = None
    tokens = 500
    while not scene:
        try:
            scene = chat_with_gpt(
                client=client,
                system_message=scene_system_message(),
                user_message=flow_scene_template(location.name,
                                                 location.description,
                                                 [world.items[item_id] for item_id in location.items],
                                                 [world.characters[character_id] for character_id in location.characters
                                                  if
                                                  (world.characters[character_id]).playable is not True],
                                                 most_recent_choice,
                                                 world.key_events,
                                                 list(BEATS.keys())[world.curr_story_beat],
                                                 list(BEATS.values())[world.curr_story_beat]),
                context=True,
                tokens=tokens,
                structure=SceneStructure
            )
        except openai.LengthFinishReasonError:
            print("Token Count Error, Not provided enough tokens... increasing token count and retrying")
            tokens += 100
        except openai.APIConnectionError:
            print("API CONNECTION ERROR ... Retrying")

    mapped_scene = scene_mapper.create_scene_from_json(scene)
    mapped_scene = mapped_scene.split(". ")
    print()
    for para in mapped_scene:
        print(f"{textwrap.fill(para, 100)}.\n")
    print()


def display_scene_new_beat(client: OpenAI, location: Location, world: World, most_recent_choice: str) -> None:
    """
    Function to display the scene the player is in

    :param OpenAI client: OpenAI client
    :param Location location: Location of the scene
    :param World world: The current World object
    :param str most_recent_choice: The most recent choice the user has made
    :rtype: None
    """
    scene = None
    tokens = 500
    while not scene:
        try:
            scene = chat_with_gpt(
                client=client,
                system_message=scene_system_message(),
                user_message=flow_scene_template_new_beat(location.name,
                                                          location.description,
                                                          [world.items[item_id] for item_id in location.items],
                                                          [world.characters[character_id] for character_id in
                                                           location.characters if
                                                           (world.characters[character_id]).playable is not True],
                                                          most_recent_choice,
                                                          world.key_events,
                                                          list(BEATS.keys())[world.curr_story_beat],
                                                          list(BEATS.values())[world.curr_story_beat]),
                context=True,
                tokens=tokens,
                structure=SceneStructure
            )
        except openai.LengthFinishReasonError:
            print("Token Count Error, Not provided enough tokens... increasing token count and retrying")
            tokens += 100
        except openai.APIConnectionError:
            print("API CONNECTION ERROR ... Retrying")

    mapped_scene = scene_mapper.create_scene_from_json(scene)
    mapped_scene = mapped_scene.split(". ")
    print()
    for para in mapped_scene:
        print(f"{textwrap.fill(para, 100)}.\n")
    print()


def visualise_locations(locations: list[Location], style="graphic") -> None:
    """Function to visualise the locations in the game

    :param list[Location] locations: list of Location objects
    :param str style: style of visualisation, either "graphic" or "text"
    :rtype: None
    """
    if style == "graphic":
        # Create a graph from the locations
        edge_list = pd.concat(
            [pd.DataFrame([[location.name, neighbor.name]], columns=["Loc1", "Loc2"]) for location in locations for
             neighbor in location.neighbors if neighbor is not None], ignore_index=True)
        graph = nx.from_pandas_edgelist(edge_list, "Loc1", "Loc2")
        # get the old positions of the nodes
        old_pos = {location.name: (location.coords[0], location.coords[1]) for location in locations if
                   location.coords is not None}
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
    """
    The main game loop, defines what happens after every user choice

    :param Character player: The Character of the player
    :param World world: The current World object
    :param OpenAI client: OpenAI client
    :rtype: None
    """
    game_over = False

    player_choice = None

    while not game_over:

        current_location = world.locations[player.current_location]
        # Displays the Scene for the user to view
        if player_choice is None:
            display_initial_scene(client, current_location, world)
        else:
            new_beat, last_beat = change_beat(world.curr_story_beat)
            if last_beat:
                world.curr_story_beat = new_beat
                display_scene_new_beat(client, current_location, world, player_choice[0])
                game_over = True
                continue
            elif new_beat:
                world.curr_story_beat = new_beat
                display_scene_new_beat(client, current_location, world, player_choice[0])
            else:
                display_scene(client, current_location, world, player_choice[0])

        choices = None
        tokens = 500
        while not choices:
            try:
                choices = chat_with_gpt(
                    client=client,
                    system_message=choices_system_message(),
                    user_message=flow_on_choices_template(
                        4, list(world.tropes.values()), world.theme[0], world.key_events,
                        [f"{neighbor.name}({neighbor.id_})" if neighbor is not None else None for neighbor
                         in current_location.neighbors], [world.characters[cid] for cid in current_location.characters],
                        [world.items[iid] for iid in current_location.items], AVAILABLE_ACTIONS,
                        [world.items[iid] for iid in player.inventory.keys()]),
                    context=True,
                    tokens=tokens,
                    temp=0.2,
                    structure=ChoicesStructure
                )
            except openai.LengthFinishReasonError:
                print("Token Count Error, Not provided enough tokens... increasing token count and retrying")
                tokens += 100
            except ValueError:
                pass
            except openai.APIConnectionError:
                print("API CONNECTION ERROR ... Retrying")

        mapped_choices = choice_mapper.create_choices_from_json(choices)

        # Returns the tuple choice of (desc, id)
        player_choice = choice_selection(mapped_choices, world)
        SESSION_MESSAGES.append({"role": "user", "content": f"I choose to: {player_choice[0]}"})

        process_user_choice(player_choice[1], [client, world, player, current_location], player_choice[2])
