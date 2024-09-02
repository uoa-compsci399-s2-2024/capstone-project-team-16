"""Mapper helper functions to convert JSON output
from the API into instances of our defined classes."""

import json
from src.location import Location
from src.character import Character
from src.item import Item


def create_location_from_json(json_str: str,
                              previous_location: Location or None = None) -> list[Location]:
    """
    Takes a JSON string as input, deserializes it,
    and converts it into a new instance of the Location class.
    
    Parameters:
        json_str (str): The JSON string to be deserialized into a Location object.
        previous_location (Optional[Location]|None): The previous Location object.
    
    Returns:
        list[Location]: A list of new instances of the Location class.
    """
    json_str = json_str.strip('```json').strip('```').strip()
    data = json.loads(json_str)["locations"]

    # List of created locations
    created_locations = []
    # Dictionary helpers to create neighbors efficiently
    location_to_neighbour_dict = {}
    name_to_location_dict = {}

    # If the previous location is given add to the variables so neighbor creation does not error
    if previous_location is not None:
        created_locations.append(previous_location)
        name_to_location_dict[previous_location.name] = previous_location

    # Creates a location and adds to the list
    for location in data:
        created_locations.append(Location(location['name'], location['description']))
        location_to_neighbour_dict[created_locations[-1]] = location['neighbours']
        name_to_location_dict[location['name']] = created_locations[-1]

    # Adding each neighbor to a location
    for location, neighbour_list in location_to_neighbour_dict.items():
        for neighbour in neighbour_list:
            if neighbour is None:
                location.add_neighbor(None)
            else:
                location.add_neighbor(neighbour)

    # Remove the existing previous location so duplication does not occur
    if previous_location is not None:
        created_locations.pop(0)
    return created_locations


def create_character_from_json(json_str: str) -> list[Character]:
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


def create_item_from_json(json_str: str) -> list[Item]:
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


def create_choices_from_json(json_str: str) -> list:
    """
    Takes a JSON string as input, deserializes it, and
    converts it into a list of choices.

    Parameters:
        json_str (str): The JSON string to be deserialized into an list of choices.

    Returns:
        Item: A list of choices.
    """
    json_str = json_str.strip('```json').strip('```').strip()
    data = json.loads(json_str)["choices"]

    return [choice['description'] for choice in data]
