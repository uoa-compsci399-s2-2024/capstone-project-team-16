"""Module for initialising the game"""
import os

import openai

from utils import templates, prompt, structures
from utils.mappers import character_mapper, location_mapper, item_mapper, trope_mapper
from world import World
# from game import get_random_tropes, read_csv_file, create_tropes
from utils.narrative_elements import select_narrative_elements
from game import game_loop
import json
from character import Character

# number of characters and items to populate each location with
NUM_CHARACTERS = 1
NUM_ITEMS = 1


def print_art() -> None:
    print("      _,.")
    print("    ,` -.)")
    print("   ( _/-\\\\-._")
    print("  /,|`--._,-^|            ,")
    print("  \\_| |`-._/||          ,'|")
    print("    |  `-, / |         /  /")
    print("    |     || |        /  /")
    print("     `r-._||/   __   /  /")
    print(" __,-<_     )`-/  `./  /")
    print("'  \\   `---'   \\   /  /")
    print("    |           |./  /")
    print("    /           //  /")
    print("\\_/' \\         |/  /")
    print(" |    |   _,^-'/  /")
    print(" |    , ``  (\\/  /_")
    print("  \\,.->._    \\X-=/^")
    print("  (  /   `-._//^`")
    print("   `Y-.____(__}")
    print("    |     {__)")
    print("          ()")
    print("")


def print_title() -> None:
    print("   _____       .___                    __                     /\\         _________        .__  .__   ")
    print("  /  _  \\    __| _/__  __ ____   _____/  |_ __ _________   ___)/  ______ \\_   ___ \\_____  |  | |  |  ")
    print(" /  /_\\  \\  / __ |\\  \\/ // __ \\ /    \\   __\\  |  \\_  __ \\_/ __ \\ /  ___/ /    \\  \\/\\__  \\ |  | |  |  ")
    print("/    |    \\/ /_/ | \\   /\\  ___/|   |  \\  | |  |  /|  | \\/\\  ___/ \\___ \\  \\     \\____/ __ \\|  |_|  |__")
    print("\\____|__  /\\____ |  \\_/  \\___  >___|  /__| |____/ |__|    \\___  >____  >  \\______  (____  /____/____/")
    print("        \\/      \\/           \\/     \\/                        \\/     \\/          \\/     \\/           ")

def print_description() -> None:
    print("In this game, you will embark on a thrilling quest")
    print("filled with danger, mystery, and magic. Your choices")
    print("will determine the outcome of your adventure.")
    print("NOTE: If you should wish to view the data of this playthrough then enter INFO.")
    print()


def start_game() -> bool:
    user_input = input("> Press enter to start game... ")
    return True

def setup_save_folder() -> None:
    '''Checks if save folder exists, if not creates it'''
    saved_games_folder = os.path.join(os.environ["USERPROFILE"], "Saved Games")
    game_folder = os.path.join(saved_games_folder, "Adventure's Call")

    if not os.path.exists(game_folder):
        os.makedirs(game_folder)
        print("DEBUG: SAVE FOLDER CREATED")
    else:
        print("DEBUG: SAVE FOLDER ALREADY EXISTS")


def initialise_game(client):
    """Initialises the tropes, themes,
    characters, locations and items
    for the game."""

    setup_save_folder()
    plot_tropes_path = str(os.getcwd()) + '/src/story/plot_tropes.csv'
    protagonist_tropes_path = str(os.getcwd()) + '/src/story/protagonist_tropes.csv'
    antagonist_tropes_path = str(os.getcwd()) + '/src/story/antagonist_tropes.csv'
    themes_path = str(os.getcwd()) + '/src/story/themes.txt'

    current_world = World()
    load_world = input("Would you like to load a previous game? (y/n): ").lower().strip() == 'y'
    if load_world:
        load_game(client, current_world)
    else:
        create_new_game(themes_path, plot_tropes_path, protagonist_tropes_path, antagonist_tropes_path, 3,
                        1, 1, current_world, client)


def load_game(client, current_world):
    """
    Load a game from a previous playthrough

    Parameters:
        client (OpenAI): the OpenAI client
        current_world (World): the current world object
    """
    # get playthrough file path

    saved_games_folder = os.path.join(os.environ["USERPROFILE"], "Saved Games")
    game_folder = os.path.join(saved_games_folder, "Adventure's Call")

    saved_games = [f for f in os.listdir(game_folder) if os.path.isfile(os.path.join(game_folder, f))]

    if not saved_games:
        print("No save files exist.")
        initialise_game(client)
        return
    
    for saved_game in saved_games:
        print(saved_game.removesuffix(".txt"))

    playthrough_name = input("Enter the name of the playthrough you would like to load: ")
    playthrough_file_path = os.path.join(game_folder, f"{playthrough_name}.txt")
    while not os.path.exists(playthrough_file_path):
        playthrough_name = input(
            "That playthrough does not exist. Please enter a valid playthrough name, or enter nothing to exit: ")
        if playthrough_name == "":
            return
        playthrough_file_path = os.path.join(game_folder, f"{playthrough_name}.txt")
    # read the playthrough file
    lines = None
    with open(playthrough_file_path, 'r') as file:
        lines = file.readlines()
    if lines is None:
        raise ValueError("No content found in playthrough file")
    objects = [json.loads(line) for line in lines]
    # process objects
    json_locations = None
    json_characters = None
    json_items = None
    json_choices = None
    json_tropes = None
    json_themes = None
    # for each object, add it to the world
    for obj in objects:
        if "characters" in obj:
            json_characters = obj["characters"]
            for character in json_characters:
                current_world.add_character(character_mapper.create_character_from_json_save(character))
        if "locations" in obj:
            json_locations = obj["locations"]
            for location in json_locations:
                current_world.add_location(location_mapper.create_location_from_json_save(location))
        if "items" in obj:
            json_items = obj["items"]
            for item in json_items:
                current_world.add_item(item_mapper.create_item_from_json_save(item))
        if "tropes" in obj:
            json_tropes = obj["tropes"]
            for trope in json_tropes:
                #current_world.add_trope(trope)
                current_world.add_trope(trope_mapper.create_trope_from_json_save(trope))
        if "themes" in obj:
            json_themes = obj["themes"]
            current_world.add_theme(json_themes)
        if "choices" in obj:
            json_choices = obj["choices"]
            current_world.set_choices(json_choices)

    # join locations together
    for location in current_world.locations.values():
        for other_location in json_locations:
            if other_location["id"] == location.id_:
                for neighbour in other_location["neighbours"]:
                    location.add_neighbor(current_world.locations[neighbour])

    # find the player character
    player = [character for character in current_world.characters.values() if character.playable][0]
    # proceed to the game loop
    game_loop(player, current_world, client)


def create_new_game(themes_path, plot_tropes_path, protagonist_tropes_path, antagonist_tropes_path, num_plot_tropes,
                    num_prot_tropes, num_ant_tropes, current_world, client):
    # Choose the theme and tropes
    theme, tropes = select_narrative_elements(themes_path, plot_tropes_path, protagonist_tropes_path,
                                              antagonist_tropes_path, num_plot_tropes, num_prot_tropes, num_ant_tropes)
    for trope in tropes:
        current_world.add_trope(trope)

    current_world.add_theme(theme)

    # Construct prompt and generate the locations using the tropes and theme
    locations = None
    tokens = 700
    while not locations:
        try:
            locations = prompt.chat_with_gpt(
                client,
                templates.location_system_message(),
                templates.location_template(5, tropes, theme, NUM_ITEMS, NUM_CHARACTERS),
                False,
                tokens=tokens,
                temp=0.5,
                structure=structures.SectionStructure
            )
        except openai.LengthFinishReasonError:
            print("Token Count Error, Not provided enough tokens... increasing token count and retrying")
            tokens += 100

    # add the initial JSON objects to their world.py lists
    current_world.add_json_location(locations)

    mapped_locations = location_mapper.create_location_from_json(json_str=locations, world=current_world)

    for location in mapped_locations:
        current_world.add_location(location)

    # Easy Way to create a Playable Character FOR DEMO
    player = Character(input("Input your character's name:\n> "), [], playable=True)

    current_world.add_character(player)
    # Adds Player to the ID 0 location and vice versa
    player.current_location = (current_world.locations[0]).id_
    (current_world.locations[0]).add_character(player.id_)

    game_loop(player, current_world, client)
