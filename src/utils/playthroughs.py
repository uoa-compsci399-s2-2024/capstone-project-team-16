import os
import shutil
import json
from world import World
from utils.mappers.character_mapper import create_json_from_characters
from utils.mappers.choice_mapper import create_json_from_choices
from utils.mappers.item_mapper import create_json_from_item
from utils.mappers.location_mapper import create_json_from_locations
from utils.mappers.trope_mapper import create_json_from_tropes
from utils.prompt import get_session_messages


temp_file_path = str(os.getcwd()) + '/src/story/temp_story_store.txt'


def create_temp_story_file():
    if not os.path.exists(temp_file_path):
        with open(temp_file_path, 'x') as file:
            file.close()


def write_scene_and_choice(scene_str: str, choice_str: str) -> None:
    with open(temp_file_path, 'a') as file:
        file.write(scene_str)
        file.write("\n\n")
        file.write("> " + choice_str[0])
        file.write("\n\n")
        file.close()


def save_playthrough_as_file(world: World, choices: tuple[str]) -> None:
    """
    Save the playthrough as a file

    Parameters:
        world (World): the world object
        choices (tuple): the choices available to the player (won't be loaded, but useful for later maybe)
    """
    #get playthrough file path
    playthrough_name = str(input("Enter the name of your playthrough: "))
    playthrough_file_path = str(os.getcwd()) + f'/src/playthroughs/{playthrough_name}.txt'
    while os.path.exists(playthrough_file_path):
        new_playthrough = str(input("That filename already exists. Would you like to overwrite it? y/n"))
        if new_playthrough.lower() == 'y':
            break
        else:
            playthrough_name = str(input("Enter a new name for your playthrough: "))
            playthrough_file_path = str(os.getcwd()) + f'/src/playthroughs/{playthrough_name}.txt'
    playthrough_file_path = str(os.getcwd()) + f'/src/playthroughs/{playthrough_name}.txt'

    #break down the world object into its components and write them to the file
    with open(playthrough_file_path, 'w') as file:
        file.write(create_json_from_characters(world.characters))
        file.write('\n')
        file.write(create_json_from_item(world.items))
        file.write('\n')
        file.write(create_json_from_choices(choices))
        file.write('\n')
        file.write(create_json_from_locations(world.locations))
        file.write('\n')
        file.write(create_json_from_tropes(world.tropes))
        file.write('\n')
        file.write(json.dumps({"themes": world.theme}))
        file.write('\n')
        file.write(json.dumps({"session_messages": get_session_messages()}))
        file.write('\n')
        file.write(json.dumps({"key_events": world.key_events}))
        file.write('\n')
        file.write(json.dumps({"choices": world.choices}))


def wipe_temp_file() -> None:
    with open(temp_file_path, 'w') as file:
        file.close()


def show_background_data(curr_world: World):
    print("----------")
    print("Locations:")
    print(curr_world.locations)
    print("Items:")
    print(curr_world.items)
    print("Characters:")
    print(curr_world.characters)
    print("Tropes")
    print(curr_world.tropes)
    print("Themes:")
    print(curr_world.theme)
    print("----------")
