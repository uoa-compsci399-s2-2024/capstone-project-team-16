"""Location class"""
import itertools
from typing import Self


class Location:
    """
    A class defining a location object in an interactive story.
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

        :param str name: The name of the Location
        :param str description: The description of the Location
        :param int new_id: The new id of the Location
        :param list[int] characters: A list of characters in the Location
        :param list[int] items: A list of items in the Location
        :param list[int] neighbors: A list of neighboring Locations of this Location
        :param list[int] coords: The coordinates of the Location
        :rtype: None
        """
        self._id_ = next(Location.id_iter) if new_id is None else new_id
        self._name = name
        self._characters = characters or []
        self._items = items or []
        self._description = description
        self._neighbors = neighbors or []
        self._coords = coords

    def add_neighbor(self, neighbor: Self) -> None:
        """
        Adds a Location object to the list of neighbors this Location has

        :param Location neighbor: A neighbour of this Location to be added
        :rtype: None
        """
        if neighbor not in self.neighbors:
            self._neighbors.append(neighbor)

    def remove_neighbor(self, neighbor: Self) -> None:
        """
        Removes a Location object from the list of neighbors this Location has

        :param Location neighbor: A neighbour of this Location to be removed
        :rtype: None
        """
        if neighbor in self.neighbors:
            self._neighbors.remove(neighbor)

    def add_item(self, item_id: int) -> None:
        """
        Adds the ID of an item to the list of items at this location

        :param int item_id: The ID of an Item to be added to the Location
        :rtype: None
        """
        if item_id not in self.items:
            self._items.append(item_id)

    def remove_item(self, item_id: int) -> None:
        """
        Removes the ID of an item from the list of items at this location

        :param int item_id: The ID of an Item to be removed from the Location
        :rtype: None
        """
        if item_id in self.items:
            self._items.remove(item_id)

    def add_character(self, character_id: int) -> None:
        """
        Adds the ID of a character to the list of characters at this location

        :param int character_id: The ID of a Character to be added to the Location
        :rtype: None
        """
        if character_id not in self.characters:
            self._characters.append(character_id)

    def remove_character(self, character_id: int) -> None:
        """
        Removes the ID of a character from the list of items at this location

        :param int character_id: The ID of a Character to be removed from the Location
        :rtype: None
        """
        if character_id in self.characters:
            self._characters.remove(character_id)

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

    @property
    def id_(self) -> int:
        """
        Getter for ID attribute

        :return: The ID of an Item
        :rtype: int
        """
        return self._id_

    @property
    def name(self) -> str:
        """
        Getter for name attribute

        :return: The name of a Location
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        """
        Setter for name attribute

        :param str name: The name of a Location
        :rtype: None
        """
        self._name = name

    @property
    def characters(self) -> list[int]:
        """
        Getter for characters attribute

        :return: A list of IDs of characters at a Location
        :rtype: list[int]
        """
        return self._characters

    @characters.setter
    def characters(self, characters: list[int]) -> None:
        """
        Setter for name attribute

        :param list[int] characters: A list of character IDs for a Location
        :rtype: None
        """
        self._characters = characters

    @property
    def items(self) -> list[int]:
        """
        Getter for items attribute

        :return: A list of IDs of items at a Location
        :rtype: list[int]
        """
        return self._items

    @items.setter
    def items(self, items: list[int]) -> None:
        """
        Setter for items attribute

        :param list[int] items: A list of character IDs for a Location
        :rtype: None
        """
        self._items = items

    @property
    def description(self) -> str:
        """
        Getter for description attribute

        :return: The description of a Location
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str) -> None:
        """
        Setter for description attribute

        :param str description: A description of a Location
        :rtype: None
        """
        self._description = description

    @property
    def neighbors(self) -> list[Self]:
        """
        Getter for neighbours attribute

        :return: The list of neighbouring locations of a Location
        :rtype: list[Location]
        """
        return self._neighbors

    @neighbors.setter
    def neighbors(self, neighbors: list[Self]) -> None:
        """
        Setter for neighbours attribute

        :param list[Location] neighbors: A list of neighbouring locations of a Location
        :rtype: None
        """
        self._neighbors = neighbors

    @property
    def coords(self) -> tuple[int, int]:
        """
        Getter for coords attribute

        :return: The co-ordinates of a Location
        :rtype: str
        """
        return self._coords

    @coords.setter
    def coords(self, coords: tuple[int, int]) -> None:
        """
        Setter for co-ordinates attribute

        :param tuple[int, int] coords: The co-ordinates of a Location
        :rtype: None
        """
        self._coords = coords
