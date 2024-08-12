# Character Class

class Character:
    def __init__(self, name, playable, currentLocation = None, inventory={}):
        self.name = name #characters name
        self.currentLocation = currentLocation #name of current node
        self.inventory = inventory #dict item:quantity
        self.playable = playable #boolean

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
    
    def display_inventory(self): #prints inventory
        print(self.inventory)
    
    def update_location(self, location): #updates current node 
        self.currentLocation = location
    
    def __str__(self):
        return f"Name: {self.name}\nCurrent Location: {self.currentLocation}\nInventory: {self.inventory}"
    