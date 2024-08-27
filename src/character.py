# Character Class

class Character:
    def __init__(self, ID: int, name: str, playable: bool, , traits: list[str], current_location: int = None, inventory: dict = {}) -> None:
        self._ID = ID
        self._name = name # character's name
        self._traits = traits # traits the character has
        self._current_location = current_location # ID of current node
        self._inventory = inventory # dict item:quantity
        self._playable = playable # boolean

    
    def add_to_inventory(self, item_id: int, quantity: int = 1) -> None: # adds an item of specified quantity to inventory 
        if item_id in self.inventory:
            self.inventory[item_id] += quantity
        else:
            self.inventory[item_id] = quantity
    
    def remove_from_inventory(self, item_id: int, quantity: int) -> None: #removes an item of specified quantity from inventory
        if item_id in self.inventory.keys():
            if self.inventory[item_id] > quantity:
                self.inventory[item_id] -= quantity
            else:
                del self.inventory[item_id]

    def move(self, new_location: int) -> None:
        self.current_location = new_location

    # base functions
    def __str__(self) -> str:
        return f"Name: {self.name}\nCurrent Location: {self.currentLocation}\nInventory: {self.inventory}"

    def __repr__(self) -> str:
        return f"Name: {self.name}\nCurrent Location: {self.currentLocation}\nInventory: {self.inventory}"

    def __eq__(self, other) -> bool:
        if isinstance(other, Character):
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
    def playable(self) -> bool:
        return self._playable
    @playable.setter
    def playable(self, playable: bool) -> None:
        self._playable = playable

    @property
    def traits(self) -> list[str]:
        return self._traits
    @traits.setter
    def traits(self, traits: list[str]) -> None:
        self._traits = traits

    @property
    def current_location(self) -> int:
        return self._current_location
    @current_location.setter
    def name(self, current_location: int) -> None:
        self._current_location = current_location

    @property
    def inventory(self) -> dict:
        return self._inventory
    @inventory.setter
    def inventory(self, inventory: dict) -> None:
        self._inventory = inventory
