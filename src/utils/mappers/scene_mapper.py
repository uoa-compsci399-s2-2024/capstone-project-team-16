"""
This is a json to string Mapper for scene creating a string to display to the user
"""

import json


def create_scene_from_json(json_str: str) -> str:
    """"""
    json_str = json_str.strip('```json').strip('```').strip()
    data = json.loads(json_str)["scene"]

    return data

def create_json_from_scene(scene: str) -> str:
    """
    Takes a scene as input, serializes it, and
    converts it into a JSON string.

    Parameters:
        scene (str): The scene to be serialized into a JSON string.

    Returns:
        str: A JSON string representing the scene.
    """
    return json.dumps({
        "scene": scene
    })