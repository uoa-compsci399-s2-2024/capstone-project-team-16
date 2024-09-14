"""
This is a json to string Mapper for scene creating a string to display to the user
"""

import json


def create_scene_from_json(json_str: str) -> str:
    """"""
    json_str = json_str.strip('```json').strip('```').strip()
    data = json.loads(json_str)["scene"]

    return data
