class Location:
    """
    This class represents a location.
    """

    def __init__(self, ID: int, name: str, characters: list[int], items: list[int], description: str, neighbors: list[Location]):
        self._ID = ID
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

    def add_neighbor(self, neighbor: Location) -> None:
    	if neighbor not in self._neighbors:
    		self._neighbors.append(neighbor)

    def add_item(self, item_id: int) -> None:
        if item_id not in self._items:
            self._items.append(item_id)

    def add_character(self, character_id: int) -> None:
        if character_id not in self._characters:
            self._characters.append(character_id)

    # base functions
    def __str__(self) -> str:
        return f"Name: {self._name}\nDescription: {self._description}\nCharacters: {self._characters}"

    def __eq__(self, other) -> bool:
    	if isinstance(other, Location):
    		return self.ID == other.ID
    	else:
    		return False

    def __hash__(self) -> int:
        return hash(self.ID)

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
    def ID(self) -> int:
        return self._ID

    @property
    def name(self) -> str:
        return self._name
    @name.setter
    def name(self, name: str) -> None:
        self._name = name

    @property
    def characters(self) -> list[int]:
        return self._characters
    @characters.setter
    def characters(self, characters: list[int]) -> None:
        self._characters = characters

    @property
    def items(self) -> list[int]:
        return self._items
    @items.setter
    def items(self, items: list[int]) -> None:
        self._items = items

    @property
    def description(self) -> str:
        return self._description
    @description.setter
    def description(self, description: str) -> None:
        self._description = description

    @property
    def neighbors(self) -> list[Location]:
        return self._neighbors
    @neighbors.setter
    def neighbors(self, neighbors: list[Location]) -> None:
        self._neighbors = neighbors
    