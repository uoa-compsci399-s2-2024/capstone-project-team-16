"""
Functions for saving playthroughs and displaying background data
"""
import os
import json
from world import World
from utils.mappers.character_mapper import create_json_from_characters
from utils.mappers.choice_mapper import create_json_from_choices
from utils.mappers.item_mapper import create_json_from_item
from utils.mappers.location_mapper import create_json_from_locations
from utils.mappers.trope_mapper import create_json_from_tropes
from utils.prompt import get_session_messages


def save_playthrough_as_file(world: World, choices: list[tuple]) -> None:
    """
    Save the playthrough in a file

    :param World world: The World object
    :param list[tuple] choices: A list of all the choices a player has made
    :rtype: None
    """
    # get playthrough file path
    playthrough_name = str(input("Enter the name of your playthrough: "))
    saved_games_folder = os.path.join(os.environ["USERPROFILE"], "Saved Games")
    game_folder = os.path.join(saved_games_folder, "Adventure's Call")
    playthrough_file_path = os.path.join(game_folder, f"{playthrough_name}.txt")
    while os.path.exists(playthrough_file_path):
        new_playthrough = str(input("That filename already exists. Would you like to overwrite it? y/n"))
        if new_playthrough.lower() == 'y':
            break
        else:
            playthrough_name = str(input("Enter a new name for your playthrough: "))
            playthrough_file_path = os.path.join(game_folder, f"{playthrough_name}.txt")
    playthrough_file_path = os.path.join(game_folder, f"{playthrough_name}.txt")

    # break down the world object into its components and write them to the file
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


def show_background_data(curr_world: World) -> None:
    """
    Prints the background data of the current World object

    :param World curr_world: The current World object
    :rtype: None
    """
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
