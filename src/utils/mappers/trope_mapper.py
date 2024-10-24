"""
This is a json to object Mapper for tropes, saving a trope for the game to use
"""

import json
from trope import Trope


def create_trope_from_json(json_str: str) -> list:
    """
    Takes a JSON string as input, deserializes it, and
    converts it into a list of tropes.

    Parameters:
        json_str (str): The JSON string to be deserialized into an list of tropes.

    Returns:
        Item: A list of tropes.
    """
    json_str = json_str.strip('```json').strip('```').strip()
    data = json.loads(json_str)["tropes"]

    return [(Trope(trope["name"]), Trope(trope["description"], Trope(trope["conflicts"]))) for trope in data]

def create_json_from_tropes(tropes: dict) -> str:
    """
    Takes a trope as input, serializes it, and
    converts it into a JSON string.

    Parameters:
        tropes (list[Trope]): The tropes to be serialized into a JSON string.

    Returns:
        str: A JSON string representing the trope.
    """
    return json.dumps({"tropes": [{
        "id": key,
        "name": trope.name,
        "description": trope.description,
        "conflicts": trope.conflicts
    } for key, trope in tropes.items() if isinstance(trope, Trope)]})

def create_trope_from_json_save(trope: dict) -> Trope:
    """
    Takes a dict as input, deserializes it, and
    converts it into a new instance of the Trope class.

    Parameters:
        trope (dict): The dict to be deserialized into a Trope object.

    Returns:
        Trope: A new instance of the Trope class.
    """
    return Trope(
        id_=trope['id'],
        name=trope['name'],
        description=trope['description'],
        conflicts=trope['conflicts']
    )