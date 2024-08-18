# Location Class

class Location:
    def __init__(self, loc_id: int, name: str, characters: list[int], items: list[int], description: str, neighbors: list[Location]):
        self.loc_id = loc_id 
        self.name = name
        self.characters = characters
        self.items = items
        self.description = description
        self.neighbors = neighbors

    def populate(self, num_characters: int) -> None:
    	"""Send prompt to LLM such as 'This is x location in x story with 
    	num_characters of characters. Generate xyz stats for each character.'
    	Once characters generated, add them (or their id numbers) to self.characters
    	list. If needed also do this with items"""
    	pass

    def add_neighbor(self, neighbor: Location) -> None:
    	if neighbor not in neighbors:
    		self.neighbors.append(neighbor)

    
    def __str__(self) -> str:
        return f"Name: {self.name}\nDescription: {self.description}\nCharacters: {self.characters}"

    def __eq__(self, other) -> bool:
    	if isinstance(other, Location):
    		return self.loc_id == other.loc_id
    	else:
    		return False
    