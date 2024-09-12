"""This is a file of all possible actions for the game"""

import location, character, item, world
from utils.prompt import chat_with_gpt
from utils.templates import flow_on_location_template
from utils.mappers import location_mapper


def move_character(character_object: character.Character, current_location: location.Location,
                   new_location: location.Location, client: 'OpenAI', world_object: world.World):
    """This is an action to move a character from one location to another"""
    if new_location is not None:
        character_object.move(new_location.id_)
        current_location.remove_character(character_object.id_)
        new_location.add_character(character_object.id_)
    else:
        # The new location is not known and as such needs to generate a new sector of the map
        new_locations = chat_with_gpt(client,
                                      "You are a knowledgeable chatbot that creates unique items",
                                      flow_on_location_template(5, current_location.name,
                                                                list(world_object.tropes.values()),
                                                                world_object.theme),
                                      False,
                                      tokens=500)
        # Map the new Locations
        mapped_new_locations = location_mapper.create_location_from_json(
            previous_location=current_location, json_str=new_locations)

        # Add the new locations to the locations within the world
        for mapped_location in mapped_new_locations:
            world_object.add_location(mapped_location)

        # Find the connection in the new locations
        for mapped_new_location in mapped_new_locations:
            if current_location in mapped_new_location.neighbors:
                new_location = mapped_new_location

        character_object.move(new_location.id_)
        current_location.remove_character(character_object.id_)
        new_location.add_character(character_object.id_)
