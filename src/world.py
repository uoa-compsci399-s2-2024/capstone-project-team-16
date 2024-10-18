"""World class"""
from location import Location
from character import Character
from item import Item
from trope import Trope


class World:
    """A class for keeping track of all the
    current game's objects and their instances."""
    def __init__(
        self,
        locations: dict = None,
        items: dict = None,
        characters: dict = None,
        tropes: dict = None,
        theme: list[str] = None,
        choices: list[str] = None,
        key_events: list[str] = None,
        curr_story_beat: int = 0,
    ) -> None:
        """initialises a World instance"""
        self._locations = locations or {}
        self._items = items or {}
        self._characters = characters or {}
        self._tropes = tropes or {}
        self._theme = theme or []
        self._choices = choices or []
        self._key_events = key_events or []
        self._curr_story_beat = curr_story_beat or None

        """A list of JSON objects to pass to our 
        choices template for better choice generation"""
        self._json_locations = []
        self._json_items = []
        self._json_characters =[]

    def add_location(self, location: Location) -> None:
        """adds a Location object to the world, setting
        its unique ID as its key in the dictionary"""
        self._locations[location.id_] = location

    def add_json_location(self, json_str: str) -> None:
        """adds a JSON object to the json_locations list"""
        self._json_locations.append(json_str)

    def add_character(self, character: Character) -> None:
        """adds a Character object to the world, setting its
        unique ID as its key in the dictionary"""
        self._characters[character.id_] = character

    def add_json_character(self, json_str: str) -> None:
        """adds a JSON object to the json_characters list"""
        self._json_characters.append(json_str)

    def add_item(self, item: Item) -> None:
        """adds an Item object to the world, setting its
        unique ID as its key in the dictionary"""
        self._items[item.id_] = item

    def add_json_item(self, json_str: str) -> None:
        """adds a JSON object to the json_items list"""
        self._json_items.append(json_str)

    def add_trope(self, trope: Trope) -> None:
        """adds a Trope object to the world, setting its
        unique ID as its key in the dictionary"""
        self._tropes[trope.id_] = trope

    def add_theme(self, theme: str) -> None:
        """adds a theme to the world's themes"""
        self._theme.append(theme)

    def add_key_event(self, event: str) -> None:
        """adds a key event to the key events that have happened in the story so far"""
        self._key_events.append(event)

    def remove_location(self, location_id: int) -> None:
        """remove a Location object from the world's locations by its unique ID"""
        if location_id in self._locations.keys():
            del self._locations[location_id]

    def remove_character(self, character_id: int) -> None:
        """remove a Character object from the world's characters by its unique ID"""
        if character_id in self.characters.keys():
            del self._characters[character_id]

    def remove_item(self, item_id: int) -> None:
        """remove an Item object from the world's items by its unique ID"""

        if item_id in self.items.keys():
            del self._items[item_id]

    def remove_trope(self, trope_id: int) -> None:
        """remove a Trope object from the world's items by its unique ID"""
        if trope_id in self.tropes.keys():
            del self._tropes[trope_id]

    def remove_theme(self, theme: str) -> None:
        """remove a theme from the world's themes"""
        if theme in self._theme:
            self._theme.remove(theme)

    def remove_key_events(self, event: str) -> None:
        """remove a key event from the world's key events"""
        if event in self._key_events:
            self._key_events.remove(event)

    def set_choices(self, choices: list) -> None:
        """set the choices list which represents the
        current choices the player is presented with"""
        self._choices = choices

    def delete_choices(self) -> None:
        """resets the choices list to an empty list, so
        we can repopulate it at the next set of choices"""
        self._choices = []

    def set_curr_story_beat(self, story_beat: int) -> None:
        self._curr_story_beat = story_beat

    @property
    def locations(self) -> dict:
        """Getter for locations attribute"""
        return self._locations

    @property
    def json_locations(self) -> list:
        """Getter for json_locations attribute"""
        return self._json_locations

    @property
    def characters(self) -> dict:
        """Getter for characters attribute"""
        return self._characters

    @property
    def json_characters(self) -> list:
        """Getter for json_characters attribute"""
        return self._json_characters

    @property
    def items(self) -> dict:
        """Getter for items attribute"""
        return self._items

    @property
    def json_items(self) -> list:
        """Getter for json_items attribute"""
        return self._json_items

    @property
    def tropes(self) -> dict:
        """Getter for tropes attribute"""
        return self._tropes

    @property
    def theme(self) -> list:
        """Getter for theme attribute"""
        return self._theme

    @property
    def choices(self) -> list[str]:
        """Getter for choices attribute"""
        return self._choices

    @property
    def key_events(self) -> list[str]:
        """Getter for key events attribute"""
        return self._key_events

    @property
    def curr_story_beat(self) -> int:
        """Getter for current story beat attribute"""
        return self._curr_story_beat
