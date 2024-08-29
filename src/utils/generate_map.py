from src.location import Location
from prompt import chat_with_gpt
from templates import location_template
import json

'''
V1.0 version of location initilisation prompt used to test if creating Location Objects works correctly



Create {quantity} location/s with a name and a description of the area. The locations should logically connect to each other, and are allowed to have cycles. The rooms should also allow neighbours to unknown locations and these should be represented as a Neighbour of Null. No more than 30% of the locations should have a Null Neighbor.

Keep the location consistent with the tropes of {tropes} and the themes of {themes}.

Return this in JSON format. Following this format as an example: 
{ 
"name": Location 
"description": Description of Location 
"neighbours": A List of Neighbouring locations 
}



'''


def generate_initial_locations():
    # Prompt the API for an initial Location for the story world
    # location_json_from_api = chat_with_gpt()

    # TODO Remove Manual Testing of prompts
    with open('location.json', 'r') as file:
        location_list = json.load(file)
    file.close()

    created_locations = []
    location_neighbour_dict = {}

    location_dict = {}

    # Temp ID counter
    i = 0

    # Creates a list of created locations
    for location in location_list:
        created_locations.append(Location(i, location['name'], [], [], location['description'], []))
        location_neighbour_dict[created_locations[-1]] = location['neighbours']
        location_dict[location['name']] = created_locations[-1]
        i += 1

    for location in location_neighbour_dict:
        for neighbour in location_neighbour_dict[location]:
            if neighbour is None:
                location.add_neighbor(None)
            else:
                location.add_neighbor(location_dict[neighbour])

    for location in created_locations:
        print(location.name)
        print([neighbour.name if neighbour is not None else neighbour for neighbour in location.neighbors])
        print("\n")


def generate_connected_locations():
    raise NotImplemented


generate_initial_locations()
