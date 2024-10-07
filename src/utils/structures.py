"""This file keeps BaseModel objects to pass to an LLM to force a specific output"""

from pydantic import BaseModel


# Scene Structure
class SceneStructure(BaseModel):
    """Structure for Scene Generation"""
    scene: str


# Choice Structure
class ActionStructure(BaseModel):
    """Structure for Action Generation"""
    new_location: int or "unknown" or None
    item_to_interact: int or None
    item_to_pick_up_id: int or None
    item_to_put_down_id: int or None
    item_to_use_up_id: int or None
    character_id: int or None


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

# Location Structures
class LocationStructure(BaseModel):
    """Structure for Location Generation"""
    name: str
    description: str
    items: list[ItemSingularStructure]
    characters: list[CharacterSingularStructure]

class SectionStructure(BaseModel):
    """Structure for Section Location Generation"""
    locations: list[LocationStructure]


class DismissiveDialogStructure(BaseModel):
    """Structure for Dismissive Dialog from an NPC"""
    dialog: str


class DialogResponseStructure(BaseModel):
    """Structure for Dialog Responses for a talkative NPC"""
    player_response: str
    npc_comment: str


class TalkativeDialogStructure(BaseModel):
    """Structure for Talkative Dialog from an NPC"""
    dialog: str
    responses: list[DialogResponseStructure]
