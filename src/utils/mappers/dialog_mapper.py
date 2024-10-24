"""
This is a json to text Mapper for dialog spoken by an NPC and has two forms they are both in here
cause it makes sense to have both mappers for the same thing in the file
"""

import json


def talkative_dialog_mapper(json_str: str) -> list:
    """Mapper that turns npc dialog json into a string
    Index 0 is for the initial dialog spoken with every odd index after that being a player choice
    and every even index being a npc response to the previous player choice
    """
    json_str = json_str.strip('```json').strip('```').strip()

    # NPC talking about what the want to talk about
    response_list = [json.loads(json_str)["dialog"]]

    # Dialog options the player has to pick + the responses from them
    response = json.loads(json_str)["responses"]
    for dialog in response:
        response_list.append(dialog["player_response"])
        response_list.append(dialog["npc_comment"])

    return response_list

def dismissive_dialog_mapper(json_str: str) -> str:
    """Mapper that turns npc dialog json into a string"""
    json_str = json_str.strip('```json').strip('```').strip()
    data = json.loads(json_str)["dialog"]

    return data
