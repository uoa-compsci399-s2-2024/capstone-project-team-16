import json
from src.utils.mappers.location_mapper import create_location_from_json
from src.world import World


def jsonstr():
    with open("tests/test_json_files/location_JSON_1.json") as json_file:
        location_response = json.load(json_file)
    json_file.close()
    return location_response

def world():
    world = World()
    return world

def son_to_object_mapper(jsonstr):
    pass


jsonstr = jsonstr()
world = world()
locations = create_location_from_json(jsonstr, world)
for location in locations:
    print(f"-------Name-------\n{location.name}")
    print(f"-------Characters-\n{location.characters}")
    print(f"-------Items------\n{location.items}")
    print(f"-------Neighbours-\n{[neighbour.name if neighbour is not None else None for neighbour in location.neighbors]}")
    print("-------------------")