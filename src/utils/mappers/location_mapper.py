"""
This is a mapper for Locations, it maps locations from a JSON string into a Location Object and vice versa
"""
import json
import random
from location import Location
from world import World
from utils.mappers import item_mapper, character_mapper


def create_location_from_json(json_str: str, world: World, previous_location_id: int or None = None) -> list[Location]:
    """
    Creates a list of Location objects from a JSON string

    :param str json_str: A JSON string to be deserialized into a list of Location Objects
    :param World world: The World object
    :param previous_location_id: The id of the previous Location object, defaults to None
    :type previous_location_id: integer or None
    :return: A list of new instances of the Item class
    :rtype: list[Location]
    """
    json_str = json_str.strip('```json').strip('```').strip()
    data = json.loads(json_str)["locations"]

    # Section list
    section = []
    # Creates a location and adds to the list
    for location in data:
        new_location = Location(location['name'], location['description'])
        characters = character_mapper.create_character_from_list(location['characters'])
        items = item_mapper.create_item_from_list(location['items'])
        for character in characters:
            world.add_character(character)
            new_location.add_character(character.id_)

        for item in items:
            world.add_item(item)
            new_location.add_item(item.id_)

        section.append(new_location)

    # Neighbour mapping
    # Rules: connections are bidirectional, graph must be connected, no edges to self, multiple edges to the same node
    none_edge_made = False
    for location in section:
        degree = random.randrange(1, 3)
        for i in range(degree):
            if len(location.neighbors) <= degree:
                neighbour = None
                while not neighbour:
                    random_neighbour = random.choice(section)
                    if random_neighbour not in location.neighbors and random_neighbour != location:
                        neighbour = random_neighbour
                # Found a suitable neighbour
                location.add_neighbor(neighbour)
                neighbour.add_neighbor(location)
        # Chance to have a loose edge 30% chance to have a null neighbour.
        if random.randint(1, 10) <= 3:
            location.add_neighbor(None)
            none_edge_made = True

    # This is to guarantee at least 1 none edge so the player can explore
    if not none_edge_made:
        random_location = random.choice(section)
        random_location.add_neighbor(None)

    # Connect randomly to the world from previous node
    if previous_location_id is not None:
        random_location = random.choice(section)
        # Remove the None from neighbours of the previous location
        world.locations[previous_location_id].remove_neighbor(None)
        # Create the replacement edge to the new sector
        world.locations[previous_location_id].add_neighbor(random_location)
        random_location.add_neighbor(world.locations[previous_location_id])

    return section


def create_json_from_locations(locations: dict) -> str:
    """
    Creates a JSON string representing a list of Location objects

    :param dict locations: A list of Location objects to be serialized into a JSON string
    :return: A JSON string representing the Location objects
    :rtype: str
    """
    return json.dumps({
        "locations": [
            {
                "id": key,
                "name": location.name,
                "description": location.description,
                "neighbours": [neighbour.id_ for neighbour in location.neighbors if isinstance(neighbour, Location)],
                "coords": location.coords,
                "characters": location.characters,
                "items": location.items
            } for key, location in locations.items() if isinstance(location, Location)
        ]
    })


def create_location_from_json_save(location: dict) -> Location:
    """
    Creates a Location object from a JSON string representing saved game data

    :param dict location: A JSON string to be deserialized into a Character object
    :return: A new instance of the Location class
    :rtype: Location
    """
    return Location(
        name=location['name'],
        description=location['description'],
        coords=location['coords'],
        characters=location['characters'],
        items=location['items'],
        new_id=location['id']
    )
