"""
This file keeps BaseModel objects to pass to an LLM to force a specific output
"""

from pydantic import BaseModel, model_validator
from typing import Union, Optional, Literal, List


# Scene Structure
class SceneStructure(BaseModel):
    """
    Structure for Scene Generation
    """
    scene: str


# Choice Structure
class ActionStructure(BaseModel):
    """
    Structure for Action Generation
    """
    new_location: Union[int, Literal["Unknown"], None]
    item_to_interact: Optional[int]
    item_to_pick_up_id: Optional[int]
    item_to_put_down_id: Optional[int]
    item_to_use_up_id: Optional[int]
    character_to_talk_to_id: Optional[int]

    @model_validator(mode='before')
    def one_valid_id(cls, values: dict) -> dict:
        """
        Validator Function to check at least one of the parameters has a value

        :param values: A dictionary of all the values present in the structure, this is default
        :raise ValueError: If all the values in the structure are None
        :return: A dictionary of all the values present in the structure, this is default
        """
        # Passed in Pydantic
        # This check checks at least one value in the structure is not None
        if not any(value is not None for value in values.values()):
            raise ValueError(f"There is no valid id present in the response")
        return values


class ChoiceSingularStructure(BaseModel):
    """Structure for generating a single choice"""
    description: str
    actions_performed: List[Literal["move location", "interact with item", "pick up item", "put down item",
                                    "use up item in inventory", "talk to character"]]
    actions: ActionStructure


class ChoicesStructure(BaseModel):
    """Structure for multiple choice generation"""
    choices: list[ChoiceSingularStructure]


class ItemSingularStructure(BaseModel):
    """Structure for generating a single Item"""
    name: str
    price: float
    weight: float
    category: str


class CharacterSingularStructure(BaseModel):
    """Structure for generating a single Character"""
    name: str
    traits: list[str]


# Location Structures
class LocationStructure(BaseModel):
    """Structure for Location generation"""
    name: str
    description: str
    items: list[ItemSingularStructure]
    characters: list[CharacterSingularStructure]


class SectionStructure(BaseModel):
    """Structure for section Location generation"""
    locations: list[LocationStructure]


class DismissiveDialogStructure(BaseModel):
    """Structure for dismissive dialog from an NPC"""
    dialog: str


class DialogResponseStructure(BaseModel):
    """Structure for dialog responses for a talkative NPC"""
    player_response: str
    npc_comment: str


class TalkativeDialogStructure(BaseModel):
    """Structure for talkative dialog from an NPC"""
    dialog: str
    responses: list[DialogResponseStructure]
