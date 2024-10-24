"""
This is a JSON to object mapper for Characters it turns a JSON string to a Character Object
"""
import json
from character import Character


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

def create_json_from_characters(characters: dict) -> str:
    """
    Takes a Character object as input, serializes it,
    and converts it into a JSON string.

    Parameters:
        characters (list[Character]): A list of Character objects to be serialized into a JSON string.

    Returns:
        str: A JSON string representing the Character object.
    """
    return json.dumps({'characters': [{
        "id": key,
        "playable": character.playable,
        "name": character.name,
        "traits": character.traits,
        "inventory": character.inventory,
        "location": character.current_location #stores current location as ID
    } for key, character in characters.items() if isinstance(character, Character)]})

def create_character_from_json_save(character: dict) -> Character:
    """
    Takes a JSON string as input, deserializes it,
    and converts it into a new instance of the Character class.

    Parameters:
        character (str): The JSON string to be deserialized into a Character object.

    Returns:
        Character: A new instance of the Character class.
    """
    # JSON states that a key has to be a string we use an int as a key this fixes the inventory
    print(character)
    print(type(character['inventory']))
    inventory = {int(item_id): item_quantity for item_id, item_quantity in character['inventory'].items()}

    return Character(
        name=character['name'],
        traits=character['traits'],
        playable=character['playable'],
        current_location=character['location'],
        inventory=inventory,
        id=character['id']
    )

def create_character_from_list(characters: list[dict]) -> list[Character]:
    return [Character(
        name=character['name'],
        traits=character['traits']
    ) for character in characters]

