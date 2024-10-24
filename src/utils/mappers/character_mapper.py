"""
This is a mapper for Characters, it maps characters from a JSON string into a Character Object and vice versa
"""
import json
from character import Character


def create_character_from_json(json_str: str) -> list[Character]:
    """
    Creates a list of Character objects from a JSON string

    :param str json_str: A JSON string to be deserialized into a list of Character objects
    :return: A list of new instances of the Character class
    :rtype: list[Character]
    """
    json_str = json_str.strip('```json').strip('```').strip()
    data = json.loads(json_str)["characters"]

    return [Character(
        name=character['name'],
        traits=character['traits']
    ) for character in data]


def create_json_from_characters(characters: dict) -> str:
    """
    Creates a JSON string representing a list of Character object

    :param dict characters: A list of Character objects to be serialized into a JSON string
    :return: A JSON string representing the Character objects
    :rtype: str
    """
    return json.dumps({'characters': [{
        "id": key,
        "playable": character.playable,
        "name": character.name,
        "traits": character.traits,
        "inventory": character.inventory,
        "location": character.current_location,  # stores current location as ID
        "conversation history": character.conversation_history
    } for key, character in characters.items() if isinstance(character, Character)]})


def create_character_from_json_save(character: dict) -> Character:
    """
    Creates a Character object from a JSON string representing saved game data

    :param dict character: A JSON string to be deserialized into a Character object
    :return: A new instance of the Character class
    :rtype: Character
    """
    # JSON states that a key has to be a string we use an int as a key this fixes the inventory
    inventory = {int(item_id): item_quantity for item_id, item_quantity in character['inventory'].items()}

    return Character(
        name=character['name'],
        traits=character['traits'],
        playable=character['playable'],
        current_location=character['location'],
        inventory=inventory,
        conversation_history=character['conversation history']
    )


def create_character_from_list(characters: list[dict]) -> list[Character]:
    """
    Creates several Character objects from a list of JSON strings

    :param list[dict] characters: A list of JSON strings to be deserialized into Character objects
    :return: A list of new instances of the Character class
    :rtype: list[Character]
    """
    return [Character(
        name=character['name'],
        traits=character['traits']
    ) for character in characters]
