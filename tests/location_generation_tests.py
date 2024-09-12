import os
from openai import OpenAI
from dotenv import load_dotenv
import pytest
from src.utils import prompt, templates
from src.utils.mappers import location_mapper
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
        templates.initial_location_template(5, tropes, theme),
        False,
        tokens=500,
        temp=2
    )

    print(locations)

    mapped_locations = location_mapper.create_location_from_json(json_str=locations)

    print(mapped_locations)

    for location in mapped_locations:
        print(location)
    # Tests

    assert isinstance(locations, str)
    assert isinstance(mapped_locations, list)
    assert len(mapped_locations) == 5
    for location in mapped_locations:
        assert isinstance(location, Location)
