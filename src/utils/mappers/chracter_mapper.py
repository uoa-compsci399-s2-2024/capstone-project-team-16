import json
from src.character import Character


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
