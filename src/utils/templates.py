""" Template functions for generating prompts to send to LLM """


def character_system_message() -> str:
    system_message = ("You are an imaginative game character generator. Create diverse and intriguing "
                            "characters for a role-playing game. Consider different attributes, such as "
                            "traits, motivations and friendliness. Make sure the characters "
                            "fit within a theme. Aim for creativity and originality!")
    return system_message


def item_system_message() -> str:
    system_message = ("You are an imaginative game item generator. Create diverse and intriguing items "
                       "for a role-playing game. Consider different categories, such as "
                       "weapons, armor, potions, and artifacts. Make sure the items are balanced "
                       "for gameplay and fit within a theme. Aim for creativity and originality!")
    return system_message


def location_system_message() -> str:
    system_message = ("You are an imaginative game location generator. Create diverse and intriguing"
                           "locations for a role-playing game. Consider different attributes, such as "
                            "where it is, the items there and the characters there. Make sure the locations "
                           "are consistent and fit within a theme. Aim for creativity and originality!")
    return system_message


def choices_system_message() -> str:
    system_message = ("You are a choice generator for a role playing game. Create engaging and meaningful "
                          "choices for the player. Promote exploration of the storyline. Focus on creativity "
                          "and depth to enhance player engagement and immersion, but keep the choices concise"
                          "and readable for a game-like experience.")
    return system_message


def scene_system_message() -> str:
    system_message = ("You are a scene generator for a choose-your-path role playing game. Create immersive scenes that set the "
                        "stage for player decisions, including vivid descriptions of the setting, atmosphere, "
                        "and key elements. Blend in prior items and characters into the scene if it makes sense. "
                        "Focus on creativity and depth to enhance player immersion and storytelling.")#" Make use of whitespace"
                        #"and make the scene readable and written in a game-like style")
    return system_message


def character_template(quantity: int, type_of_char: str, tropes: list, theme: str) -> str:
    """Template for generating characters"""
    user_message = (f"Create {quantity} {type_of_char} character/s including their "
                    "name and a list of 1-5 word traits. Keep the character consistent "
                    f"with the the tropes of {tropes} and the themes of {theme}. Return this "
                    "in JSON format with the first key being 'characters'.")
    return user_message


def item_template(quantity: int, tropes: list, theme: str) -> str:
    """Template for generating items"""
    user_message = (f"Create {quantity} item/s including their name, "
                    "price, weight and category. Keep the item consistent "
                    f"with the the tropes of {tropes} and the themes of {theme}. Return this "
                    "in JSON format with the first key being 'items'.")
    return user_message


def location_template(quantity: int, tropes: list, theme: str, num_items: int, num_characters: int) -> str:
    """Template for generating the initial locations"""
    user_message = (f"Create {quantity} location/s with a name and a description of the area. "
                    f"Descriptions do not have to be full sentences and should only include "
                    f"important descriptors of the location. Descriptions for the location"
                    " should have no more than 50 words. Keep the location name and description "
                    f"consistent with the tropes of {tropes} and the themes of {theme}. For each location,"
                    f"also generate {num_items} items including their name, "
                    f"price, weight and category. For each location, also generate {num_characters} characters"
                    f"including their name and a list of 1-5 word traits. Keep your overall response to under 700 words.")
    return user_message



def initial_choices_template(quantity: int, tropes: list, theme: str) -> str:
    """Template for generating initial story choices"""
    user_message = (f"Generate {quantity} choices our player can take that make sense for the beginning of a story. "
                    f"These choices should reflect that we're just starting the story and should not speed up the pace "
                    f"of our story rapidly. Make sure the choices are consistent with the tropes of {tropes} and the "
                    f"theme of {theme}. Return this in JSON format with choices being the first key")
    return user_message


def flow_on_choices_template(quantity: int, tropes: list, theme: str, key_events:list,
                             json_locations: list, json_characters: list,
                             json_items: list, actions: list) -> str:
    """Template for generating subsequent story choices"""
    user_message = (f"Generate {quantity} choices our player can take that make sense for the current pacing of the "
                    f"story. The actions in the choices may ONLY include one or more of the following actions: {actions}."
                    f"No other actions can be available to the player if they are not in that list."
                    f"The choices must be consistent with the current pacing of the story and can speed it up "
                    f"slightly but not too much. Make sure the choices are consistent with the tropes of {tropes}, "
                    f"the theme of {theme}, and the key events that have happened so far {key_events}. "
                    "Incorporate some of the characters, items or locations from the given "
                    f"objects into the choices if it makes sense to do so. The objects are in JSON format and are as "
                    f"follows: The list of characters: {json_characters}. The list of items: {json_items}. The list of "
                    f"locations: {json_locations}. new_location action should be an integer of a "
                    "location, None if you are not moving, or -1 if the location isnt known. "
                    "item_to_interact should be an integer of an item or None if you are not interacting with an item.")
    return user_message

def demo_choices_movement_template(list_of_neighbours: list):
    """Template for generating a choices for movement options in the demo"""
    user_message = ("You are to generate movement choices for the user. The locations connected to "
                    f"this location are: {list_of_neighbours} ) The format is \"Name(ID)\", if one "
                    "of the Neighbours are None you are to create a text description describing "
                    "the user going into a mysterious location, You are to be creative with how "
                    "the user can go to this mysterious unknown location You are to return the "
                    "movement choices in a JSON file in the following format { 'choices': [{ "
                    "'description': A very short text description to display to the user, with "
                    "displaying the name ONLY, 'new_location': the integer number ID of the "
                    "location you are to move to or None if the location is unknown} ]}")
    return user_message


def initial_scene_template(location_name: str, location_description: str, items: list,
                   characters: list) -> str:
    """Template for generating a scene to begin the game"""
    user_message = ("You are to create a scene using the following information and output a JSON "
                    f"dictionary. The location is {location_name}, {location_description}. "
                    f"The items in this location are: {items} The Characters in this location "
                    f"are: {characters} Using this information generate text description "
                    "for a scene for the player to interact with. The scene should not be more than"
                    " 100 words in length.")
    return user_message

def flow_scene_template(location_name: str, location_description: str, items: list,
                   characters: list, most_recent_choice: str, key_events: list[str]) -> str:
    """Template for generating a scene after the user makes a choice"""
    user_message = ("You are to create a scene using the following information and output a JSON "
                    f"dictionary. The user has just chosen to do {most_recent_choice}."
                    f"The key events that have happened so far are {key_events}."
                    f"The location is {location_name}, {location_description}. "
                    f"The items in this location are: {items} The Characters in this location "
                    f"are: {characters} Using this information generate text description "
                    "for the next scene in the story. The scene should not be more than"
                    " 100 words in length.")
    return user_message