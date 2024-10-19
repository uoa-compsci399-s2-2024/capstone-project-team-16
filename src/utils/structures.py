"""This file keeps BaseModel objects to pass to an LLM to force a specific output"""

from pydantic import BaseModel, model_validator
from typing import Union, Optional, Literal


# Scene Structure
class SceneStructure(BaseModel):
    """Structure for Scene Generation"""
    scene: str


# Choice Structure
class ActionStructure(BaseModel):
    """Structure for Action Generation"""
    new_location: Union[int, Literal["Unknown"], None]
    item_to_interact: Optional[int]
    item_to_pick_up_id: Optional[int]
    item_to_put_down_id: Optional[int]
    item_to_use_up_id: Optional[int]
    character_to_talk_to_id: Optional[int]

    @model_validator(mode='before')
    def one_valid_id(cls, values):
        """Validator Function to check at least one of the parameters has a value"""
        # Values is a dictionary of all the values present in the structures this is default
        # passed in Pydantic
        # This check checks at least one value in the structure is not None
        if not any(value is not None for value in values.values()):
            raise ValueError(f"There is no valid id present in the response. Dict of Stucture: {values}")
        return values


class ChoiceSingularStructure(BaseModel):
    """Structure for Choice Singular Generation"""
    description: str
    action_performed: str
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
