import os
from openai import OpenAI
from dotenv import load_dotenv
import pytest
from src.utils import prompt, templates, mappers
from src.location import Location

@pytest.fixture
def client():
    load_dotenv()
    openai_api_key = os.getenv('OPENAI_API_KEY')

    # initialise client
    client = OpenAI(api_key=openai_api_key)
    return client


@pytest.fixture
def tropes():
    return ["The Chosen One"]


@pytest.fixture
def theme():
    return "Fantasy"


def test_location_generation_init(client, tropes, theme):
    locations = prompt.chat_with_gpt(
        client,
        "You are a knowledgeable chatbot that creates unique locations",
        templates.initial_location_template(6, tropes, theme),
        False,
        tokens=500,
        temp=2
    )

    mapped_locations = mappers.create_location_from_json(json_str=locations)

    # Tests

    assert isinstance(locations, str)
    assert isinstance(mapped_locations, list)
    assert len(mapped_locations) == 6

    for location in mapped_locations:
        assert isinstance(location, Location)
