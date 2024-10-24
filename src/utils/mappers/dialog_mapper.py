"""
This is a mapper for NPC dialog, it maps talkative and dismissive dialog from a JSON string into a string
"""

import json


def talkative_dialog_mapper(json_str: str) -> list[str]:
    """
    Creates a list of strings of talkative dialog from a JSON string

    :param str json_str: A JSON string to be deserialized into string of talkative dialog
    :return: A list of strings of talkative dialog
    :rtype: list[str]
    """
    json_str = json_str.strip('```json').strip('```').strip()
    response_list = [json.loads(json_str)["dialog"]]

    response = json.loads(json_str)["responses"]
    for dialog in response:
        response_list.append(dialog["player_response"])
        response_list.append(dialog["npc_comment"])

    return response_list


def dismissive_dialog_mapper(json_str: str) -> str:
    """
        Creates a string of dismissive dialog from a JSON string

        :param str json_str: A JSON string to be deserialized into string of dismissive dialog
        :return: A string of dismissive dialog
        :rtype: str
        """
    json_str = json_str.strip('```json').strip('```').strip()
    data = json.loads(json_str)["dialog"]

    return data
