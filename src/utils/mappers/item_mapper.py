"""
This is a mapper for Items, it maps items from a JSON string into an Item Object and vice versa
"""
import json
from item import Item


def create_item_from_json(json_str: str) -> list[Item]:
    """
    Creates a list of Item objects from a JSON string

    :param str json_str: A JSON string to be deserialized into a list of Item Objects
    :return: A list of new instances of the Item class
    :rtype: list[Item]
    """
    json_str = json_str.strip('```json').strip('```').strip()
    data = json.loads(json_str)["items"]

    return [Item(
        name=item['name'],
        price=item['price'],
        weight=item['weight'],
        category=item['category']
    ) for item in data]


def create_json_from_item(items: dict) -> str:
    """
    Creates a JSON string representing a list of Item objects

    :param dict items: A list of Item objects to be serialized into a JSON string
    :return: A JSON string representing the Item objects
    :rtype: str
    """
    return json.dumps({'items': [{
        "id": key,
        "name": item.name,
        "price": item.price,
        "weight": item.weight,
        "category": item.category
    } for key, item in items.items() if isinstance(item, Item)]})


def create_item_from_json_save(item: dict) -> Item:
    """
    Creates an Item object from a JSON string representing saved game data

    :param dict item: A JSON string to be deserialized into an Item object
    :return: A new instance of the Item class
    :rtype: Item
    """
    return Item(
        name=item['name'],
        price=item['price'],
        weight=item['weight'],
        category=item['category'],
        id=item['id']
    )


def create_item_from_list(items: list[dict]) -> list[Item]:
    """
    Creates several Item objects from a list of JSON strings

    :param list[dict] items: A list of JSON strings to be deserialized into Item objects
    :return: A list of new instances of the Item class
    :rtype: list[Item]
    """
    return [Item(
        name=item['name'],
        price=item['price'],
        weight=item['weight'],
        category=item['category']
    ) for item in items]
