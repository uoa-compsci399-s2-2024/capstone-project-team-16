"""Trope Class"""
import itertools

class Trope:
    """A class defining a trope object in an interactive story."""

    id_iter = itertools.count()
    def __init__(
            self,
            name: str,
            description: str,
            conflicts: list[int] = None
    ) -> None:
        """
        Initialises a Character instance.

            Parameters:
                id_ (int): unique object ID
                name (str): trope's name
                description (str): description of the trope
                conflicts (list): ID's of conflicting tropes
        """
        self._id_ = next(Trope.id_iter)
        self._name = name
        self._description = description
        self._conflicts = conflicts

    # base functions
    def __str__(self) -> str:
        return f"Name: {self.name}\nDescription: {self.description}\nConflicts: {self.conflicts}"

    def __repr__(self) -> str:
        return f"Name: {self.name}\nDescription: {self.description}\nConflicts: {self.conflicts}"

    def __eq__(self, other) -> bool:
        if isinstance(other, Trope):
            return self.id_ == other.id_
        return False

    def __hash__(self) -> int:
        return hash(self.id_)

    def __lt__(self, other) -> bool:
        return self._name < other.name

    def __le__(self, other) -> bool:
        return self._name <= other.name

    def __gt__(self, other) -> bool:
        return self._name > other.name

    def __ge__(self, other) -> bool:
        return self._name >= other.name

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
    def description(self) -> str:
        """Getter for playable attribute"""
        return self._description

    @description.setter
    def description(self, description: str) -> None:
        """Setter for playable attribute"""
        self._description = description

    @property
    def conflicts(self) -> list[int]:
        """Getter for traits attribute"""
        return self._conflicts

    @conflicts.setter
    def conflicts(self, conflicts: list[int]) -> None:
        """Setter for traits attribute"""
        self._conflicts = conflicts
