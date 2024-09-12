import json
from src.location import Location


with open("location_jsons/initial_location.json") as json_file:
    initial_locations = json.load(json_file)
json_file.close()

data = initial_locations['locations']

# ------- Mapper Code ------------------
# List of created locations
created_locations = []
# Dictionary helpers to create neighbors efficiently
location_to_neighbour_dict = {}
name_to_location_dict = {}

# If the previous location is given add to the variables so neighbor creation does not error
# Creates a location and adds to the list
for location in data:
    created_locations.append(Location(location['name'], location['description']))
    location_to_neighbour_dict[created_locations[-1]] = location['neighbours']
    name_to_location_dict[location['name']] = created_locations[-1]

# Adding each neighbor to a location
for location, neighbour_list in location_to_neighbour_dict.items():

    for neighbour in neighbour_list:
        if neighbour is None:
            location.add_neighbor(None)
        else:
            location.add_neighbor(name_to_location_dict[neighbour])
# ---------------------- END OF MAPPER CODE -------------------

for location in created_locations:
    print("\n")
    print(location.name)
    print("Neihbours of ", location.name)
    for neighbour in location.neighbors:
        if neighbour is not None:
            print(neighbour.name)
        else:
            print(neighbour)