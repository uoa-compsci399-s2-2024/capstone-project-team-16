"""Game Loop"""

from actions import move_character
from character import Character
from location import Location
from world import World
from openai import OpenAI
from utils.templates import demo_choices_movement_template, scene_template
from utils.prompt import chat_with_gpt
from utils.mappers import scene_mapper, choice_mapper
from utils.playthroughs import write_scene_and_choice, save_playthrough_as_file, wipe_temp_file

# This is just for readability's sake
import textwrap

def choice_selection(choices: list[tuple]) -> str:
    '''Function to get user input for the choice'''

    updated_choices = [choices[i][0] for i in range(len(choices))]

    for i, choice in enumerate(updated_choices, start=1):
        print(f"{i}. {choice}")
    
    while True:
        try:
            selection = int(input("> "))
            if 1 <= selection <= len(updated_choices):
                return choices[selection - 1]
            else:
                print("Invalid number")
        except:
            print("Not number") #will need to change these



def display_scene(client: OpenAI, location: Location, world: World) -> str:
    """Function to display the scene the player is in"""
    scene = chat_with_gpt(
        client=client,
        system_message="You are a knowledgable chatbot that generates a scene description",
        user_message=scene_template(location.name, location.description,
                                    [world.items[item_id] for item_id in location.items],
                                    [world.characters[character_id] for character_id in location.characters if (world.characters[character_id]).playable is not True]),
        context=False,
        tokens=500
    )

    mapped_scene = scene_mapper.create_scene_from_json(scene)
    #print(textwrap.fill(mapped_scene, 100))
    return textwrap.fill(mapped_scene, 100)
  

def game_loop(player: Character, world: World, client: OpenAI) -> None:

    game_over = False

    while not game_over:

        current_location = world.locations[player.current_location]
        # Displays the Scene for the user to view
        print("")
        #display_scene(client, current_location, world)
        mapped_scene = display_scene(client, current_location, world)
        print(mapped_scene)
        print("")

        choices = chat_with_gpt(
            client=client,
            system_message="You are a knowledgable chatbot that generates choices",
            user_message=demo_choices_movement_template(
                [f"{neighbor.name}({neighbor.id_})" if neighbor is not None else None for neighbor
                 in current_location.neighbors]),
            context=False,
            tokens=500,
            temp=0.5
        )
        mapped_choices = choice_mapper.create_demo_choices_from_json(choices)

        # Returns the tuple choice of (desc, id)
        player_choice = choice_selection(mapped_choices)
        if player_choice[1] is not None:
            new_location = world.locations[player_choice[1]]
        else:
            new_location = None
        
        #store the scene and choices in temp file
        write_scene_and_choice(mapped_scene, player_choice)
        
        # use the move action to move the player
        move_character(player, current_location, new_location, client, world)
    
    # create a fresh txt file for this playthrough, store it and wipe temp for repeated use
    save_playthrough_as_file()
    wipe_temp_file()