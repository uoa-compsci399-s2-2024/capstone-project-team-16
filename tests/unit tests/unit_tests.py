import pytest
from src.item import Item


def test_item_init():
    items_from_api = [{"ID": 0,
                       "name": "Flaming Sword of Greatness",
                       "type": "Slashing",
                       "weight": 5.0,
                       "price": 35.5,
                       "quantity": 1},
                      {"ID": 1,
                       "name": "Cube of Force",
                       "type": "Wondrous Item",
                       "weight": 1.2,
                       "price": 23.3,
                       "quantity": 2}]

    item_list = [Item(item["ID"], item["name"], item["type"], item["weight"], item["price"], item["quantity"]) for item
                 in items_from_api]

    # Initialisation testing, Getter tes
    item_1 = item_list[0]
    assert str(item_1) == "Flaming Sword of Greatness x1"
    assert item_1.ID == 0
    assert item_1.name == "Flaming Sword of Greatness"
    assert item_1.type == "Slashing"
    assert item_1.weight == 5.0
    assert item_1.price == 35.5
    assert item_1.quantity == 1

    item_2 = item_list[1]
    assert str(item_2) == "Cube of Force x2"
    assert item_2.ID == 1
    assert item_2.name == "Cube of Force"
    assert item_2.type == "Wondrous Item"
    assert item_2.weight == 1.2
    assert item_2.price == 23.3
    assert item_2.quantity == 2


def test_item_equality():
    items_from_api = [{"ID": 0,
                       "name": "Flaming Sword of Greatness",
                       "type": "Slashing",
                       "weight": 5.0,
                       "price": 35.5,
                       "quantity": 1},
                      {"ID": 1,
                       "name": "Cube of Force",
                       "type": "Wondrous Item",
                       "weight": 1.2,
                       "price": 23.3,
                       "quantity": 2}]

    item_list = [Item(item["ID"], item["name"], item["type"], item["weight"], item["price"], item["quantity"]) for item
                 in items_from_api]

    item_1 = item_list[0]
    item_2 = item_list[1]

    assert item_1 != item_2


def test_item_setters():
    items_from_api = [{"ID": 0,
                       "name": "Flaming Sword of Greatness",
                       "type": "Slashing",
                       "weight": 5.0,
                       "price": 35.5,
                       "quantity": 1},
                      {"ID": 1,
                       "name": "Cube of Force",
                       "type": "Wondrous Item",
                       "weight": 1.2,
                       "price": 23.3,
                       "quantity": 2}]

    item_list = [Item(item["ID"], item["name"], item["type"], item["weight"], item["price"], item["quantity"]) for item
                 in items_from_api]

    item_1 = item_list[0]
    item_2 = item_list[1]

    # Changing via setters
    item_1.name = "Broken Flaming Sword of Greatness"
    item_1.type = "Inert"
    item_1.weight = 0.6
    item_1.price = 5.0
    item_1.add(2)

    # Testing setters
    assert str(item_1) == "Broken Flaming Sword of Greatness x3"
    assert item_1.ID == 0
    assert item_1.name == "Broken Flaming Sword of Greatness"
    assert item_1.type == "Inert"
    assert item_1.weight == 0.6
    assert item_1.price == 5.0
    assert item_1.quantity == 3


def test_character_init():
    characters_from_api = [{"ID": 0,}]