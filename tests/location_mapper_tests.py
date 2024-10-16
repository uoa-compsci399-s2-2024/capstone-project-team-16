import json
import pytest
import random

from src.character import Character
from src.item import Item
from src.location import Location
from src.utils.mappers.location_mapper import create_location_from_json
from src.world import World


@pytest.fixture
def jsonstr():
    with open("test_json_files/location_JSON_1.json") as json_file:
        location_response = json.load(json_file)
    json_file.close()
    return location_response


@pytest.fixture
def world():
    world = World()
    return world


def test_json_to_object_mapper(jsonstr, world):
    # set seed as the mapper object assigns neighbors randomly
    random.seed(42)

    # use the mapper class to create the locations
    locations = create_location_from_json(jsonstr, world)

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
