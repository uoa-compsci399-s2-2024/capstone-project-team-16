"""Character Class"""

import itertools


class Character:
    """
    A class defining a character object in an interactive story.
    """

    id_iter = itertools.count()

    def __init__(
        self,
        name: str,
        traits: list[str],
        playable: bool = False,
        current_location: int = None,
        inventory: dict = None,
        id_: int = None,
        conversation_history: list = None
    ) -> None:
        """
        Initialises a Character instance.

        :param str name: A Character's name
        :param list[str] traits: A list of a Character's traits
        :param bool playable: Whether the Character is playable
        :param int current_location: ID of the current Location of the Character
        :param dict inventory: A dictionary of IDs and quantities of Items in the Character's inventory
        :param int id_: The ID of the Character
        :param list conversation_history: A list of conversations the character has had
        :rtype: None
        """

        self._id_ = next(Character.id_iter) if id_ is None else id_
        self._name = name
        self._traits = traits
        self._current_location = current_location
        if inventory is None:
            self._inventory = {}
        else:
            self._inventory = inventory
        self._playable = playable
        self._conversation_history = [] if conversation_history is None else conversation_history

    def add_to_inventory(self, item_id: int, quantity: int = 1) -> None:
        """
        A function to add an Item of specified quantity to a Character's inventory

        :param int item_id: The ID of the Item to be added to the Character's inventory
        :param int quantity: The quantity of the Item to be added to the Character's inventory
        :rtype: None
        """
        if item_id in self.inventory:
            self.inventory[item_id] += quantity
        else:
            self.inventory[item_id] = quantity

    def remove_from_inventory(self, item_id: int, quantity: int) -> None:
        """
        A function to remove an Item of specified quantity from a Character's inventory

        :param int item_id: The ID of the Item to be removed from the Character's inventory
        :param int quantity: The quantity of the Item to be removed from the Character's inventory
        :rtype: None
        """
        if item_id in self.inventory.keys():
            if self.inventory[item_id] > quantity:
                self.inventory[item_id] -= quantity
            else:
                del self.inventory[item_id]

    def move(self, new_location: int) -> None:
        """
        A function to move a Character to a new Location

        :param int new_location: The ID of the new Location the Character is moving to
        :rtype: None
        """
        self.current_location = new_location

    def add_to_conversation_history(self, conversation: list) -> None:
        """
        A function to add a conversation to the Character's conversation history

        :param list conversation: A list of messages from a conversation between two Characters
        :rtype: None
        """
        self._conversation_history.append(conversation)

    def __str__(self) -> str:
        return f"Name: {self.name}\nCurrent Location: {self.current_location}\nTraits: {self.traits}"

    def __repr__(self) -> str:
        return f"Name: {self.name}\nCurrent Location: {self.current_location}\nTraits: {self.traits}"

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

        :return: The ID of a Character
        :rtype: int
        """
        return self._id_

    @property
    def name(self) -> str:
        """
        Getter for name attribute

        :return: The name of a Character
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        """
        Setter for name attribute

        :param str name: The name of a Character
        :rtype: None
        """
        self._name = name

    @property
    def playable(self) -> bool:
        """
        Getter for playable attribute

        :return: The playable status of a Character
        :rtype: bool
        """
        return self._playable

    @playable.setter
    def playable(self, playable: bool) -> None:
        """
        Setter for playable attribute

        :param bool playable: The playable status of a Character
        :rtype: None
        """
        self._playable = playable

    @property
    def traits(self) -> list[str]:
        """
        Getter for traits attribute

        :return: A list of traits a Character has
        :rtype: list[str]
        """
        return self._traits

    @traits.setter
    def traits(self, traits: list[str]) -> None:
        """
        Setter for traits attribute

        :param list[str] traits: A list of traits a Character has
        :rtype: None
        """
        self._traits = traits

    @property
    def current_location(self) -> int:
        """
        Getter for current Location attribute

        :return: The ID of the current Location of a Character
        :rtype: int
        """
        return self._current_location

    @current_location.setter
    def current_location(self, current_location: int) -> None:
        """
        Setter for current Location attribute

        :param int current_location: The ID of the current Location of a Character
        :rtype: None
        """
        self._current_location = current_location

    @property
    def inventory(self) -> dict:
        """
        Getter for inventory attribute

        :return: A dictionary of IDs and quantities of Items in the Character's inventory
        :rtype: dict
        """
        return self._inventory

    @inventory.setter
    def inventory(self, inventory: dict) -> None:
        """
        Setter for inventory attribute

        :param dict inventory: A dictionary of IDs and quantities of Items in the Character's inventory
        :rtype: None
        """
        self._inventory = inventory

    @property
    def conversation_history(self) -> list:
        """
        Getter for conversation history attribute

        :return: A list of the messages of every conversation the Character has participated in
        :rtype: list
        """
        return self._conversation_history

    @conversation_history.setter
    def conversation_history(self, conversation_history: list) -> None:
        """
        Getter for conversation history attribute

        :param list conversation_history: A list of the messages of every conversation the Character has participated in
        :rtype: None
        """
        self._conversation_history = conversation_history
