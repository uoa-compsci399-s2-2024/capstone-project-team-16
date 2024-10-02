import os
import shutil
import json
from src.world import World
from src.utils.mappers.character_mapper import create_json_from_characters
from src.utils.mappers.choice_mapper import create_json_from_choices
from src.utils.mappers.item_mapper import create_json_from_item
from src.utils.mappers.location_mapper import create_json_from_locations
from src.utils.mappers.trope_mapper import create_json_from_tropes

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

    with open(playthrough_file_path, 'w') as file:
        file.write(create_json_from_characters(world.characters))
        file.write(create_json_from_item(world.items))
        file.write(create_json_from_choices(choices))
        file.write(create_json_from_locations(world.locations))
        file.write(create_json_from_tropes(world.tropes))
        file.write(json.dumps({"themes": world.theme}))


def wipe_temp_file() -> None:
    with open(temp_file_path, 'w') as file:
        file.close()