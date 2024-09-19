"""Game Loop"""

# This is just for readability's sake
import textwrap
from openai import OpenAI

from actions import process_user_choice
from character import Character
from location import Location
from world import World
from utils.templates import flow_on_choices_template, scene_template
from utils.prompt import chat_with_gpt
from utils.mappers import scene_mapper, choice_mapper

def choice_selection(choices: list[tuple]) -> str:
    """Function to get user input for the choice"""

    updated_choices = [choices[i][0] for i in range(len(choices))]
    selection = None

    for i, choice in enumerate(updated_choices, start=1):
        print(f"{i}. {choice}")

    while not selection:
        user_input = input("> ")
        if not user_input.isdigit():
            print("Please enter a number")
            continue
        else:
            user_input = int(user_input)

        if user_input <= len(choices) and user_input > 0:
            selection = choices[user_input - 1]
        else:
            print("Invalid number")


    return selection



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



def game_loop(player: Character, world: World, client: OpenAI) -> None:
    """The main game loop, defines what happens after every user choice"""
    game_over = False

    while not game_over:

        current_location = world.locations[player.current_location]
        # Displays the Scene for the user to view
        print("")
        display_scene(client, current_location, world)
        print("")

        choices = chat_with_gpt(
            client=client,
            system_message="You are a knowledgable chatbot that generates choices",
            user_message=flow_on_choices_template(
                4, world.tropes, world.theme, [f"{neighbor.name}({neighbor.id_})" if neighbor is not None else None for neighbor
                in current_location.neighbors], [world.characters[cid] for cid in current_location.characters],
                [world.items[iid] for iid in current_location.items], ["move location"]),
            context=False,
            tokens=500,
            temp=0.5
        )
        mapped_choices = choice_mapper.create_choices_from_json(choices)

        # Returns the tuple choice of (desc, id)
        player_choice = choice_selection(mapped_choices)
        process_user_choice(player_choice[1], [client, world, player, current_location])
        #if player_choice[1] is not None:
        #    new_location = world.locations[player_choice[1]]
        #else:
        #    new_location = None
        # use the move action to move the player
