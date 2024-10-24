"""
This is a mapper for Tropes, it maps scene from a JSON string into a Trope Object and vice versa
"""

import json
from trope import Trope


def create_json_from_tropes(tropes: dict) -> str:
    """
    Creates a JSON string representing a list of Trope objects

    :param dict tropes: A list of Trope objects to be serialized into a JSON string
    :return: A JSON string representing the Trope objects
    :rtype: str
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
