from utils import templates, prompt
from world import World

def initialise_game(client):

	# Choose the tropes
	tropes = ["rags to riches", "chosen one", "orphan hero"]


	# Choose the theme
	themes = ["fantasy"]

	# Construct prompt and generate the characters using the tropes and theme

	characters = prompt.chat_with_gpt(client, "", templates.character_template(3, "main", tropes, themes), None, tokens=500)

	# Construct prompt and generate the locations using the tropes and theme

	locations = prompt.chat_with_gpt(client, "", templates.location_template(3, tropes, themes), None, tokens=500)


	# Construct prompt and generate items using the tropes and theme

	items = prompt.chat_with_gpt(client, "", templates.item_template(3, tropes, themes), None, tokens=500)


	current_world = World()

	# mappers go here

	# for character in mapped_characters: current_world.add_character(character)
	# etc

	print(characters)
	print(locations)
	print(items)
