"""Character Class"""

class Character:
    """A class defining a character object in an interactive story."""
    def __init__(
        self,
        id_: int,
        name: str,
        playable: bool,
        traits: list[str],
        current_location: int = None,
        inventory: dict = None
    ) -> None:
        """
        Initialises a Character instance.

            Parameters:
                id_ (int): unique object ID
                name (str): character's name
                traits (list): traits the character has
                current_location (int): ID of the current node
                inventory (dict): dictionary of format item:quantity
                playable (boolean): whether the character is playable
        """

        self._id_ = id_
        self._name = name
        self._traits = traits
        self._current_location = current_location
        if inventory is None:
            self._inventory = {}
        else:
            self._inventory = inventory
        self._playable = playable

    def add_to_inventory(
        self,
        item_id: int,
        quantity: int = 1
    ) -> None:
        """Adds an item of specified quantity to inventory"""

        if item_id in self.inventory:
            self.inventory[item_id] += quantity
        else:
            self.inventory[item_id] = quantity

    def remove_from_inventory(
        self,
        item_id: int,
        quantity: int
    ) -> None:
        """Removes an item of specified quantity from inventory"""

        if item_id in self.inventory.keys():
            if self.inventory[item_id] > quantity:
                self.inventory[item_id] -= quantity
            else:
                del self.inventory[item_id]

    def move(self, new_location: int) -> None:
        """Moves character to new location."""

        self.current_location = new_location

    # base functions
    def __str__(self) -> str:
        return f"Name: {self.name}\nCurrent Location: {self.current_location}\nInventory: {self.inventory}"

    def __repr__(self) -> str:
        return f"Name: {self.name}\nCurrent Location: {self.current_location}\nInventory: {self.inventory}"

    def __eq__(self, other) -> bool:
        if isinstance(other, Character):
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
    def playable(self) -> bool:
        """Getter for playable attribute"""
        return self._playable
    @playable.setter
    def playable(self, playable: bool) -> None:
        """Setter for playable attribute"""
        self._playable = playable

    @property
    def traits(self) -> list[str]:
        """Getter for traits attribute"""
        return self._traits
    @traits.setter
    def traits(self, traits: list[str]) -> None:
        """Setter for traits attribute"""
        self._traits = traits

    @property
    def current_location(self) -> int:
        """Getter for current location attribute"""
        return self._current_location
    @current_location.setter
    def current_location(self, current_location: int) -> None:
        """Setter for current location attribute"""
        self._current_location = current_location

    @property
    def inventory(self) -> dict:
        """Getter for inventory attribute"""
        return self._inventory
    @inventory.setter
    def inventory(self, inventory: dict) -> None:
        """Setter for inventory attribute"""
        self._inventory = inventory
