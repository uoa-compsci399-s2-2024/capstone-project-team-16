""" Template functions for generating prompts to send to LLM """

def character_template(quantity: int, type_of_char: str, tropes: list, themes: list) -> str:
    """Template for generating characters"""
    user_message = (f"Create {quantity} {type_of_char} character/s including their "
                    "name and a list of 1-5 word traits. Keep the character consistent "
                    f"with the the tropes of {tropes} and the themes of {themes}. Return this "
                    "in JSON format with the first key being 'characters'.")
    return user_message


def item_template(quantity: int, tropes: list, theme: str) -> str:
    """Template for generating items"""
    user_message = (f"Create {quantity} item/s including their name, "
                    "price, weight and type. Keep the item consistent "
                    f"with the the tropes of {tropes} and the themes of {theme}. Return this "
                    "in JSON format with the first key being 'items'.")
    return user_message


def initial_location_template(quantity: int, tropes: list, theme: str) -> str:
    """Template for generating the initial locations"""
    user_message = (f"Create {quantity} location/s with a name and a description of the area. The "
                    "locations should connect to each other and are allowed cycles. 30% of the "
                    "locations should have a JSON null as a neighbour, rounding up. At least one "
                    "Location needs to have JSON null as a neighbour. Descriptions for the location"
                    " should have no more than 100 words. Keep the location consistent with the "
                    f"tropes of {tropes} and the themes of {theme}. Return this in JSON format. "
                    "Following this format as an example: "
                    "{\"locations\": [{ \"name\": Location, \"description\": Description of "
                    "Location, \"neighbours\": A List of Neighbouring locations allowing for null "
                    "}]}")
    return user_message


def flow_on_location_template(quantity: int,
                              prev_location_name: str, tropes: list, theme: str) -> str:
    """Template for generating flow on locations with a previous node as a neighbor."""
    user_message = (f"Create {quantity} location/s with a name and a description of the area. The "
                    "locations should connect to each other and are allowed cycles. 30% of the "
                    "locations should have a JSON null as a neighbour At least one Location needs "
                    "to have JSON null as a neighbour. Only one location is allowed to have a "
                    f"neighbour called {prev_location_name}. {prev_location_name} Should NOT be "
                    "included as a location Descriptions for the location should have no more than "
                    f"100 words. Keep the location consistent with the tropes of {tropes} and "
                    f"the themes of {theme}. Return this in JSON format. Following this format as "
                    "an example: {\"locations\": [{ \"name\": Location, \"description\": "
                    "Description of Location, \"neighbours\": A List of Neighbouring locations "
                    "allowing for null }]}")
    return user_message


def choices_template(quantity: int, tropes: list, theme: str) -> str:
    """Template for generating story choices"""
    user_message = (f"Generate {quantity} choices our player can take that logically blend in generated locations, "
                    f"characters and items. Make sure the choices are consistent with the tropes of {tropes} and "
                    f"the themes of {theme}. Return this in JSON format with choices being the first key")
    return user_message
