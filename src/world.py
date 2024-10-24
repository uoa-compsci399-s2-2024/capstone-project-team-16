"""World class"""
from location import Location
from character import Character
from item import Item
from trope import Trope


class World:
    """
    A class defining a world object in an interactive story.
    Keeps track of all the current game's objects and their instances.
    """
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
        """
        Initialises an Item instance.

        :param dict[Location} locations: A dictionary of locations in the World
        :param dict[Item] items: A dictionary of items in the World
        :param dict[Character] characters: A dictionary of characters in the World
        :param list[Trope] tropes: A dictionary of tropes in the World
        :param list[str] theme: A list of themes in the World
        :param list[str] choices: A list of choices in the World
        :param list[str] key_events: A list of key events that have occurred in the World
        :param int curr_story_beat: The current story beat time of the World
        :rtype: None
        """
        self._locations = locations or {}
        self._items = items or {}
        self._characters = characters or {}
        self._tropes = tropes or {}
        self._theme = theme or []
        self._choices = choices or []
        self._key_events = key_events or []
        self._curr_story_beat = curr_story_beat or 0

        # A list of JSON objects to pass to our choices template for better choice generation
        self._json_locations = []
        self._json_items = []
        self._json_characters = []

    def add_location(self, location: Location) -> None:
        """
        Adds a Location object to the world, setting its unique ID as its key in the dictionary

        :param Location location: A Location object to be added to the World
        :rtype: None
        """
        self._locations[location.id_] = location

    def add_json_location(self, json_str: str) -> None:
        """
        Adds a JSON object to the json_locations list

        :param str json_str: A json_str of a Location to be added to the World
        :rtype: None
        """
        self._json_locations.append(json_str)

    def add_character(self, character: Character) -> None:
        """
        Adds a Character object to the world, setting its unique ID as its key in the dictionary

        :param Character character: A Character object to be added to the World
        :rtype: None
        """
        self._characters[character.id_] = character

    def add_json_character(self, json_str: str) -> None:
        """
        Adds a JSON object to the json_characters list

        :param str json_str: A json_str of a Character to be added to the World
        :rtype: None
        """
        self._json_characters.append(json_str)

    def add_item(self, item: Item) -> None:
        """
        Adds an Item object to the world, setting its unique ID as its key in the dictionary

        :param Item item: An Item object to be added to the World
        :rtype: None
        """
        self._items[item.id_] = item

    def add_json_item(self, json_str: str) -> None:
        """
        Adds a JSON object to the json_items list

        :param str json_str: A json_str of an Item to be added to the World
        :rtype: None
        """
        self._json_items.append(json_str)

    def add_trope(self, trope: Trope) -> None:
        """
        Adds a Trope object to the world, setting its unique ID as its key in the dictionary

        :param Trope trope: A Trope object to be added to the World
        :rtype: None
        """
        self._tropes[trope.id_] = trope

    def add_theme(self, theme: str) -> None:
        """
        Adds a theme to the world's themes

        :param str theme: A theme to be added to the World
        :rtype: None
        """
        self._theme.append(theme)

    def add_key_event(self, event: str) -> None:
        """
        Adds a key event to the key events that have happened in the story so far

        :param str event: A key event to be added to the World
        :rtype: None
        """
        self._key_events.append(event)

    def remove_location(self, location_id: int) -> None:
        """
        Remove a Location object from the world's locations by its unique ID

        :param int location_id: The ID of a Location object to be removed from the World
        :rtype: None
        """
        if location_id in self._locations.keys():
            del self._locations[location_id]

    def remove_character(self, character_id: int) -> None:
        """
        Remove a Character object from the world's characters by its unique ID

        :param int character_id: The ID of a Character object to be removed from the World
        :rtype: None
        """
        if character_id in self.characters.keys():
            del self._characters[character_id]

    def remove_item(self, item_id: int) -> None:
        """
        Remove an Item object from the world's items by its unique ID

        :param int item_id: The ID of an Item object to be removed from the World
        :rtype: None
        """

        if item_id in self.items.keys():
            del self._items[item_id]

    def remove_trope(self, trope_id: int) -> None:
        """
        Remove a Trope object from the world's items by its unique ID

        :param int trope_id: The ID of a Trope object to be removed from the World
        :rtype: None
        """
        if trope_id in self.tropes.keys():
            del self._tropes[trope_id]

    def remove_theme(self, theme: str) -> None:
        """
        Remove a theme from the world's themes

        :param str theme: The theme to be removed from the World
        :rtype: None
        """
        if theme in self._theme:
            self._theme.remove(theme)

    def remove_key_event(self, event: str) -> None:
        """
        Remove a key event from the world's key events

        :param str event: The key event to be removed from the World
        :rtype: None
        """
        if event in self._key_events:
            self._key_events.remove(event)

    def delete_choices(self) -> None:
        """
        Resets the choices list to an empty list, so we can repopulate it at the next set of choices

        :rtype: None
        """
        self._choices = []

    @property
    def locations(self) -> dict[int, Location]:
        """
        Getter for locations attribute

        :return: The locations of a World
        :rtype: dict[int, Location]
        """
        return self._locations

    @property
    def json_locations(self) -> list[str]:
        """
        Getter for json_locations attribute

        :return: The JSONs of locations of a World
        :rtype: list[str]
        """
        return self._json_locations

    @property
    def characters(self) -> dict[int, Character]:
        """
        Getter for characters attribute

        :return: The characters of a World
        :rtype: dict[int, Character]
        """
        return self._characters

    @property
    def json_characters(self) -> list[str]:
        """
        Getter for json_characters attribute

        :return: The JSONs of characters of a World
        :rtype: list[str]
        """
        return self._json_characters

    @property
    def items(self) -> dict[int, Item]:
        """
        Getter for items attribute

        :return: The items of a World
        :rtype: dict[int, Item]
        """
        return self._items

    @property
    def json_items(self) -> list[str]:
        """
        Getter for json_items attribute

        :return: The JSONs of items of a World
        :rtype: list[str]
        """
        return self._json_items

    @property
    def tropes(self) -> dict[int, Trope]:
        """
        Getter for tropes attribute

        :return: The tropes of a World
        :rtype: dict[int, Trope]
        """
        return self._tropes

    @property
    def theme(self) -> list[str]:
        """
        Getter for theme attribute

        :return: The themes of a World
        :rtype: list[str]
        """
        return self._theme

    @property
    def choices(self) -> list[str]:
        """
        Getter for choices attribute

        :return: The choices of a World
        :rtype: list[str]
        """
        return self._choices

    @choices.setter
    def choices(self, choices: list[str]) -> None:
        """
        Setter for choices attribute

        :param list[str] choices: The new choices of a World
        :rtype: None
        """
        self._choices = choices

    @property
    def key_events(self) -> list[str]:
        """
        Getter for key events attribute

        :return: The key events of a World
        :rtype: list[str]
        """
        return self._key_events

    @property
    def curr_story_beat(self) -> int:
        """
        Getter for current story beat attribute

        :return: The current story beat of a World
        :rtype: int
        """
        return self._curr_story_beat

    @curr_story_beat.setter
    def curr_story_beat(self, story_beat: int) -> None:
        """
        Setter for current story beat attribute

        :param int story_beat: The new story beat of a World
        :rtype: None
        """
        self._curr_story_beat = story_beat
