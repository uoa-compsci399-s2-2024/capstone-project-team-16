"""
This is a mapper for choices, it maps choices from a JSON string into a list of strings and vice versa
"""

import json


def create_choices_from_json(json_str: str) -> list[tuple]:
    """
    Creates a list of choices from a JSON string

    :param str json_str: A JSON string to be deserialized into a list of choices
    :return: A list of choices
    :rtype: list[tuple]
    """
    json_str = json_str.strip('```json').strip('```').strip()
    data = json.loads(json_str)["choices"]

    return [(choice['description'], choice['actions'], choice['actions_performed']) for choice in data]


def create_json_from_choices(choices: tuple[str]) -> str:
    """
    Creates a JSON string representing a list of choices

    :param tuple[str] choices: A list of choices to be serialized into a JSON string
    :return: A JSON string representing the choices
    :rtype: str
    """
    return json.dumps({
        "choices": [
            {
                "description": choice[0],
                "actions": choice[1]
            } for choice in choices
        ]
    })
