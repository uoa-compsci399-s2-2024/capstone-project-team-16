"""This file keeps BaseModel objects to pass to an LLM to force a specific output"""

from pydantic import BaseModel


# Location Strucuters
class LocationStructure(BaseModel):
    """Structure for Location Generation"""
    name: str
    description: str


class SectionStructure(BaseModel):
    """Structure for Section Location Generation"""
    locations: list[LocationStructure]


# Scene Structure
class SceneStructure(BaseModel):
    """Structure for Scene Generation"""
    scene: str


# Choice Structure
class ActionStructure(BaseModel):
    """Structure for Action Generation"""
    new_location: int or None
    character_id: int or None


class ChoiceSingularStructure(BaseModel):
    """Structure for Choice Singular Generation"""
    description: str
    actions: ActionStructure


class ChoicesStructure(BaseModel):
    """Structure for Choice Generation"""
    choices: list[ChoiceSingularStructure]
