import os
import shutil

temp_file_path = str(os.getcwd()) + r"src\story\temp_story_store.txt"

def write_scene_and_choice(scene_str: str, choice_str: str) -> None:
    with open(temp_file_path, 'w') as file:
        file.write(scene_str)
        file.write("\n\n")
        file.write(choice_str)
        file.write("\n\n")


def save_playthrough_as_file() -> None:
    playthrough_name = str(input("Enter the name of your playthrough: "))
    playthrough_file_path = r"src\playthroughs" + playthrough_name + ".txt"
    
    with open(playthrough_file_path):
        pass
    
    shutil.copy(temp_file_path, playthrough_file_path)


def wipe_temp_file() -> None:
    with open(temp_file_path, 'w') as file:
        pass