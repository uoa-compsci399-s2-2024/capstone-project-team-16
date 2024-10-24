"""
This is a mapper for scenes, it maps scene from a JSON string into a string
"""

import json


def create_scene_from_json(json_str: str) -> str:
    """
    Creates a string of a scene from a JSON string

    :param str json_str: A JSON string to be deserialized into a string of a scene
    :return: A string of a scene
    :rtype: str
    """
    json_str = json_str.strip('```json').strip('```').strip()
    data = json.loads(json_str)["scene"]

    return data


def create_json_from_scene(scene: str) -> str:
    """
    Creates a JSON string representing a scene

    :param str scene: A scene to be serialized into a JSON string
    :return: A JSON string representing the scene
    :rtype: str
    """
    return json.dumps({
        "scene": scene
    })