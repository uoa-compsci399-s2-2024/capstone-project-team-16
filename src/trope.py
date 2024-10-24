"""Trope Class"""


class Trope:
    """
    A class defining a trope object in an interactive story.
    """
    def __init__(
            self,
            id_: int,
            name: str,
            description: str,
            conflicts: list[int] = None
    ) -> None:
        """
        Initialises a Character instance.

        :param int id_: The ID of a Trope
        :param str name: The name of a Trope
        :param str description: The description of a Trope
        :param list[int] conflicts: A list of tropes which conflict with a Trope
        :rtype: None
        """
        self._id_ = id_
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
        """
        Getter for ID attribute

        :return: The ID of a Trope
        :rtype: int
        """
        return self._id_

    @property
    def name(self) -> str:
        """
        Getter for name attribute

        :return: The name of a Trope
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        """
        Setter for name attribute

        :param str name: The name of a Trope
        :rtype: None
        """
        self._name = name

    @property
    def description(self) -> str:
        """
        Getter for description attribute

        :return: The description of a Trope
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str) -> None:
        """
         Setter for description attribute

         :param str description: The description of a Trope
         :rtype: None
         """
        self._description = description

    @property
    def conflicts(self) -> list[int]:
        """
        Getter for conflicts attribute

        :return: A list of IDs of tropes which conflict with a Trope
        :rtype: list[int]
        """
        return self._conflicts

    @conflicts.setter
    def conflicts(self, conflicts: list[int]) -> None:
        """
         Setter for conflicts attribute

         :param list[int] conflicts: A list of IDs of tropes which conflict with a Trope
         :rtype: None
         """
        self._conflicts = conflicts
