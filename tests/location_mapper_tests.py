import itertools
import json
import pytest
import random

from src.character import Character
from src.item import Item
from src.location import Location
from src.utils.mappers.location_mapper import create_location_from_json
from src.world import World


@pytest.fixture
def jsonstr_1():
    with open("tests/test_json_files/location_JSON_1.json") as json_file:
        location_response = json.load(json_file)
    json_file.close()
    return location_response

@pytest.fixture
def jsonstr_2():
    with open("tests/test_json_files/location_JSON_2.json") as json_file:
        location_response = json.load(json_file)
    json_file.close()
    return location_response

@pytest.fixture
def world():
    world = World()
    return world

@pytest.fixture
def existing_world(jsonstr_1):
    # RESET ITERATOR ITERTOOLS on a class level
    Location.id_iter = itertools.count()
    Item.id_iter = itertools.count()
    Character.id_iter = itertools.count()

    # set seed as the mapper object assigns neighbors randomly
    random.seed(42)

    existing_world = World()

    locations = create_location_from_json(jsonstr_1, existing_world)

    for location in locations:
        existing_world.add_location(location)


    return existing_world


def test_json_to_object_mapper(jsonstr_1, jsonstr_2, world):
    # set seed as the mapper object assigns neighbors randomly
    random.seed(42)

    # use the mapper class to create the locations
    locations = create_location_from_json(jsonstr_1, world)

    # add locations to the world object easy access
    for location in locations:
        world.add_location(location)

    # Check that the correct number of locations is created
    assert len(world.locations) == 5
    # Test Location ID 0 entries are correct
    assert world.locations[0].name == "The Flesh Garden"
    # Checking characters
    assert len(world.locations[0].characters) == 1
    assert isinstance(world.locations[0].characters[0], int)
    # Checking Items
    assert len(world.locations[0].items) == 1
    assert isinstance(world.locations[0].items[0], int)

    # Checking neighbours
    assert len(world.locations[0].neighbors) == 3
    for neighbor in world.locations[0].neighbors:
        assert isinstance(neighbor, (Location, type(None)))
    # Checking the names of the neighbours are correct
    assert world.locations[0].neighbors[0].name == "The Wailing Marsh"
    assert world.locations[0].neighbors[1].name == "The Abandoned Asylum"
    assert world.locations[0].neighbors[2].name == "The Shattered Cathedral"


    # Test Location ID 1 entries are correct
    assert world.locations[1].name == "The Abandoned Asylum"
    # Checking characters
    assert len(world.locations[1].characters) == 1
    assert isinstance(world.locations[1].characters[0], int)
    # Checking Items
    assert len(world.locations[1].items) == 1
    assert isinstance(world.locations[1].items[0], int)

    # Checking neighbours
    assert len(world.locations[1].neighbors) == 2
    for neighbor in world.locations[0].neighbors:
        assert isinstance(neighbor, (Location, type(None)))
    # Checking the names of the neighbours are correct
    assert world.locations[1].neighbors[0].name == "The Flesh Garden"
    assert world.locations[1].neighbors[1].name == "The Veil of Flesh"


    # Test Location ID 2 entries are correct
    assert world.locations[2].name == "The Wailing Marsh"
    # Checking characters
    assert len(world.locations[2].characters) == 1
    assert isinstance(world.locations[2].characters[0], int)
    # Checking Items
    assert len(world.locations[2].items) == 1
    assert isinstance(world.locations[2].items[0], int)

    # Checking neighbours
    assert len(world.locations[2].neighbors) == 2
    for neighbor in world.locations[2].neighbors:
        assert isinstance(neighbor, (Location, type(None)))
    # Checking the names of the neighbours are correct
    assert world.locations[2].neighbors[0].name == "The Flesh Garden"
    assert world.locations[2].neighbors[1].name == "The Veil of Flesh"


    # Test Location ID 3 entries are correct
    assert world.locations[3].name == "The Shattered Cathedral"
    # Checking characters
    assert len(world.locations[3].characters) == 1
    assert isinstance(world.locations[3].characters[0], int)
    # Checking Items
    assert len(world.locations[3].items) == 1
    assert isinstance(world.locations[3].items[0], int)

    # Checking neighbours
    assert len(world.locations[3].neighbors) == 2
    for neighbor in world.locations[3].neighbors:
        assert isinstance(neighbor, (Location, type(None)))
    # Checking the names of the neighbours are correct
    assert world.locations[3].neighbors[0].name == "The Flesh Garden"
    assert world.locations[3].neighbors[1] is None


    # Test Location ID 4 entries are correct
    assert world.locations[4].name == "The Veil of Flesh"
    # Checking characters
    assert len(world.locations[4].characters) == 1
    assert isinstance(world.locations[4].characters[0], int)
    # Checking Items
    assert len(world.locations[4].items) == 1
    assert isinstance(world.locations[4].items[0], int)

    # Checking neighbours
    assert len(world.locations[4].neighbors) == 2
    for neighbor in world.locations[4].neighbors:
        assert isinstance(neighbor, (Location, type(None)))
    # Checking the names of the neighbours are correct
    assert world.locations[4].neighbors[0].name == "The Wailing Marsh"
    assert world.locations[4].neighbors[1].name == "The Abandoned Asylum"


def test_mapping_from_none_edge(jsonstr_2, existing_world):
    """This test simulates moving along a none edge and if the mapping can handle connecting
    new locations to existing ones"""
    random.seed(42)

    # location with a None Edge
    current_location = existing_world.locations[3]

    # use the mapper class to map the locations and link to existing node
    locations = create_location_from_json(jsonstr_2, existing_world, previous_location_id=current_location.id_)

    # add locations to the existing world object for easy access
    for location in locations:
        existing_world.add_location(location)

    # Check that the previous location has had its neighbours changed to reflect the new neighbor
    # Test Location ID 3 entries are correct and have been updated
    assert existing_world.locations[3].name == "The Shattered Cathedral"
    # Checking characters
    assert len(existing_world.locations[3].characters) == 1
    assert isinstance(existing_world.locations[3].characters[0], int)
    # Checking Items
    assert len(existing_world.locations[3].items) == 1
    assert isinstance(existing_world.locations[3].items[0], int)

    # Checking neighbours
    assert len(existing_world.locations[3].neighbors) == 2
    for neighbor in existing_world.locations[3].neighbors:
        assert isinstance(neighbor, Location)
    # Checking the names of the neighbours are correct
    assert existing_world.locations[3].neighbors[0].name == "The Flesh Garden"
    assert existing_world.locations[3].neighbors[1].name == "The Ruins of Eldoria"


    # Check that the new locations are mapped correctly
    # Location start from 5 and continue upwards
    assert existing_world.locations[5].name == "The Gilded Slums"
    # Checking characters
    assert len(existing_world.locations[5].characters) == 1
    assert isinstance(existing_world.locations[3].characters[0], int)
    # Checking Items
    assert len(existing_world.locations[5].items) == 1
    assert isinstance(existing_world.locations[3].items[0], int)

    # Checking neighbours
    assert len(existing_world.locations[5].neighbors) == 3
    for neighbor in existing_world.locations[5].neighbors:
        assert isinstance(neighbor, Location)
    # Checking the names of the neighbours are correct
    assert existing_world.locations[5].neighbors[0].name == "The Forgotten Manor"
    assert existing_world.locations[5].neighbors[1].name == "The Opulent Bazaar"
    assert existing_world.locations[5].neighbors[2].name == "The Starry Outpost"


    # Location id 6 tests
    assert existing_world.locations[6].name == "The Opulent Bazaar"
    # Checking characters
    assert len(existing_world.locations[6].characters) == 1
    assert isinstance(existing_world.locations[6].characters[0], int)
    # Checking Items
    assert len(existing_world.locations[6].items) == 1
    assert isinstance(existing_world.locations[6].items[0], int)

    # Checking neighbours
    assert len(existing_world.locations[6].neighbors) == 2
    for neighbor in existing_world.locations[6].neighbors:
        assert isinstance(neighbor, Location)
    # Checking the names of the neighbours are correct
    assert existing_world.locations[6].neighbors[0].name == "The Gilded Slums"
    assert existing_world.locations[6].neighbors[1].name == "The Ruins of Eldoria"


    # Location id 7 tests
    assert existing_world.locations[7].name == "The Forgotten Manor"
    # Checking characters
    assert len(existing_world.locations[7].characters) == 1
    assert isinstance(existing_world.locations[7].characters[0], int)
    # Checking Items
    assert len(existing_world.locations[7].items) == 1
    assert isinstance(existing_world.locations[7].items[0], int)

    # Checking neighbours
    assert len(existing_world.locations[7].neighbors) == 2
    for neighbor in existing_world.locations[7].neighbors:
        assert isinstance(neighbor, Location)
    # Checking the names of the neighbours are correct
    assert existing_world.locations[7].neighbors[0].name == "The Gilded Slums"
    assert existing_world.locations[7].neighbors[1].name == "The Ruins of Eldoria"


    # Location id 8 tests
    assert existing_world.locations[8].name == "The Starry Outpost"
    # Checking characters
    assert len(existing_world.locations[8].characters) == 1
    assert isinstance(existing_world.locations[8].characters[0], int)
    # Checking Items
    assert len(existing_world.locations[8].items) == 1
    assert isinstance(existing_world.locations[8].items[0], int)

    # Checking neighbours
    assert len(existing_world.locations[8].neighbors) == 2
    for neighbor in existing_world.locations[8].neighbors:
        assert isinstance(neighbor, (Location, type(None)))
    # Checking the names of the neighbours are correct
    assert existing_world.locations[8].neighbors[0].name == "The Gilded Slums"
    assert existing_world.locations[8].neighbors[1] is None

    # Location id 9 tests
    assert existing_world.locations[9].name == "The Ruins of Eldoria"
    # Checking characters
    assert len(existing_world.locations[9].characters) == 1
    assert isinstance(existing_world.locations[9].characters[0], int)
    # Checking Items
    assert len(existing_world.locations[9].items) == 1
    assert isinstance(existing_world.locations[9].items[0], int)

    # Checking neighbours
    assert len(existing_world.locations[9].neighbors) == 3
    for neighbor in existing_world.locations[9].neighbors:
        assert isinstance(neighbor, Location)
    # Checking the names of the neighbours are correct
    assert existing_world.locations[9].neighbors[0].name == "The Forgotten Manor"
    assert existing_world.locations[9].neighbors[1].name == "The Opulent Bazaar"
    assert existing_world.locations[9].neighbors[2].name == "The Shattered Cathedral"
