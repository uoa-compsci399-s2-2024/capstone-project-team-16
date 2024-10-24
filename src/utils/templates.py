""" 
Template functions for generating prompts to send to LLM 
"""


def character_system_message() -> str:
    """
    Character generating system message
    
    :return: A system message for Character generation
    :rtype: str
    """
    system_message = ("You are an imaginative game character generator. Create diverse and intriguing "
                      "characters for a role-playing game. Consider different attributes, such as "
                      "traits, motivations and friendliness. Make sure the characters "
                      "fit within a theme. Aim for creativity and originality!")
    return system_message


def item_system_message() -> str:
    """
    Item generating system message

    :return: A system message for Item generation
    :rtype: str
    """
    system_message = ("You are an imaginative game item generator. Create diverse and intriguing items "
                      "for a role-playing game. Consider different categories, such as "
                      "weapons, armor, potions, and artifacts. Make sure the items are balanced "
                      "for gameplay and fit within a theme. Aim for creativity and originality!")
    return system_message


def location_system_message() -> str:
    """
    Location generating system message

    :return: A system message for Location generation
    :rtype: str
    """
    system_message = ("You are an imaginative game location generator. Create diverse and intriguing"
                      "locations for a role-playing game. Consider different attributes, such as "
                      "where it is, the items there and the characters there. Make sure the locations "
                      "are consistent and fit within a theme. Aim for creativity and originality!")
    return system_message


def choices_system_message() -> str:
    """
    Choices generating system message
    
    :return: A system message for choices generation
    :rtype: str
    """
    system_message = ("You are a choice generator for a role playing game. Create engaging and meaningful "
                      "choices for the player. Promote exploration of the storyline. Focus on creativity "
                      "and depth to enhance player engagement and immersion, but keep the choices concise"
                      "and readable for a game-like experience.")
    return system_message


def scene_system_message() -> str:
    """
    Scene generating system message

    :return: A system message for scene generation
    :rtype: str
    """
    system_message = (
        "You are a scene generator for a choose-your-path role playing game. Create immersive scenes that set the "
        "stage for player decisions, including vivid descriptions of the setting, atmosphere, "
        "and key elements. Blend in prior items and characters into the scene if it makes sense. "
        "Focus on creativity and depth to enhance player immersion and storytelling.")  # " Make use of whitespace"
    # "and make the scene readable and written in a game-like style")
    return system_message


def dialog_system_message() -> str:
    """
    Dialog generating system message

    :return: A system message for dialog generation
    :rtype: str
    """
    system_message = ("You are a dialog creator for a role playing game. Create fitting dialog that"
                      "characters will talk to the player with. Only create small talk and "
                      "background information of that character. Do not have any meaningful dialog "
                      "that would affect story. The dialog should fit within a theme and setting")
    return system_message


def character_template(quantity: int, type_of_char: str, tropes: list, theme: str) -> str:
    """
    Template for the Character generation prompt

    :param int quantity: A number of Characters to be created
    :param str type_of_char: A type of Character to be created
    :param list tropes: A list of Tropes
    :param str theme: A theme
    :return: A prompt for Location generation as a string
    :rtype: str
    """
    user_message = (f"Create {quantity} {type_of_char} character/s including their "
                    "name and a list of 1-5 word traits. Keep the character consistent "
                    f"with the the tropes of {tropes} and the themes of {theme}. Return this "
                    "in JSON format with the first key being 'characters'.")
    return user_message


def item_template(quantity: int, tropes: list, theme: str) -> str:
    """
    Template for the Item generation prompt

    :param int quantity: A number of Items to be created
    :param list tropes: A list of Tropes
    :param str theme: A theme
    :return: The prompt for Item generation as a string
    :rtype: str
    """
    user_message = (f"Create {quantity} item/s including their name, "
                    "price, weight and category. Keep the item consistent "
                    f"with the the tropes of {tropes} and the themes of {theme}. Return this "
                    "in JSON format with the first key being 'items'.")
    return user_message


def location_template(quantity: int, tropes: list, theme: str, num_items: int, num_characters: int) -> str:
    """
    Template for the Location generation prompt

    :param int quantity: A number of Locations to be created
    :param list tropes: A list of Tropes
    :param str theme: A theme
    :param int num_items: A number of Items to be created
    :param int num_characters: A number of Characters to be created
    :return: A prompt for Location generation as a string
    :rtype: str
    """
    user_message = (f"Create {quantity} location/s with a name and a description of the area. "
                    f"Descriptions do not have to be full sentences and should only include "
                    f"important descriptors of the location. Descriptions for the location"
                    " should have no more than 50 words. Keep the location name and description "
                    f"consistent with the tropes of {tropes} and the themes of {theme}. For each location,"
                    f"also generate {num_items} items including their name, "
                    f"price, weight and category. For each location, also generate {num_characters} characters"
                    f"including their name and a list of 1-5 word traits. Keep your overall response to under 700 "
                    f"words.")
    return user_message


def initial_choices_template(quantity: int, tropes: list, theme: str) -> str:
    """
    Template for the initial choices generation prompt

    :param int quantity: A number of initial choices to be created
    :param list tropes: A list of Tropes
    :param str theme: A theme
    :return: A prompt for initial choices generation as a string
    :rtype: str
    """
    user_message = (f"Generate {quantity} choices our player can take that make sense for the beginning of a story. "
                    f"These choices should reflect that we're just starting the story and should not speed up the pace "
                    f"of our story rapidly. Make sure the choices are consistent with the tropes of {tropes} and the "
                    f"theme of {theme}. Return this in JSON format with choices being the first key")
    return user_message


def flow_on_choices_template(quantity: int, tropes: list, theme: str, key_events: list,
                             json_locations: list, json_characters: list,
                             json_items: list, actions: list, character_inventory) -> str:
    """
    Template for the subsequent choices generation prompt

    :param int quantity: A number of subsequent choices to be created
    :param list tropes: A list of Tropes
    :param str theme: A theme
    :param str key_events: A list of key events that have happened
    :param list json_locations: A list of Locations
    :param list json_characters: A list of Characters
    :param list json_items: A list of Items
    :param list actions: A list of possible actions
    :param list character_inventory: A list of items in the player's character's inventory
    :return: A prompt for initial choices generation as a string
    :rtype: str
    """
    user_message = (f"Generate {quantity} choices our player can take that make sense for the current pacing of the "
                    f"story. The actions in the choices may ONLY include one or more of the following actions: "
                    f"{actions}. actions_performed is a list of chosen actions within the choice. The actions within "
                    f"this list must have values the values be not None in the response. Make sure that there is every "
                    f"action explained in the description. No other actions can be available to the player if they are "
                    f"not in that list. The choices must be consistent with the current pacing of the story and can "
                    f"speed it up slightly but not too much. Make sure the choices are consistent with the tropes of "
                    f"{tropes}, the theme of {theme}, and the key events that have happened so far {key_events}. "
                    "Incorporate some of the characters, items or locations from the given "
                    f"objects into the choices if it makes sense to do so. The objects are in JSON format and are as "
                    f"follows: The list of characters: {json_characters}. The list of items: {json_items}. The list of "
                    f"locations: {json_locations}. The character's inventory: {character_inventory}."
                    "new_location action should be an integer of a "
                    "location, None if you are not moving, or \"unknown\" if the location isn't known. "
                    "item_to_interact, pick_up_item or put_down_item should be an integer of an item "
                    "or None if you are not interacting with an item.")
    return user_message


def initial_scene_template(location_name: str, location_description: str, items: list,
                           characters: list, first_beat: str, first_beat_descr: str) -> str:
    """
    Template for the initial scene generation prompt

    :param str location_name: The name of the scene Location
    :param str location_description: A description of the scene Location
    :param list items: A list of Items in the scene Location
    :param list characters: A list of Characters in the scene Location
    :param str first_beat: The name of the first story beat
    :param str first_beat_descr: A description of the first story beat
    :return: A prompt for initial scene generation as a string
    :rtype: str
    """
    user_message = ("You are to create a scene using the following information and output a JSON "
                    f"dictionary. The location is {location_name}, {location_description}. "
                    f"The items in this location are: {items}. The Characters in this location "
                    f"are: {characters}. This scene is the first story beat {first_beat}, which is "
                    f"{first_beat_descr}. Using this information generate text description "
                    "for a scene for the player to interact with. The scene should not be more than"
                    " 100 words in length.")
    return user_message


def flow_scene_template(location_name: str, location_description: str, items: list, characters: list,
                        most_recent_choice: str, key_events: list[str], curr_beat: str, curr_beat_descr: str) -> str:
    """
    Template for the subsequent scene generation prompt

    :param str location_name: The name of the scene Location
    :param str location_description: A description of the scene Location
    :param list items: A list of Items in the scene Location
    :param list characters: A list of Characters in the scene Location
    :param str most_recent_choice: A string describing the most recent choice the player has made
    :param list[str] key_events: A list of key events that have occurred
    :param str curr_beat: The name of the current beat
    :param str curr_beat_descr: A description of the current beat
    :return: A prompt for subsequent scene generation as a string
    :rtype: str
    """
    user_message = ("You are to create a scene using the following information and output a JSON "
                    f"dictionary. The user has just chosen to do {most_recent_choice}."
                    f"The key events that have happened so far are {key_events}."
                    "This scene follows on from the previous scene without moving to the next story beat. "
                    f"The most recent story beat was {curr_beat}, which is described as {curr_beat_descr}, this scene "
                    f"should continue to adhere to elements of that beat. The location is {location_name}, "
                    f"{location_description}. The items in this location are: {items} The Characters in this "
                    f"location are: {characters} Using this information generate text description "
                    "for the next scene in the story. The scene should not be more than"
                    " 100 words in length.")
    return user_message


def flow_scene_template_new_beat(location_name: str, location_description: str, items: list,
                                 characters: list, most_recent_choice: str, key_events: list[str],
                                 curr_beat: str, curr_beat_descr: str) -> str:
    """
    Template for the subsequent scene generation with a new story beat prompt

    :param str location_name: The name of the scene Location
    :param str location_description: A description of the scene Location
    :param list items: A list of Items in the scene Location
    :param list characters: A list of Characters in the scene Location
    :param str most_recent_choice: A string describing the most recent choice the player has made
    :param list[str] key_events: A list of key events that have occurred
    :param str curr_beat: The name of the current beat
    :param str curr_beat_descr: A description of the current beat
    :return: A prompt for subsequent scene generation with a new story beat as a string
    :rtype: str
    """
    user_message = ("You are to create a scene using the following information and output a JSON "
                    f"dictionary. The user has just chosen to do {most_recent_choice}."
                    f"The key events that have happened so far are {key_events}."
                    f"This scene is the beginning of a new story beat, {curr_beat}, which is described as "
                    f"{curr_beat_descr}. The location is {location_name}, {location_description}. "
                    f"The items in this location are: {items} The Characters in this location "
                    f"are: {characters} Using this information generate text description "
                    "for the next scene in the story. The scene should not be more than"
                    " 100 words in length.")
    return user_message


def dismissive_dialog_template(character_name: str, character_traits: list,
                               playable_character_name: str, theme: str) -> str:
    """Template for the dismissive dialog generation prompt

    :param str character_name: The name of the NPC
    :param list character_traits: A list of traits for the NPC
    :param str playable_character_name: The name of the playable character
    :param str theme: A theme
    :return: A prompt for dismissive dialog as a string
    :rtype: str
    """
    user_message = (f"You are to create dialog from the character {character_name}, they "
                    f"have the following personality traits: {character_traits}. You should keep "
                    f"with these traits when generating this dialog along with the general themes "
                    f"of {theme}. For this dialog you are to be dismissive. The character is "
                    f"talking to another person with the name {playable_character_name}. "
                    f"Do NOT invite further conversation, Be dismissive of the player trying to "
                    f"talk to you. Keep the dialog short and below 25 words.")
    return user_message


def talkative_dialog_template(character_name: str, character_traits: list,
                              playable_character_name: str, theme: str) -> str:
    """Template for the talkative dialog generation prompt

    :param str character_name: The name of the NPC
    :param list character_traits: A list of traits for the NPC
    :param str playable_character_name: The name of the playable character
    :param str theme: A theme
    :return: A prompt for talkative dialog as a string
    :rtype: str
    """
    user_message = (f"You are to create dialog from the character {character_name}, they "
                    f"have the following personality traits: {character_traits}. You should keep "
                    f"with these traits when generating this dialog along with the general themes "
                    f"of {theme}. The player is talking to a character named {playable_character_name}."
                    f"The character should have some initial dialog, followed be player "
                    f"responses/questions which the npc should have reactionary comments/answers "
                    f"to. Keep each dialog option short and below 50 words. Keep the talk vague "
                    f"do not mention any place names")
    return user_message
