"""Module for initialising the game"""
import os
from utils import templates, prompt, structures
from utils.mappers import character_mapper, location_mapper, item_mapper
from world import World
#from game import get_random_tropes, read_csv_file, create_tropes
from utils.narrative_elements import get_random_tropes, get_random_theme, read_csv_file, create_tropes
from game import game_loop
import json
from character import Character
import utils.prompt as prompt

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

    print("    .___                          .___          /\\ __         __          .___              ")
    print("  __| _/____   _____   ____     __| _/____   ___)//  |_      |__|__ __  __| _/ ____   ____  ")
    print(" / __ |/ __ \\ /     \\ /  _ \\   / __ |/  _ \\ /    \\   __\\     |  |  |  \\/ __ | / ___\\_/ __ \\ ")
    print("/ /_/ \\  ___/|  Y Y  (  <_> ) / /_/ (  <_> )   |  \\  |       |  |  |  / /_/ |/ /_/  >  ___/ ")
    print("\\____ |\\___  >__|_|  /\\____/  \\____ |\\____/|___|  /__|   /\\__|  |____/\\____ |\\___  / \\___  >")
    print("     \\/    \\/      \\/              \\/           \\/       \\______|          \\/_____/      \\/ ")
    print("")

def print_description() -> None:


    print("In this game, you will embark on a thrilling quest")
    print("filled with danger, mystery, and magic. Your choices")
    print("will determine the outcome of your adventure.")
    print("NOTE: If you should wish to view the data of this playthrough then enter INFO.")
    print()

def start_game() -> bool:

    user_input = input("> Press enter to start game... ")
    return True

def initialise_game(client):
    """Initialises the tropes, themes,
    characters, locations and items
    for the game."""

    plot_tropes_path = str(os.getcwd()) + '/src/story/plot_tropes.csv'
    # file_path_2 = os.path.join(os.path.dirname(os.getcwd()), 'src/story/protagonist_tropes.csv')
    # file_path_3 = os.path.join(os.path.dirname(os.getcwd()), 'src/story/antagonist_tropes.csv')
    themes_path = str(os.getcwd()) + '/src/story/themes.txt'


    current_world = World()
    load_world = input("Would you like to load a previous game? (y/n): ").lower().strip() == 'y'
    if load_world:
        load_game(client, current_world)
    else:
        create_new_game(plot_tropes_path, themes_path, current_world, client)

def load_game(client, current_world):
    """
    Load a game from a previous playthrough

    Parameters:
        client (OpenAI): the OpenAI client
        current_world (World): the current world object
    """
    #get playthrough file path
    playthrough_name = input("Enter the name of the playthrough you would like to load: ")
    playthrough_file_path = str(os.getcwd()) + f'/src/playthroughs/{playthrough_name}.txt'
    while not os.path.exists(playthrough_file_path):
        playthrough_name = input("That playthrough does not exist. Please enter a valid playthrough name, or enter nothing to exit: ")
        if playthrough_name == "":
            return
        playthrough_file_path = str(os.getcwd()) + f'/src/playthroughs/{playthrough_name}.txt'
    #read the playthrough file
    lines = None
    with open(playthrough_file_path, 'r') as file:
        lines = file.readlines()
    if lines is None:
        raise ValueError("No content found in playthrough file")
    objects = [json.loads(line) for line in lines]
    #process objects
    json_locations = None
    json_characters = None
    json_items = None
    json_choices = None
    json_tropes = None
    json_themes = None
    #for each object, add it to the world
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
                current_world.add_trope(trope)
        if "themes" in obj:
            json_themes = obj["themes"]
            current_world.add_theme(json_themes)
        if "choices" in obj:
            json_choices = obj["choices"]
            current_world.set_choices(json_choices)
        if "session_messages" in obj:
            prompt.SESSION_MESSAGES.extend(obj["session_messages"])

    #join locations together
    for location in current_world.locations.values():
        for other_location in json_locations:
            if other_location["id"] == location.id_:
                for neighbour in other_location["neighbours"]:
                    location.add_neighbor(current_world.locations[neighbour])

    #find the player character
    player = [character for character in current_world.characters.values() if character.playable][0]
    #proceed to the game loop
    game_loop(player, current_world, client)


def create_new_game(plot_tropes_path, themes_path, current_world, client):
    # Choose the tropes
    tropes = get_random_tropes(create_tropes(read_csv_file(plot_tropes_path)), 3)
    for trope in tropes:
        current_world.add_trope(trope)

    # Choose the theme
    theme = get_random_theme(themes_path)
    current_world.add_theme(theme)


    print("DEBUG: CREATING LOCATIONS")
    # Construct prompt and generate the locations using the tropes and theme
    locations = prompt.chat_with_gpt(
        client,
        templates.location_system_message(),
        templates.location_template(5, tropes, theme, NUM_ITEMS, NUM_CHARACTERS),
        False,
        tokens=700,
        temp=0.5,
        structure=structures.SectionStructure
    )


    # add the initial JSON objects to their world.py lists
    current_world.add_json_location(locations)



    mapped_locations = location_mapper.create_location_from_json(json_str=locations, world=current_world)



    for location in mapped_locations:
        current_world.add_location(location)

    print("DEBUG: FINISHED CREATING LOCATIONS")

    # Easy Way to create a Playable Character FOR DEMO
    player = Character(input("Input your character's name:\n> "), [], playable=True)

    current_world.add_character(player)
    # Adds Player to the ID 0 location and vice versa
    player.current_location = (current_world.locations[0]).id_
    (current_world.locations[0]).add_character(player.id_)

    game_loop(player, current_world, client)
