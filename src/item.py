"""Item class"""
import itertools


class Item:
    """
    A class defining an item object in an interactive story.
    All items will inherit from this class, adding their own usage methods and attributes as required.
    """
    id_iter = itertools.count()

    def __init__(
            self,
            name: str,
            category: str,
            weight: float,
            price: float = 1,
            id_: int = None
    ) -> None:
        """
        Initialises an Item instance.

        :param str name: The name of the Item
        :param str category: The category of the Item
        :param float weight: The weight of the Item
        :param float price: The price of the Item
        :param int id_: The id of the Item
        :rtype: None
        """
        self._id_ = next(Item.id_iter) if id_ is None else id_
        self._name = name
        self._weight = weight
        self._category = category
        self._price = price

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

    @property
    def id_(self) -> int:
        """
        Getter for ID attribute

        :return: The ID of an Item
        :rtype: int
        """
        return self._id_

    @property
    def name(self) -> str:
        """
        Getter for name attribute

        :return: The name of an Item
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        """
        Setter for name attribute

        :param str name: The name of an Item
        :rtype: None
        """
        self._name = name

    @property
    def price(self) -> float:
        """
        Getter for price attribute

        :return: The price of an Item
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price: float) -> None:
        """
        Setter for price attribute

        :param float price: The price of an Item
        :rtype: None
        """
        self._price = price

    @property
    def weight(self) -> float:
        """
        Getter for weight attribute

        :return: The weight of an Item
        :rtype: float
        """
        return self._weight

    @weight.setter
    def weight(self, weight: float) -> None:
        """
        Setter for weight attribute

        :param float weight: The weight of an Item
        :rtype: None
        """
        self._weight = weight

    @property
    def category(self) -> str:
        """
        Getter for category attribute

        :return: The category of an Item
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category: str) -> None:
        """
        Setter for category attribute

        :param str category: The category of an Item
        :rtype: None
        """
        self._category = category
