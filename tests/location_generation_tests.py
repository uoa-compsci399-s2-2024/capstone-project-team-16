import os
from openai import OpenAI
from dotenv import load_dotenv
import pytest

import sys

sys.path.append(os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'src')))

from utils import prompt, templates, structures
from world import World


@pytest.fixture
def client():
    load_dotenv()
    openai_api_key = os.getenv('OPENAI_API_KEY')

    # initialise client
    client = OpenAI(api_key=openai_api_key)
    return client


@pytest.fixture
def world():
    world = World()
    return world


@pytest.fixture
def tropes():
    return ["The Chosen One"]


@pytest.fixture
def theme():
    return "Fantasy"


def test_location_generation_init(client, tropes, theme, world):
    """These tests check that the structured output is followed"""
    locations = prompt.chat_with_gpt(
        client,
        templates.location_system_message(),
        templates.location_template(5, tropes, theme, 1, 1),
        False,
        tokens=700,
        temp=1,
        structure=structures.SectionStructure
    )

    # asserts that the keys exist in the json
    assert '"name":' in locations
    assert '"description":' in locations
    assert '"items":' in locations
    assert '"characters":' in locations
