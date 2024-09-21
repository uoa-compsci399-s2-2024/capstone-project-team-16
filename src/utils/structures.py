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
