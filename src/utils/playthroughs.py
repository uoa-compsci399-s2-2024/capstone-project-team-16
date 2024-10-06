import os
import shutil

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


def save_playthrough_as_file() -> None:
    playthrough_name = str(input("Enter the name of your playthrough: "))
    playthrough_file_path = str(os.getcwd()) + f'/src/playthroughs/{playthrough_name}.txt'

    while os.path.exists(playthrough_file_path):
        playthrough_name = str(input("That filename already exists. Please enter the name of your playthrough: "))
        playthrough_file_path = str(os.getcwd()) + f'/src/playthroughs/{playthrough_name}.txt'

    with open(playthrough_file_path, 'x') as file:
        file.close()
    
    shutil.copy(temp_file_path, playthrough_file_path)


def wipe_temp_file() -> None:
    with open(temp_file_path, 'w') as file:
        file.close()