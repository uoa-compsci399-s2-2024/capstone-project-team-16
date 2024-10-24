import subprocess
import sys

'''Run this from cmd, will build an executable file. Note that filepaths 
    need to be changed for all data files. Will also need pyinstaller installed'''


def build_executable():
    script_name = 'src/main.py'

    command = [
        sys.executable,
        "-m",
        "PyInstaller",
        "--onefile",
        '--add-data=src/story/antagonist_tropes.csv;.',
        '--add-data=src/story/plot_tropes.csv;.',
        '--add-data=src/story/protagonist_tropes.csv;.',
        '--add-data=src/story/temp_story_store.txt;.',
        '--add-data=src/story/themes.txt;.',
        script_name
    ]

    try:
        subprocess.run(command, check=True)
        print("Build completed")
    except subprocess.CalledProcessError as e:
        print("Error", e)


if __name__ == "__main__":
    build_executable()
