from utils import templates, prompt
from world import World

def initialise_game(client):

	# Choose the tropes
	tropes = ["rags to riches", "chosen one", "orphan hero"]


	# Choose the theme
	themes = ["fantasy"]

	# Construct prompt and generate the scene using the tropes and theme

	characters = prompt.chat_with_gpt(client, "", templates.character_template(3, "main", tropes, themes), None, tokens=500)

	# Construct prompt and generate the locations using the tropes and theme

	locations = prompt.chat_with_gpt(client, "", templates.location_template(3, tropes, themes), None, tokens=500)


	# Construct prompt and generate characters using the tropes and theme

	items = prompt.chat_with_gpt(client, "", templates.item_template(3, tropes, themes), None, tokens=500)


	current_world = World()

	print(characters)
	print(locations)
	print(items)
