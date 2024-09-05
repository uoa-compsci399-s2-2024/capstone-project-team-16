"""Module for initialising the game"""
import os
from utils import templates, prompt, mappers
from world import World
#from game import get_random_tropes, read_csv_file, create_tropes
from utils.narrative_elements import get_random_tropes, get_random_theme, read_csv_file, create_tropes

def initialise_game(client):
    """Initialises the tropes, themes,
    characters, locations and items
    for the game."""

    plot_tropes_path = os.path.join(os.path.dirname(os.getcwd()), 'src/story/plot_tropes.csv')
    # file_path_2 = os.path.join(os.path.dirname(os.getcwd()), 'src/story/protagonist_tropes.csv')
    # file_path_3 = os.path.join(os.path.dirname(os.getcwd()), 'src/story/antagonist_tropes.csv')
    themes_path = os.path.join(os.path.dirname(os.getcwd()), 'src/story/themes/txt')

    current_world = World()

    # Choose the tropes
    tropes = get_random_tropes(create_tropes(read_csv_file(plot_tropes_path)), 3)
    for trope in tropes:
        current_world.add_trope(trope)

    # Choose the theme
    theme = get_random_theme(themes_path)
    current_world.add_theme(theme)

    # Construct prompt and generate the characters using the tropes and theme
    characters = prompt.chat_with_gpt(
        client,
        "You are a knowledgeable chatbot that creates unique characters",
        templates.character_template(3, "sec", tropes, theme),
        False,
        tokens=500
    )

    # Construct prompt and generate the locations using the tropes and theme
    locations = prompt.chat_with_gpt(
        client,
        "You are a knowledgeable chatbot that creates unique locations",
        templates.initial_location_template(6, tropes, theme),
        False,
        tokens=500
    )

    # Construct prompt and generate items using the tropes and theme
    items = prompt.chat_with_gpt(
        client,
        "You are a knowledgeable chatbot that creates unique items",
        templates.item_template(3, tropes, theme),
        False,
        tokens=500
    )

    # Construct prompt and generate player choices using the tropes and theme
    choices = prompt.chat_with_gpt(
        client,
        "You are a knowledgeable chatbot that gives a list of choices",
        templates.initial_choices_template(5, tropes, theme),
        True,
        tokens=500
    )

    # add the initial JSON objects to their world.py lists
    World.add_json_location(locations)
    World.add_json_character(characters)
    World.add_json_item(items)

    # mappers go here
    mapped_characters = mappers.create_character_from_json(characters)
    mapped_locations = mappers.create_location_from_json(json_str=locations)
    mapped_items = mappers.create_item_from_json(items)
    mapped_choices = mappers.create_choices_from_json(choices)

    for character in mapped_characters:
        current_world.add_character(character)

    for location in mapped_locations:
        current_world.add_location(location)

    for item in mapped_items:
        current_world.add_item(item)

    current_world.set_choices(mapped_choices)

    print(current_world.characters)
    print(current_world.locations)
    print(current_world.items)
    print(current_world.choices)
    print(tropes)
    print(current_world.tropes)
