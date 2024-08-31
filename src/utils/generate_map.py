from src.location import Location
from prompt import chat_with_gpt
from templates import location_template
import json
'''
V1.0 version of location initilisation prompt used to test if creating Location Objects works correctly



Create {quantity} location/s with a name and a description of the area. The locations should logically connect to each other, and are allowed to have cycles. The rooms should also allow neighbours to unknown locations and these should be represented as JSON null . No more than 30% of the locations should have a null neighbour, rounding up. At least one location needs to have a null neighbour.

The description for the Location should be no longer than 100 words.

Keep the location consistent with the tropes of {tropes} and the themes of {themes}.

Return this in JSON format. Following this format as an example: 
{ 
"name": Location 
"description": Description of Location 
"neighbours": A List of Neighbouring locations allowing for null
}


'''


def generate_initial_locations() -> list[Location]:
    # Prompt the API for an initial Location for the story world
    # location_json_from_api = chat_with_gpt()

    # TODO Remove Manual Testing of prompts
    with open('initial_location.json', 'r') as file:
        location_json_from_api = json.load(file)
    file.close()

    # List of created locations
    created_locations = []

    # Dictionary mappers to create neighbors
    location_to_neighbour_dict = {}
    name_to_location_dict = {}

    # TODO Remove temporary ID counter
    location_id = 0

    # Creates a location and adds to the list
    for location in location_json_from_api:
        created_locations.append(Location(location_id, location['name'], [], [], location['description'], []))

        # Mappers for easily adding neighbors to a location
        location_to_neighbour_dict[created_locations[-1]] = location['neighbours']
        name_to_location_dict[location['name']] = created_locations[-1]

        # TODO Remove temporary ID counter
        location_id += 1

    # Adding each neighbor to a location
    for location in location_to_neighbour_dict:
        for neighbour in location_to_neighbour_dict[location]:
            if neighbour is None:
                location.add_neighbor(None)
            else:
                location.add_neighbor(name_to_location_dict[neighbour])

    return created_locations


'''
Flow on neighbor function prompt V1.0

Create {quantity} location/s with a name and a description of the area. The locations should logically connect to each other, and are allowed to have cycles. The rooms should also allow neighbours to unknown locations and these should be represented as JSON null. No more than 30% of the locations should have a null neighbour, rounding up. At least one location needs to have a null neighbour.


The description for the Location should be no longer than 100 words.

Using the previous location of {prev_location_name}, {prev_location_description}

Do not create this previous node, Exactly One of the locations generated should connect to this previous location.  Do not allow more than one new location to connect to this previous location. 

Keep the location consistent with the tropes of {tropes} and the themes of {themes}.

Return this in JSON format. Following this format as an example: 
{ 
"name": Location 
"description": Description of Location 
"neighbours": A List of Neighbouring locations allowing for null 
}
'''


def generate_connected_locations(prev_location: Location) -> list[Location]:
    # Prompt the API for an initial Location for the story world
    # location_json_from_api = chat_with_gpt()

    # TODO Remove Manual Testing of prompts
    with open('flow_on_location.json', 'r') as file:
        location_json_from_api = json.load(file)
    file.close()

    # List of created locations
    created_locations = [prev_location]

    # Dictionary mappers to create neighbors
    location_to_neighbour_dict = {}
    name_to_location_dict = {prev_location.name: prev_location}

    # TODO Remove temporary ID counter
    location_id = 0

    # Creates a location and adds to the list
    for location in location_json_from_api:
        created_locations.append(Location(location_id, location['name'], [], [], location['description'], []))

        # Mappers for easily adding neighbors to a location
        location_to_neighbour_dict[created_locations[-1]] = location['neighbours']
        name_to_location_dict[location['name']] = created_locations[-1]

        # TODO Remove temporary ID counter
        location_id += 1

    # Adding each neighbor to a location
    for location in location_to_neighbour_dict:
        for neighbour in location_to_neighbour_dict[location]:
            if neighbour is None:
                location.add_neighbor(None)
            else:
                location.add_neighbor(name_to_location_dict[neighbour])

    return created_locations


locations = generate_initial_locations()
new_locations = generate_connected_locations(locations[0])
for location in new_locations:
    print(location.name)
    for neighbour in location.neighbors:
        if neighbour is None:
            print(neighbour)
        else:
            print(neighbour.name)
    print("\n")