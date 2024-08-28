from location import Location
from character import Character
from item import Item

class World:
	def __init__(
		self,
		locations: dict = None,
		items: dict = None,
		characters: dict = None,
		tropes: list[str] = None,
		themes: list[str] = None
	) -> None:
		self._locations = locations or {}
		self._items = items or {}
		self._characters = characters or {}
		self._tropes = tropes or []
		self._themes = themes or []

	def add_location(self, location: Location) -> None:
		self.locations[location.id_] = location

	def add_character(self, character: Character) -> None:
		self.characters[character.id_] = character

	def add_item(self, item: Item) -> None:
		self.items[item.id_] = item

	def add_trope(self, trope: str) -> None:
		self.tropes.append(trope)

	def add_theme(self, theme: str) -> None:
		self.themes.append(theme)

	def remove_location(self, location_id: int) -> None:
		if location_id in self.locations.keys():
			del self.locations[location_id]

	def remove_character(self, character_id: int) -> None:
		if character_id in self.characters.keys():
			del self.characters[character_id]

	def remove_item(self, item_id: int) -> None:
		if item_id in self.items.keys():
			del self.items[item_id]

	def remove_trope(self, trope: str) -> None:
		if trope in self.tropes:
			self.tropes.remove(trope)

	def remove_theme(self, theme: str) -> None:
		if theme in self.themes:
			self.themes.remove(theme)

	@property
	def locations(self) -> dict:
		"""Getter for locations attribute"""
		return self._locations

	@property
	def characters(self) -> dict:
		"""Getter for characters attribute"""
		return self._characters

	@property
	def items(self) -> dict:
		"""Getter for items attribute"""
		return self._items

	@property
	def tropes(self) -> list[str]:
		"""Getter for tropes attribute"""
		return self._tropes

	@property
	def themes(self) -> list[str]:
		"""Getter for themes attribute"""
		return self._themes