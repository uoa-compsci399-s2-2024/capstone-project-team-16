import sys
import pytest
import os
from openai import OpenAI
from dotenv import load_dotenv
sys.path.append(os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'src')))

from item import Item
from character import Character
from location import Location
from world import World
from trope import Trope


@pytest.fixture
def item_1():
    return Item("Flaming Sword of Greatness", "Slashing", 5.0, 35.5, 0)


@pytest.fixture
def item_2():
    return Item("Cube of Force", "Wondrous Item", 1.2, 23.3, 1)


@pytest.fixture
def character_1():
    return Character("Gandalf", ["Wizard"], True, 0, {0: 1, 1: 2}, 0)


@pytest.fixture
def character_2():
    return Character("Frodo", ["Hobbit"], True, 1, {2: 1, 3: 1}, 1)


@pytest.fixture
def location_1():
    return Location("Shire", "A peaceful place", 0, [0, 1], [0, 1, 2])


@pytest.fixture
def location_2(location_1):
    return Location("Mordor", "A dangerous place", 1, [2, 3], [4, 5, 6], [location_1])


@pytest.fixture()
def trope_1():
    return Trope(0, "The Chosen One", "A normal person discovers they are the chosen one", [1])


@pytest.fixture()
def trope_2():
    return Trope(1, "The False Prophet", "A person who falsely claims to be the chosen one", [0])


@pytest.fixture
def world(location_1, character_1, item_1, trope_1):
    return World({0: location_1}, {0: item_1}, {0: character_1}, {0: trope_1}, ["Fantasy"], ["Choice1", "Choice2"],
                 ["Event1", "Event2"], 0)


@pytest.fixture()
def client():
    load_dotenv()
    openai_api_key = os.getenv('OPENAI_API_KEY')

    # initialise client
    return OpenAI(api_key=openai_api_key)


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
    assert character_1.playable is True
    assert character_1.traits == ["Wizard"]
    assert character_1.current_location == 0
    assert character_1.inventory == {0: 1, 1: 2}

    assert character_2.name == "Frodo"
    assert character_2.playable is True
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
    assert character_1.playable is False
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


def test_character_conversation_history(character_1):
    # Adding to conversation history
    character_1.add_to_conversation_history(["Hello", "Goodbye"])
    character_1.add_to_conversation_history(["Hi", "Bye"])

    # Testing conversation history
    assert character_1.conversation_history == [["Hello", "Goodbye"], ["Hi", "Bye"]]


def test_location_init(location_1, location_2):
    # Initialisation testing, Getter testing
    assert location_1.name == "Shire"
    assert location_1.characters == [0, 1]
    assert location_1.items == [0, 1, 2]
    assert location_1.description == "A peaceful place"
    assert location_1.neighbors == []
    assert location_1.coords is None

    assert location_2.name == "Mordor"
    assert location_2.characters == [2, 3]
    assert location_2.items == [4, 5, 6]
    assert location_2.description == "A dangerous place"
    assert location_2.neighbors == [location_1]
    assert location_2.coords is None


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
    location_1.coords = (1, 2)

    # Testing setters
    assert location_1.name == "The Shire"
    assert location_1.characters == [1, 2]
    assert location_1.items == [1, 2]
    assert location_1.description == "A peaceful place, home of the hobbits"
    assert location_1.connections == [1, 2, 3]
    assert location_1.coords == (1, 2)


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


def test_location_neighbor(location_1, location_2):
    # Adding neighbour
    location_1.add_neighbor(location_2)

    # Testing neighbour
    assert location_1.neighbors == [location_2]


def test_trope_init(trope_1, trope_2):
    # Initialisation testing, Getter testing
    assert trope_1.id_ == 0
    assert trope_1.name == "The Chosen One"
    assert trope_1.description == "A normal person discovers they are the chosen one"
    assert trope_1.conflicts == [1]

    assert trope_2.id_ == 1
    assert trope_2.name == "The False Prophet"
    assert trope_2.description == "A person who falsely claims to be the chosen one"
    assert trope_2.conflicts == [0]


def test_trope_equality(trope_1, trope_2):
    assert trope_1 != trope_2
    assert trope_1 == trope_1


def test_trope_hash(trope_1):
    assert hash(trope_1) == hash(trope_1.id_)


def test_trope_comparisons(trope_1, trope_2):
    assert trope_1 < trope_2
    assert trope_1 <= trope_2
    assert trope_2 > trope_1
    assert trope_2 >= trope_1


def test_trope_setters(trope_1):
    # Changing via setters
    trope_1.name = "The Anti-Hero"
    trope_1.description = "A protagonist who lacks conventional heroic qualities"
    trope_1.conflicts = [1]

    # Testing setters
    assert trope_1.name == "The Anti-Hero"
    assert trope_1.description == "A protagonist who lacks conventional heroic qualities"
    assert trope_1.conflicts == [1]


def test_world_init(world, location_1, item_1, character_1, trope_1):
    # Initialisation testing, Getter testing
    assert world.locations == {0: location_1}
    assert world.items == {0: item_1}
    assert world.characters == {0: character_1}
    assert world.tropes == {0: trope_1}
    assert world.theme == ["Fantasy"]
    assert world.choices == ["Choice1", "Choice2"]
    assert world.key_events == ["Event1", "Event2"]
    assert world.curr_story_beat == 0


def test_world_locations(world, location_1, location_2):
    # Adding location
    world.add_location(location_2)

    # Testing location
    assert world.locations == {0: location_1, 1: location_2}

    # Removing location
    world.remove_location(1)

    # Testing location
    assert world.locations == {0: location_1}


def test_world_items(world, item_1, item_2):
    # Adding item
    world.add_item(item_2)

    # Testing item
    assert world.items == {0: item_1, 1: item_2}

    # Removing item
    world.remove_item(1)

    # Testing item
    assert world.items == {0: item_1}


def test_world_characters(world, character_1, character_2):
    # Adding character
    world.add_character(character_2)

    # Testing character
    assert world.characters == {0: character_1, 1: character_2}

    # Removing character
    world.remove_character(1)

    # Testing character
    assert world.characters == {0: character_1}


def test_world_tropes(world, trope_1, trope_2):
    # Adding trope
    world.add_trope(trope_2)

    # Testing trope
    assert world.tropes == {0: trope_1, 1: trope_2}

    # Removing trope
    world.remove_trope(1)

    # Testing trope
    assert world.tropes == {0: trope_1}


def test_world_theme(world):
    # Adding theme
    world.add_theme("Sci-Fi")

    # Testing theme
    assert world.theme == ["Fantasy", "Sci-Fi"]

    # Removing theme
    world.remove_theme("Sci-Fi")

    # Testing theme
    assert world.theme == ["Fantasy"]


def test_world_key_event(world):
    # Adding key event
    world.add_key_event("Event3")

    # Testing key event
    assert world.key_events == ["Event1", "Event2", "Event3"]

    # Removing key event
    world.remove_key_event("Event3")

    # Testing key event
    assert world.key_events == ["Event1", "Event2"]


def test_world_choices(world):
    # Setting choices
    world.choices = ["Choice3", "Choice4"]

    # Testing choices
    assert world.choices == ["Choice3", "Choice4"]

    # Remove all choices
    world.delete_choices()

    # Testing choices
    assert world.choices == []


def test_world_story_beat(world):
    # Setting story beat
    world.curr_story_beat = 1

    # Testing story beat
    assert world.curr_story_beat == 1


def test_world_json_location(world):
    # Adding json location
    world.add_json_location("Location1")

    # Testing json location
    assert world.json_locations == ["Location1"]


def test_world_json_item(world):
    # Adding json item
    world.add_json_item("Item1")

    # Testing json item
    assert world.json_items == ["Item1"]


def test_world_json_character(world):
    # Adding json character
    world.add_json_character("Character1")

    # Testing json character
    assert world.json_characters == ["Character1"]
