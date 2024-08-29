"""Location class"""

class Location:
    """
    This class represents a location.
    """

    def __init__(
        self,
        id_: int,
        name: str,
        characters: list[int],
        items: list[int],
        description: str,
        neighbors: list['Location']
    ) -> None:
        """
        Initialises a Location instance.
            Parameters:
                id_ (int): unique object ID
                name (str): location name
                characters (list): list of IDs of characters at this location
                items (list): list of IDs of items at this location
                description (str): description of this location
                neighbors (list): list of Location objects this location connects to

        """
        self._id_ = id_
        self._name = name
        self._characters = characters
        self._items = items
        self._description = description
        self._neighbors = neighbors

    def populate(self, num_characters: int) -> None:
        """Send prompt to LLM such as 'This is x location in x story with 
        num_characters of characters. Generate xyz stats for each character.'
        Once characters generated, add them (or their id numbers) to self.characters
        list. If needed also do this with items"""
        pass

    def add_neighbor(self, neighbor: 'Location') -> None:
        """Adds a Location object to the list of neighbors this Location has"""
        if neighbor not in self.neighbors:
            self._neighbors.append(neighbor)

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

    # base functions
    def __str__(self) -> str:
        return f"Name: {self.name}\nDescription: {self.description}\nCharacters: {self.characters}"

    def __eq__(self, other) -> bool:
        if isinstance(other, Location):
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
    def neighbors(self) -> list['Location']:
        """Getter for neighbors attribute"""
        return self._neighbors
    @neighbors.setter
    def neighbors(self, neighbors: list['Location']) -> None:
        """Setter for neighbors attribute"""
        self._neighbors = neighbors
