# Character Class

class Character:
    def __init__(self, ID: int, name: str, playable: bool, , traits: list[str], currentLocation: str = None, inventory: dict = {}) -> None:
        self._ID = ID
        self._name = name # character's name
        self._traits = traits # traits the character has
        self._currentLocation = currentLocation # name of current node
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

    
    def __str__(self) -> str:
        return f"Name: {self.name}\nCurrent Location: {self.currentLocation}\nInventory: {self.inventory}"
    