import json
import pytest
import src.utils.mappers.location_mapper

@pytest.fixture()
def jsonstr():
    with open("location_jsons/initial_location.json") as json_file:
        initial_locations = json.load(json_file)
    json_file.close()

