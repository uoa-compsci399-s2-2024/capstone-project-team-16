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
    playthrough_name = input("Enter the name of the playthrough you would like to load: ")
    playthrough_file_path = str(os.getcwd()) + f'/src/playthroughs/{playthrough_name}.txt'
    while not os.path.exists(playthrough_file_path):
        playthrough_name = input("That playthrough does not exist. Please enter a valid playthrough name, or enter nothing to exit: ")
        if playthrough_name == "":
            return
        playthrough_file_path = str(os.getcwd()) + f'/src/playthroughs/{playthrough_name}.txt'
    lines = None
    with open(playthrough_file_path, 'r') as file:
        lines = file.readlines()
    if lines is None:
        raise ValueError("No content found in playthrough file")
    objects = [json.loads(line) for line in lines]
    json_locations = None
    json_characters = None
    json_items = None
    json_choices = None
    json_tropes = None
    json_themes = None
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

    #join locations together
    for location in current_world.locations.values():
        for other_location in json_locations:
            if other_location["id"] == location.id_:
                for neighbor in other_location["neighbors"]:
                    location.add_neighbor(current_world.locations[neighbor])

    player = [character for character in current_world.characters if character.playable][0]

    game_loop(player, current_world, client)


def create_new_game(plot_tropes_path, themes_path, current_world, client):
    # Choose the tropes
    tropes = get_random_tropes(create_tropes(read_csv_file(plot_tropes_path)), 3)
    for trope in tropes:
        current_world.add_trope(trope)

    # Choose the theme
    theme = get_random_theme(themes_path)
    current_world.add_theme(theme)

    # Construct prompt and generate the characters using the tropes and theme
    # Commenting this out as do we need to create characters if we are populating locations with
    # them individually
    # characters = prompt.chat_with_gpt(
    #    client,
    #    "You are a knowledgeable chatbot that creates unique characters",
    #    templates.character_template(3, "sec", tropes, theme),
    #    False,
    #    tokens=500
    #)
    print("DEBUG: CREATING LOCATIONS")
    # Construct prompt and generate the locations using the tropes and theme
    locations = prompt.chat_with_gpt(
        client,
        templates.location_system_message(),
        templates.location_template(5, tropes, theme),
        False,
        tokens=600,
        temp=1,
        structure=structures.SectionStructure
    )
    print("DEBUG: FINISHED CREATING LOCATIONS")
    # Construct prompt and generate items using the tropes and theme
    # Same with this do we need items in locations? if we have a populate within location
    # items = prompt.chat_with_gpt(
    #     client,
    #     "You are a knowledgeable chatbot that creates unique items",
    #     templates.item_template(3, tropes, theme),
    #     False,
    #     tokens=500
    # )

    # Construct prompt and generate player choices using the tropes and theme
    # Choices are created within the game loop so arent needed here
    # choices = prompt.chat_with_gpt(
    #     client,
    #     "You are a knowledgeable chatbot that gives a list of choices",
    #     templates.initial_choices_template(5, tropes, theme),
    #     True,
    #     tokens=500
    # )

    # add the initial JSON objects to their world.py lists
    current_world.add_json_location(locations)
    #current_world.add_json_character(characters)
    #current_world.add_json_item(items)

    # mappers go here
    #mapped_characters = character_mapper.create_character_from_json(characters)
    mapped_locations = location_mapper.create_location_from_json(json_str=locations, world=current_world)
    #mapped_items = item_mapper.create_item_from_json(items)
    #mapped_choices = choice_mapper.create_choices_from_json(choices)

    #for character in mapped_characters:
    #    current_world.add_character(character)

    for location in mapped_locations:
        print(location.name)
        print(location.description)
        print([None if neighbor is None else neighbor.name for neighbor in location.neighbors])
        current_world.add_location(location)

    #for item in mapped_items:
    #    current_world.add_item(item)

    #current_world.set_choices(mapped_choices)

    # Easy Way to create a Playable Character FOR DEMO
    player = Character(input("Input your character's name:\n> "), [], playable=True)

    current_world.add_character(player)
    # Adds Player to the ID 0 location and vice versa
    player.current_location = (current_world.locations[0]).id_
    (current_world.locations[0]).add_character(player.id_)

    game_loop(player, current_world, client)
