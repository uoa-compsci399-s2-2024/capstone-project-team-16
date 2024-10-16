"""This is a file of all possible actions for the game"""
import openai

from utils.prompt import chat_with_gpt
from utils.templates import (location_template, location_system_message, dialog_system_message,
                             dismissive_dialog_template, talkative_dialog_template)
from utils.mappers import location_mapper, dialog_mapper
from utils.structures import SectionStructure, DismissiveDialogStructure, TalkativeDialogStructure

import random


def move_character(new_location_id: str, args: list) -> None:
    """This is an action to move a character from one location to another"""
    client = args[0]
    world_object = args[1]
    character_object = args[2]
    current_location = args[3]

    if new_location_id is None:
        new_location = None
    elif new_location_id == "unknown":
        new_location = current_location
    else:
        new_location_id = int(new_location_id)
        new_location = world_object.locations[new_location_id]

    if new_location is not None:
        character_object.move(new_location.id_)
        current_location.remove_character(character_object.id_)
        new_location.add_character(character_object.id_)
    else:
        # The new location is not known and as such needs to generate a new sector of the map
        new_locations = None
        while not new_locations:
            try:
                new_locations = chat_with_gpt(client,
                                              location_system_message(),
                                              location_template(5, current_location.name,
                                                                list(world_object.tropes.values()),
                                                                world_object.theme),
                                              False,
                                              tokens=500,
                                              structure=SectionStructure)
            except openai.LengthFinishReasonError:
                print("Token Count Error, Not provided enough tokens")
        # Map the new Locations
        mapped_new_locations = location_mapper.create_location_from_json(
            previous_location=current_location.id_, json_str=new_locations, world=world_object)

        # Add the new locations to the locations within the world
        for mapped_location in mapped_new_locations:
            world_object.add_location(mapped_location)

        # Find the connection in the new locations
        for mapped_new_location in mapped_new_locations:
            if current_location in mapped_new_location.neighbors:
                new_location = mapped_new_location

        # DIRTY IF STATEMENT THIS IS HERE DUE TO A PROMPT ERORR OCCURING
        if new_location is not None:
            character_object.move(new_location.id_)
            current_location.remove_character(character_object.id_)
            new_location.add_character(character_object.id_)
        else:
            print("DEBUG: REAL SORRY THIS IS AN ISSUE WITH FLOW ON LOCATION NOT CONNECTING "
                  "SO SORRY CANT MOVE LOCATIONS :(")


def interact_with_item(item_to_interact_id: int, args: list) -> None:
    """An action to have the player interact with an item"""
    client = args[0]
    world_object = args[1]
    character_object = args[2]
    current_location = args[3]
    if item_to_interact_id is None:
        item_to_interact = None
    else:
        item_to_interact = world_object.items[item_to_interact_id]
        world_object.add_key_event(f"Player's character, {character_object.name},"
            f"interacted with {item_to_interact} at {current_location}")
            # note that this means in cases 
            # where we both move and interact w item, we need to always process
            # moving first - should be doable with structured outputs

def pick_up_item(item_to_pick_up_id: int, args: list) -> None:
    """An action to have the player pick an item up and put it in their inventory"""
    client = args[0]
    world_object = args[1]
    character_object = args[2]
    current_location = args[3]
    if item_to_pick_up_id is None:
        item_to_pick_up = None
    else:
        item_to_pick_up = world_object.items[item_to_pick_up_id]
        character_object.add_to_inventory(item_to_pick_up_id, 1)
        current_location.remove_item(item_to_pick_up_id)
        world_object.add_key_event(f"Player's character, {character_object.name},"
            f"picked up {item_to_pick_up.name} at {current_location.name}")

def put_down_item(item_to_put_down_id: int, args: list) -> None:
    """An action to have the player put an item down and remove it from their inventory"""
    client = args[0]
    world_object = args[1]
    character_object = args[2]
    current_location = args[3]
    if item_to_put_down_id is None:
        item_to_put_down = None
    else:
        item_to_put_down = world_object.items[item_to_put_down_id]
        character_object.remove_from_inventory(item_to_put_down_id, 1)
        current_location.add_item(item_to_put_down_id)
        world_object.add_key_event(f"Player's character, {character_object.name},"
            f"put down {item_to_put_down.name} at {current_location.name}")

def use_up_item_in_inventory(item_to_use_up_id: int, args: list) -> None:
    """An action to have the player put an item down and remove it from their inventory"""
    client = args[0]
    world_object = args[1]
    character_object = args[2]
    current_location = args[3]
    if item_to_use_up_id is None:
        item_to_use_up = None
    else:
        item_to_use_up = world_object.items[item_to_use_up_id]
        character_object.remove_from_inventory(item_to_use_up_id, 1)
        world_object.add_key_event(f"Player's character, {character_object.name},"
            f"used up {item_to_use_up.name} at {current_location.name}")

def talk_to_character(character_id: int, args: list) -> None:
    """This is an action that talks to a character"""
    client = args[0]
    world_object = args[1]
    character_object_player = args[2]
    # 0.4 chance that the npc will be dismissive and only offer one line of dialog and a 0.6 chance
    # that npc will be more talk active to the player object
    talk_chance = random.randint(1, 10)
    if talk_chance <= 6:
        # NPC is talkative and wants to talk to the player
        dialog_raw = None
        while not dialog_raw:
            try:
                dialog_raw = chat_with_gpt(client,
                                           dialog_system_message(),
                                           talkative_dialog_template(
                                               world_object.characters[character_id].name,
                                               world_object.characters[character_id].traits,
                                               character_object_player.name,
                                               world_object.theme),
                                           False,
                                           tokens=500,
                                           structure=TalkativeDialogStructure)
            except openai.LengthFinishReasonError:
                print("Token Count Error, Not provided enough tokens")

        dialog_text = dialog_mapper.talkative_dialog_mapper(dialog_raw)
        # End Conversation Trigger
        end_conversation = False
        count = 1
        # Print the initial conversation start
        print(dialog_text[0])
        # Print user response
        for i in range(1, len(dialog_text), 2):
            print(f"{count}. {dialog_text[i]}\n")
            count += 1
        print(f"{count}. End Conversation.\n")
        # Conversation loop
        while not end_conversation:
            user_input = input("> ")
            if not user_input.isdigit():
                print("Please enter a number")
                continue
            else:
                user_input = int(user_input)
            # User ends a conversation
            if user_input == count:
                end_conversation = True
            # Prints the option the user selected and the NPC response then loops back to the conversation
            elif count - 1 >= user_input > 0:
                # Print Player Response
                print(dialog_text[(user_input*2)-1], "\n")
                # Print NPC Response to the Player Response
                print(dialog_text[user_input*2], "\n")
                # Reprint the dialog options
                count = 1
                for i in range(1, len(dialog_text), 2):
                    print(f"{count}. {dialog_text[i]}\n")
                    count += 1
                print(f"{count}. End Conversation.\n")
            else:
                print("Invalid number")
    else:
        # NPC is not talkative on will only offer one dialog to the player
        dialog_raw = None
        while not dialog_raw:
            try:
                dialog_raw = chat_with_gpt(client,
                                           dialog_system_message(),
                                           dismissive_dialog_template(
                                               world_object.characters[character_id].name,
                                               world_object.characters[character_id].traits,
                                               character_object_player.name,
                                               world_object.theme),
                                           False,
                                           tokens=500,
                                           structure=DismissiveDialogStructure)
            except openai.LengthFinishReasonError:
                print("Token Count Error, Not provided enough tokens")

        # Map the Dialog
        dialog_text = dialog_mapper.dismissive_dialog_mapper(dialog_raw)
        # Add the conversation to the characters conversation history
        world_object.characters[character_id].add_to_conversation_history(dialog_text)
        print(dialog_text)


AVAILABLE_ACTIONS = ["move location", "interact with item", "pick up item", "put down item", "use up item in inventory",
                     "talk to character"]

ACTION_TO_VALUE_DICT = {
"move location": "new_location",
"interact with item": "item_to_interact",
"pick up item": "item_to_pick_up_id",
"put down item": "item_to_put_down_id",
"use up item in inventory": "item_to_use_up_id",
"talk to character": "character_to_talk_to_id"
}


ACTIONS_DICT = {
"new_location": move_character,
"item_to_interact": interact_with_item,
"item_to_pick_up_id":pick_up_item,
"item_to_put_down_id":put_down_item,
"item_to_use_up_id":use_up_item_in_inventory,
"character_to_talk_to_id":talk_to_character
}

def process_user_choice(actions: dict, args: list, action_performed: str) -> None:
    """Function to process the choices the user makes using our in-built action functions.
    It goes through the actions dictionary and, for each action present, calls its relevant function.

    ACTIONS_DICT is a dictionary in key:value pairs of function_name:actual_function such that
    when we call ACTIONS_DICT[function_name](), it's the equivalent of calling actual_function()

    Parameters:
        actions: A dictionary containing all of the actions taken 
            in this choice, initially given to us in JSON format via ChatGPT.
        args: A list of all arguments needed for any of the action functions. 
            Different functions may need different parameters, but we're iterating through ACTIONS_DICT without knowing
            which function we're using each time, so this way each function uses 
            only the indices of args that it needs and our code remains simple.
            Example:

            move(args: list)
                new_location_id = args[0]
                world = args[1]
                ...

            talk(args: list)
                character = args[2]
                ...

            ACTIONS_DICT[action]([new_location_id, world, character])"""

    if action_performed in AVAILABLE_ACTIONS:
        value_to_use = ACTION_TO_VALUE_DICT[action_performed]
        ACTIONS_DICT[value_to_use](actions[value_to_use], args)
    else:
        print("ACTION NOT FOUND")
        print(action_performed)

    # As far as I can tell our actions don;t actually say which action is being performed as it
    # lists all of them so this change gives back what type of action it is and removes the
    # inconsistency with an actions description and what actually executed
    #for action in actions.keys():
    #    if action in ACTIONS_DICT:
    #        ACTIONS_DICT[action](actions[action], args)
    #    else:
    #        print("ACTION NOT FOUND")
    #        print(action)
