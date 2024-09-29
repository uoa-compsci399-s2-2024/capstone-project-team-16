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
    item_to_interact: int or None


class ChoiceSingularStructure(BaseModel):
    """Structure for Choice Singular Generation"""
    description: str
    actions: ActionStructure


class ChoicesStructure(BaseModel):
    """Structure for Choice Generation"""
    choices: list[ChoiceSingularStructure]

class ItemSingularStructure(BaseModel):
    """Structure for generating a single item"""
    name: str
    price: float
    weight: float
    category: str

class ItemsStructure(BaseModel):
    """Structure for multiple item generation"""
    items: list[ItemSingularStructure]

class CharacterSingularStructure(BaseModel):
    name: str
    traits: list[str]

class CharactersStructure(BaseModel):
    characters: list[CharacterSingularStructure]