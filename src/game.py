"""Game Loop"""

# This is just for readability's sake
import textwrap
from openai import OpenAI

from actions import process_user_choice
from character import Character
from location import Location
from world import World
from utils.templates import flow_on_choices_template, scene_template, scene_system_message, choices_system_message
from utils.prompt import chat_with_gpt
from utils.mappers import scene_mapper, choice_mapper
from utils.playthroughs import create_temp_story_file, write_scene_and_choice, save_playthrough_as_file, wipe_temp_file
from utils.structures import SceneStructure, ChoicesStructure

def choice_selection(choices: list[tuple]) -> str:
    """Function to get user input for the choice"""

    updated_choices = [choices[i][0] for i in range(len(choices))]
    selection = None

    for i, choice in enumerate(updated_choices, start=1):
        print(f"{i}. {choice}\n")

    while not selection:
        user_input = input("> ")
        if not user_input.isdigit():
            print("Please enter a number")
            continue
        else:
            user_input = int(user_input)

        if user_input <= len(choices) and user_input > 0:
            selection = choices[user_input - 1]
        else:
            print("Invalid number")


    return selection



def display_scene(client: OpenAI, location: Location, world: World) -> None:
    """Function to display the scene the player is in"""
    scene = chat_with_gpt(
        client=client,
        system_message=scene_system_message(),
        user_message=scene_template(location.name, location.description,
                                    [world.items[item_id] for item_id in location.items],
                                    [world.characters[character_id] for character_id in location.characters if (world.characters[character_id]).playable is not True]),
        context=False,
        tokens=500,
        structure= SceneStructure
    )

    mapped_scene = scene_mapper.create_scene_from_json(scene)
    mapped_scene = mapped_scene.split(". ")
    print()
    for para in mapped_scene:
        print(f"{textwrap.fill(para, 100)}.\n")
    print()
  

def game_loop(player: Character, world: World, client: OpenAI) -> None:
    """The main game loop, defines what happens after every user choice"""
        # create the temp file to store the story
    create_temp_story_file()
    wipe_temp_file()
    game_over = False

    while not game_over:

        current_location = world.locations[player.current_location]
        # Displays the Scene for the user to view
        display_scene(client, current_location, world)

        choices = chat_with_gpt(
            client=client,
            system_message=choices_system_message(),
            user_message=flow_on_choices_template(
                4, world.tropes, world.theme, [f"{neighbor.name}({neighbor.id_})" if neighbor is not None else None for neighbor
                in current_location.neighbors], [world.characters[cid] for cid in current_location.characters],
                [world.items[iid] for iid in current_location.items], ["move location"]),
            context=False,
            tokens=500,
            temp=0.5,
            structure=ChoicesStructure
        )
        mapped_choices = choice_mapper.create_choices_from_json(choices)

        # Returns the tuple choice of (desc, id)
        player_choice = choice_selection(mapped_choices)
    

        process_user_choice(player_choice[1], [client, world, player, current_location])
        # create a fresh txt file for this playthrough, store it and wipe temp for repeated use
        save_playthrough_as_file()
