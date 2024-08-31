"""World class"""
from location import Location
from character import Character
from item import Item
from trope import Trope

class World:
    """A class for keeping track of all of the
    current game's objects and their instances."""
    def __init__(
        self,
        locations: dict = None,
        items: dict = None,
        characters: dict = None,
        tropes: dict = None,
        themes: list[str] = None
    ) -> None:
        """initialises a World instance"""
        self._locations = locations or {}
        self._items = items or {}
        self._characters = characters or {}
        self._tropes = tropes or {}
        self._themes = themes or []

    def add_location(self, location: Location) -> None:
        """adds a Location object to the world, setting
        its unique ID as its key in the dictionary"""
        self.locations[location.id_] = location

    def add_character(self, character: Character) -> None:
        """adds a Character object to the world, setting its
        unique ID as its key in the dictionary"""
        self.characters[character.id_] = character

    def add_item(self, item: Item) -> None:
        """adds an Item object to the world, setting its
        unique ID as its key in the dictionary"""
        self.items[item.id_] = item

    def add_trope(self, trope: Trope) -> None:
        """adds a Trope object to the world, setting its
        unique ID as its key in the dictionary"""
        self.tropes[trope.id_] = trope

    def add_theme(self, theme: str) -> None:
        """adds a theme to the world's themes"""
        self.themes.append(theme)

    def remove_location(self, location_id: int) -> None:
        """remove a Location object from the world's locations by its unique ID"""
        if location_id in self.locations.keys():
            del self.locations[location_id]

    def remove_character(self, character_id: int) -> None:
        """remove a Character object from the world's characters by its unique ID"""
        if character_id in self.characters.keys():
            del self.characters[character_id]

    def remove_item(self, item_id: int) -> None:
        """remove an Item object from the world's items by its unique ID"""

        if item_id in self.items.keys():
            del self.items[item_id]

    def remove_trope(self, trope_id: int) -> None:
        """remove a Trope object from the world's items by its unique ID"""
        if trope_id in self.tropes.keys():
            del self.tropes[trope_id]

    def remove_theme(self, theme: str) -> None:
        """remove a theme from the world's themes"""
        if theme in self.themes:
            self.themes.remove(theme)

    @property
    def locations(self) -> dict:
        """Getter for locations attribute"""
        return self._locations

    @property
    def characters(self) -> dict:
        """Getter for characters attribute"""
        return self._characters

    @property
    def items(self) -> dict:
        """Getter for items attribute"""
        return self._items

    @property
    def tropes(self) -> dict:
        """Getter for tropes attribute"""
        return self._tropes

    @property
    def themes(self) -> list[str]:
        """Getter for themes attribute"""
        return self._themes
