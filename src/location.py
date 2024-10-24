"""Location class"""
import itertools
from typing import Self

import openai

from utils.prompt import chat_with_gpt
from utils.templates import character_template, item_template, character_system_message, item_system_message
from utils.mappers import character_mapper, item_mapper
from utils.structures import ItemsStructure, CharactersStructure



class Location:
    """
    This class represents a location.
    """
    id_iter = itertools.count()

    def __init__(
        self,
        name: str,
        description: str,
        new_id: int = None,
        characters: list[int] = None,
        items: list[int] = None,
        neighbors: list[Self] = None,
        coords: tuple[int, int] = None
    ) -> None:
        """
        Initialises a Location instance.
            Parameters:
                name (str): location name
                characters (list): list of IDs of characters at this location
                items (list): list of IDs of items at this location
                description (str): description of this location
                neighbors (list): list of Location objects this location connects to

        """
        self._id_ = next(Location.id_iter) if new_id is None else new_id
        self._name = name
        self._characters = characters or []
        self._items = items or []
        self._description = description
        self._neighbors = neighbors or []
        self._coords = coords

    def populate(self, num_characters: int, num_items: int, world, client) -> None:
        """Send prompt to LLM such as 'This is x location in x story with 
        num_characters of characters. Generate xyz stats for each character.'
        Once characters generated, add them (or their id numbers) to self.characters
        list. If needed also do this with items"""

        character_response = None
        tokens = 80
        while not character_response:
            try:
                character_response = chat_with_gpt(
                    client,
                    character_system_message(),
                    character_template(num_characters, "", world.tropes, world.theme),
                    False,
                    CharactersStructure,
                    tokens=tokens
                )
            except openai.LengthFinishReasonError:
                print("Token Count Error, Not provided enough tokens... increasing token count and retrying")
                tokens += 80

        item_response = None
        tokens = 80
        while not item_response:
            try:
                item_response = chat_with_gpt(
                    client,
                    item_system_message(),
                    item_template(num_items, world.tropes, world.theme),
                    False,
                    ItemsStructure,
                    tokens=tokens
                )
            except openai.LengthFinishReasonError:
                print("Token Count Error, Not provided enough tokens... increasing token count and retrying")
                tokens += 80

        characters = character_mapper.create_character_from_json(character_response)
        items = item_mapper.create_item_from_json(item_response)
        # Add Objects to internal lists
        for character in characters:
            self.add_character(character.id_)
            world.add_character(character)
        for item in items:
            self.add_item(item.id_)
            world.add_item(item)

    def add_neighbor(self, neighbor: Self) -> None:
        """Adds a Location object to the list of neighbors this Location has"""
        if neighbor not in self.neighbors:
            self._neighbors.append(neighbor)

    def remove_neighbor(self, neighbor: Self) -> None:
        """Removes a Location object from the list of neighbors this Location has"""
        if neighbor in self.neighbors:
            self._neighbors.remove(neighbor)

    def add_item(self, item_id: int) -> None:
        """Adds the ID of an item to the list of items at this location"""
        if item_id not in self.items:
            self._items.append(item_id)

    def add_character(self, character_id: int) -> None:
        """Adds the ID of a character to the list of characters at this location"""
        if character_id not in self.characters:
            self._characters.append(character_id)

    def remove_item(self, item_id: int) -> None:
        """Removes the ID of an item from the list of items at this location"""
        if item_id in self.items:
            self._items.remove(item_id)

    def remove_character(self, character_id: int) -> None:
        """Removes the ID of a character from the list of characters at this location"""
        if character_id in self.characters:
            self._characters.remove(character_id)

    @property
    def coords(self) -> tuple[int, int]:
        """Gets the coordinates of this location"""
        return self._coords
    @coords.setter
    def coords(self, coords: tuple[int, int]) -> None:
        """Sets the coordinates of this location"""
        self._coords = coords

    # base functions
    def __str__(self) -> str:
        return f"Name: {self.name}\nDescription: {self.description}\nCharacters: {self.characters}"

    def __repr__(self) -> str:
        return f"Name: {self.name}\nDescription: {self.description}\nCharacters: {self.characters}"

    def __eq__(self, other) -> bool:
        if isinstance(other, self.__class__):
            return self.id_ == other.id_
        return False

    def __hash__(self) -> int:
        return hash(self.id_)

    def __lt__(self, other) -> bool:
        return self.name < other.name

    def __le__(self, other) -> bool:
        return self.name <= other.name

    def __gt__(self, other) -> bool:
        return self.name > other.name

    def __ge__(self, other) -> bool:
        return self.name >= other.name

    # getters and setters

    @property
    def id_(self) -> int:
        """Getter for ID attribute"""
        return self._id_

    @property
    def name(self) -> str:
        """Getter for name attribute"""
        return self._name
    @name.setter
    def name(self, name: str) -> None:
        """Setter for name attribute"""
        self._name = name

    @property
    def characters(self) -> list[int]:
        """Getter for characters attribute"""
        return self._characters
    @characters.setter
    def characters(self, characters: list[int]) -> None:
        """Setter for characters attribute"""
        self._characters = characters

    @property
    def items(self) -> list[int]:
        """Getter for items attribute"""
        return self._items
    @items.setter
    def items(self, items: list[int]) -> None:
        """Setter for items attribute"""
        self._items = items

    @property
    def description(self) -> str:
        """Getter for description attribute"""
        return self._description
    @description.setter
    def description(self, description: str) -> None:
        """Setter for description attribute"""
        self._description = description

    @property
    def neighbors(self) -> list[Self]:
        """Getter for neighbors attribute"""
        return self._neighbors
    @neighbors.setter
    def neighbors(self, neighbors: list[Self]) -> None:
        """Setter for neighbors attribute"""
        self._neighbors = neighbors
