"""Game Loop"""

from actions import move_character
from character import Character
from location import Location
from world import World
from openai import OpenAI
from utils.templates import demo_choices_movement_template, scene_template
from utils.prompt import chat_with_gpt
from utils.mappers import scene_mapper, choice_mapper

# This is just for readability's sake
import textwrap

def choice_selection(choices: list[str]) -> str:
    '''Function to get user input for the choice'''

    for i, choice in enumerate(choices, start=1):
        print(f"{i}. {choice}")
    
    while True:
        try:
            selection = int(input("> "))
            if 1 <= selection <= len(choices):
                return choices[selection - 1]
            else:
                print("Invalid number")
        except:
            print("Not number") #will need to change these


def get_choices() -> list[str]:
    ''''Function to get choices when that is written'''
    pass


def display_scene(client: OpenAI, location: Location, world: World) -> None:
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
    print(textwrap.fill(mapped_scene, 100))


def pass_choice(choice: str) -> None:
    '''Function to process the users choice'''
    pass


def game_loop(player: Character, world: World, client: OpenAI) -> None:

    game_over = False

    while not game_over:

        current_location = world.locations[player.current_location]
        # Displays the Scene for the user to view
        display_scene(client, current_location, world)

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
        for choice in mapped_choices:
            print(mapped_choices[choice])


        input("END GAME?")
        game_over = True

        #player_choice = choice_selection(choices)
        #move_character(
        #    character_object=player,
        #    current_location=current_location,
        #    new_location=player_choice,
        #    client=client,
        #    world_object=world
        #)