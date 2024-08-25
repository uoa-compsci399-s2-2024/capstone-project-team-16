class Item:
    """
    This class represents an item. All items will inheret from this class, adding its own usage methods and attributes as required
    """
    def __init__(self, ID: int, name: str, type: str, weight: float, price: float = 1, quantity: int = 1):
        self._name = name
        #price is for the total quantity
        self._price = price
        self._quantity = quantity
        self._weight = weight
        self._type = type
        self._ID = ID
    
    #base functions
    def __str__(self) -> str:
        return f"{self.name} x{self.quantity}"
    def __repr__(self) -> str:
        return f"{self.name} x{self.quantity}"
    def __eq__(self, other) -> bool:
        return self.ID == other.ID
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

    #getters and setters
    @property
    def name(self) -> str:
        return self._name
    @name.setter
    def name(self, name: str):
        self._name = name
    @property
    def price(self) -> float:
        return self._price
    @price.setter
    def price(self, price: float):
        self._price = price

    @property
    def weight(self) -> float:
        return self._weight
    @weight.setter
    def weight(self, weight: float):
        self._weight = weight
    
    @property
    def type(self) -> str:
        return self._type
    @type.setter
    def type(self, type: str):
        self._type = type
    
    @property
    def ID(self) -> int:
        return self._ID
    #we shouldn't be changing item IDs so no setter for this property

    @property
    def quantity(self) -> int:
        return self._quantity
    #by default, add and remove methods remove or add 1 to the item stack.
    def add(self, quantity: int =1):
        self._quantity += quantity
    def remove(self, quantity: int =1):
        self._quantity -= quantity
    
