import pytest
from src.item import Item
from src.character import Character
from src.location import Location

@pytest.fixture
def item_1():
    return Item("Flaming Sword of Greatness", "Slashing", 5.0, 35.5)

@pytest.fixture
def item_2():
    return Item("Cube of Force", "Wondrous Item", 1.2, 23.3)

@pytest.fixture
def character_1():
    return Character("Gandalf", ["Wizard"], True, 0, {0: 1, 1: 2})

@pytest.fixture
def character_2():
    return Character("Frodo", ["Hobbit"], True, 1, {2: 1, 3: 1})

@pytest.fixture
def location_1():
    return Location("Shire", "A peaceful place", [0,1], [0,1], [0, 1, 2])

@pytest.fixture
def location_2():
    return Location("Mordor",  "A dangerous place", [2,3], [2,3], [4, 5, 6])

def test_item_init(item_1, item_2):
    # Initialisation testing, Getter testing
    assert str(item_1) == "Name: Flaming Sword of Greatness\nWeight: 5.0\nPrice: 35.5\nType: Slashing"
    assert item_1.id_ == 0
    assert item_1.name == "Flaming Sword of Greatness"
    assert item_1.category == "Slashing"
    assert item_1.weight == 5.0
    assert item_1.price == 35.5

    assert str(item_2) == "Name: Cube of Force\nWeight: 1.2\nPrice: 23.3\nType: Wondrous Item"
    assert item_2.id_ == 1
    assert item_2.name == "Cube of Force"
    assert item_2.category == "Wondrous Item"
    assert item_2.weight == 1.2
    assert item_2.price == 23.3


def test_item_equality(item_1, item_2):
    assert item_1 != item_2
    assert item_1 == item_1

def test_item_hash(item_1):
    assert hash(item_1) == hash(item_1.id_)

def test_item_comparisons(item_1, item_2):
    assert item_1 > item_2
    assert item_1 >= item_2
    assert item_2 < item_1
    assert item_2 <= item_1

def test_item_setters(item_1):

    # Changing via setters
    item_1.name = "Broken Flaming Sword of Greatness"
    item_1.category = "Inert"
    item_1.weight = 0.6
    item_1.price = 5.0

    # Testing setters
    assert str(item_1) == "Name: Broken Flaming Sword of Greatness\nWeight: 0.6\nPrice: 5.0\nType: Inert"
    assert item_1.name == "Broken Flaming Sword of Greatness"
    assert item_1.category == "Inert"
    assert item_1.weight == 0.6
    assert item_1.price == 5.0


def test_character_init(character_1, character_2):
    # Initialisation testing, Getter testing
    assert character_1.name == "Gandalf"
    assert character_1.playable == True
    assert character_1.traits == ["Wizard"]
    assert character_1.current_location == 0
    assert character_1.inventory == {0: 1, 1: 2}

    assert character_2.name == "Frodo"
    assert character_2.playable == True
    assert character_2.traits == ["Hobbit"]
    assert character_2.current_location == 1
    assert character_2.inventory == {2: 1, 3: 1}

def test_character_equality(character_1, character_2):
    assert character_1 != character_2
    assert character_1 == character_1

def test_character_hash(character_1):
    assert hash(character_1) == hash(character_1.id_)

def test_character_comparisons(character_1, character_2):
    assert character_1 > character_2
    assert character_1 >= character_2
    assert character_2 < character_1
    assert character_2 <= character_1

def test_character_setters(character_1):

    # Changing via setters
    character_1.name = "Gandalf the Grey"
    character_1.playable = False
    character_1.traits = ["Wizard", "Grey"]
    character_1.current_location = 1
    character_1.inventory = {0: 2, 1: 1}

    # Testing setters
    assert character_1.name == "Gandalf the Grey"
    assert character_1.playable == False
    assert character_1.traits == ["Wizard", "Grey"]
    assert character_1.current_location == 1
    assert character_1.inventory == {0: 2, 1: 1}
    
def test_character_inventory(character_1):
    # Adding to inventory
    character_1.add_to_inventory(0, 1)
    character_1.add_to_inventory(1, 1)
    character_1.add_to_inventory(2, 1)
    character_1.add_to_inventory(3, 1)

    # Testing inventory
    assert character_1.inventory == {0: 2, 1: 3, 2: 1, 3: 1}

    # Removing from inventory
    character_1.remove_from_inventory(0, 1)
    character_1.remove_from_inventory(1, 1)
    character_1.remove_from_inventory(2, 1)
    character_1.remove_from_inventory(3, 1)

    # Testing inventory
    assert character_1.inventory == {0: 1, 1: 2}

def test_character_move(character_1):
    # Moving character
    character_1.move(2)

    # Testing move
    assert character_1.current_location == 2

def test_location_init(location_1, location_2):
    # Initialisation testing, Getter testing
    assert location_1.name == "Shire"
    assert location_1.characters == [0, 1]
    assert location_1.items == [0, 1]
    assert location_1.description == "A peaceful place"
    assert location_1.neighbors == [0, 1, 2]

    assert location_2.name == "Mordor"
    assert location_2.characters == [2, 3]
    assert location_2.items == [2, 3]
    assert location_2.description == "A dangerous place"
    assert location_2.neighbors == [4, 5, 6]

def test_location_equality(location_1, location_2):
    assert location_1 != location_2
    assert location_1 == location_1

def test_location_hash(location_1):
    assert hash(location_1) == hash(location_1.id_)

def test_location_comparisons(location_1, location_2):
    assert location_1 > location_2
    assert location_1 >= location_2
    assert location_2 < location_1
    assert location_2 <= location_1

def test_location_setters(location_1):
    # Changing via setters
    location_1.name = "The Shire"
    location_1.characters = [1, 2]
    location_1.items = [1, 2]
    location_1.description = "A peaceful place, home of the hobbits"
    location_1.connections = [1, 2, 3]

    # Testing setters
    assert location_1.name == "The Shire"
    assert location_1.characters == [1, 2]
    assert location_1.items == [1, 2]
    assert location_1.description == "A peaceful place, home of the hobbits"
    assert location_1.connections == [1, 2, 3]

def test_location_items(location_1):
    # Adding and removing items
    location_1.add_item(2)
    location_1.add_item(3)
    location_1.remove_item(0)

    # Testing items
    assert location_1.items == [1, 2, 3]

def test_location_characters(location_1):
    # Adding and removing characters
    location_1.add_character(2)
    location_1.add_character(3)
    location_1.remove_character(0)

    # Testing characters
    assert location_1.characters == [1, 2, 3]

def test_location_neighbor(location_1):
    # Adding neighbour
    location_1.add_neighbor(3)

    # Testing neighbour
    assert location_1.neighbors == [0, 1, 2, 3]

def test_location_populate(location_1):
    #placeholder for when this function is implemented
    pass