# Character Class

class Character:
    def __init__(self, name: str, playable: bool, currentLocation: str = None, inventory: dict = {}):
        self.name = name #characters name
        self.currentLocation = currentLocation #name of current node
        self.inventory = inventory #dict item:quantity
        self.playable = playable #boolean

    def set_name(self, name):
        self.name = name
    def get_name(self) -> str:
        return self.name
    
    def set_location(self, location):
        self.location = location
    def get_location(self) -> str:
        return self.location
    
    def add_to_inventory(self, item, quantity): #adds an item of specified quantity to inventory 
        if item in self.inventory:
            self.inventory[item] += quantity
        else:
            self.inventory[item] = quantity
    
    def remove_from_inventory(self, item, quantity): #removes an item of specified quantity from inventory
        try:
            if self.inventory[item] > quantity:
                self.inventory -= quantity
            else:
                del self.inventory[item]
        except:
            pass
    
    def __str__(self) -> str:
        return f"Name: {self.name}\nCurrent Location: {self.currentLocation}\nInventory: {self.inventory}"
    