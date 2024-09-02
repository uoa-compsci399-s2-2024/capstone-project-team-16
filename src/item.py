"""Item class"""
import itertools

class Item:
    """
    This class represents an item.
    All items will inherit from this class, adding their
    own usage methods and attributes as required
    """
    id_iter = itertools.count()

    def __init__(
        self,
        name: str,
        category: str,
        weight: float,
        price: float = 1
    ) -> None:
        """
        Initialises an instance of the Item class.
            Parameters:
                id_ (int): unique object ID
                name (str): item name
                weight (float): weight of the item
                category (str): category of the item
                price (float): price of the item
        """
        self._id_ = next(Item.id_iter)
        self._name = name
        self._weight = weight
        self._category = category
        self._price = price

    # base functions
    def __str__(self) -> str:
        return f"Name: {self.name}\nWeight: {self.weight}\nPrice: {self.price}\nType: {self.category}"

    def __repr__(self) -> str:
        return f"Name: {self.name}\nWeight: {self.weight}\nPrice: {self.price}\nType: {self.category}"

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
    def price(self) -> float:
        """Getter for price attribute"""
        return self._price
    @price.setter
    def price(self, price: float) -> None:
        """Setter for price attribute"""
        self._price = price

    @property
    def weight(self) -> float:
        """Getter for weight attribute"""
        return self._weight
    @weight.setter
    def weight(self, weight: float) -> None:
        """Setter for weight attribute"""
        self._weight = weight

    @property
    def category(self) -> str:
        """Getter for category attribute"""
        return self._category
    @category.setter
    def category(self, category: str) -> None:
        """Setter for category attribute"""
        self._category = category
