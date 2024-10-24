"""
This is a json to object Mapper for choices creating a list of choices for the game to display
"""

import json


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

    return [(choice['description'], choice['actions'], choice['actions_performed']) for choice in data]

def create_demo_choices_from_json(json_str: str) -> list:
    json_str = json_str.strip('```json').strip('```').strip()
    data = json.loads(json_str)["choices"]

    choices = []
    for choice in data:
        choices.append((choice['description'], choice['new_location']))
    return choices

def create_json_from_choices(choices: tuple[str]) -> str:
    """
    Takes a list of choices as input, serializes it, and
    converts it into a JSON string.

    Parameters:
        choices (list[str]): The list of choices to be serialized into a JSON string.

    Returns:
        str: A JSON string representing the list of choices.
    """
    return json.dumps({
        "choices": [
            {
                "description": choice[0],
                "actions": choice[1]
            } for choice in choices
        ]
    })