# Item Class
class Item:
    """
    This class represents an item. All items will inheret from this class, adding its own usage methods and attributes as required
    """
    def __init__(self, ID: int, name: str, type: str, weight: float, price: float = 1, quantity: int = 1):
        self._name = name
        #price is for the total quantity
        self._price = price
        self._quantity = quantity
    
    #getters and setters
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name: str):
        self._name = name
    @property
    def price(self):
        return self._price
    @price.setter
    def price(self, price: float):
        self._price = price
    @property
    def quantity(self):
        return self._quantity
    #by default, add and remove methods remove or add 1 to the item stack.
    def add(self, quantity: int =1):
        self._quantity += quantity
    def remove(self, quantity: int =1):
        self._quantity -= quantity
    
