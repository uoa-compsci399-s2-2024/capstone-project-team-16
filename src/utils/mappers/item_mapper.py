"""
This is a JSON to object mapper for Items it turns a JSON string to a Item Object
"""
import json
from item import Item


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
        category=item['category']
    ) for item in data]

def create_json_from_item(items: dict) -> str:
    """
    Takes a Item object as input, serializes it, and
    converts it into a JSON string.

    Parameters:
        items (list[Item]): The Item objects to be serialized into a JSON string.

    Returns:
        str: A JSON string representing the Item object.
    """
    return json.dumps({'items':[{
        "id": key,
        "name": item.name,
        "price": item.price,
        "weight": item.weight,
        "category": item.category
    } for key, item in items.items() if isinstance(item, Item)]})