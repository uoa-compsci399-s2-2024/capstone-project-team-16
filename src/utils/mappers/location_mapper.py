"""
This is a JSON to object mapper for Locations  it turns a JSON string to a Character Object
"""
import json
import random
from location import Location
from world import World


def create_location_from_json(json_str: str, world: World, previous_location_id: int or None = None) -> list[Location]:
    """
    Takes a JSON string as input, deserializes it,
    and converts it into a new instance of the Location class.

    Parameters:
        json_str (str): The JSON string to be deserialized into a Location object.
        previous_location (Optional[Location]|None): The previous Location object.
        world (World): the World Object
    Returns:
        list[Location]: A list of new instances of the Location class.
    """
    json_str = json_str.strip('```json').strip('```').strip()
    data = json.loads(json_str)["locations"]

    # There probably is a better way of doing this and im just stuck in my own head with how I want
    # locations to work

    # Section list
    section = []
    # Creates a location and adds to the list
    for location in data:
        section.append(Location(location['name'], location['description']))

    # Neighbour mapping
    # rules
    #The connections are Bi Directional. The graph must also be connected. No edges to self,
    # multiple edges to the same node

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
        if random.randrange(1, 11) <= 3:
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
        world.world.locations[previous_location_id].remove_neighbor(None)
        # Create the replacement edge to the new sector
        world.locations[previous_location_id].add_neighbor(random_location)
        random_location.add_neighbor(world.locations[previous_location_id])

    return section
