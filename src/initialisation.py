"""Module for initialising the game"""

from utils import templates, prompt, mappers
from world import World

def initialise_game(client):
    """Initialises the tropes, themes,
    characters, locations and items
    for the game."""

    # Choose the tropes
    tropes = ["rags to riches", "chosen one", "orphan hero"]


    # Choose the theme
    themes = ["fantasy"]

    # Construct prompt and generate the characters using the tropes and theme

    characters = prompt.chat_with_gpt(client,
        "",
        templates.character_template(3, "main", tropes, themes),
        None,
        tokens=500
    )


    # Construct prompt and generate the locations using the tropes and theme

    locations = prompt.chat_with_gpt(
        client,
        "",
        templates.location_template(3, tropes, themes),
        None,
        tokens=500
    )


    # Construct prompt and generate items using the tropes and theme

    items = prompt.chat_with_gpt(
        client,
        "",
        templates.item_template(3, tropes, themes),
        None,
        tokens=500
    )


    current_world = World()
    print(characters)
    print(locations)
    print(items)
    # mappers go here
    mapped_characters = mappers.create_character_from_json(characters)
    mapped_locations = mappers.create_location_from_json(locations)
    mapped_items = mappers.create_item_from_json(items)

    for character in mapped_characters:
        current_world.add_character(character)

    for location in mapped_locations:
        current_world.add_location(location)

    for item in mapped_items:
        current_world.add_item(item)

    print(current_world.characters)
    print(current_world.locations)
    print(current_world.items)
