"""Mapper helper functions to convert JSON output
from the API into instances of our defined classes."""

import json
from location import Location
from character import Character
from item import Item


def create_location_from_json(json_str: str) -> Location:
    """
    Takes a JSON string as input, deserializes it, 
    and converts it into a new instance of the Location class.
    
    Parameters:
        json_str (str): The JSON string to be deserialized into a Location object.
    
    Returns:
        Location: A new instance of the Location class.
    """
    json_str = json_str.strip('```json').strip('```').strip()
    data = json.loads(json_str)["locations"]


    return [Location(
        name=location['name'],
        description=location['description']
        ) for location in data]


def create_character_from_json(json_str: str) -> Character:
    """
    Takes a JSON string as input, deserializes it,
    and converts it into a new instance of the Character class.
    
    Parameters:
        json_str (str): The JSON string to be deserialized into a Character object.
    
    Returns:
        Character: A new instance of the Character class.
    """
    json_str = json_str.strip('```json').strip('```').strip()
    data = json.loads(json_str)["characters"]


    return [Character(
        name=character['name'],
        traits=character['traits']
        ) for character in data]


def create_item_from_json(json_str: str) -> Item:
    """
    Takes a JSON string as input, deserializes it, and 
    converts it into a new instance of the Item class.
    
    Parameters:
        json_str (str): The JSON string to be deserialized into an Item object.
    
    Returns:
        Item: A new instance of the Item class.
    """
    json_str = json_str.strip('```json').strip('```').strip()
    data = json.loads(json_str)["items"]


    return [Item(
        name=item['name'],
        price=item['price'],
        weight=item['weight'],
        type_=item['type']
        ) for item in data]
