""" Template functions for generating prompts to send to LLM """

def character_template(quantity: int, type_of_char: str, tropes: list, themes: list) -> str:
    """Template for generating characters"""
    user_message = (f"Create a detailed description of {quantity} {type_of_char} character/s including their "
                    "name and a list of traits. Keep the character consistent "
                    f"with the the tropes of {tropes} and the themes of {themes}. Return this "
                    "in JSON format.")
    return user_message


def item_template(quantity: int, tropes: list, themes: list) -> str:
    """Template for generating items"""
    user_message = (f"Create a detailed description of {quantity} item/s including its name, "
                    "price, weight and type. Keep the item consistent "
                    f"with the the tropes of {tropes} and the themes of {themes}. Return this "
                    "in JSON format.")
    return user_message


def location_template(quantity: int, tropes: list, themes: list) -> str:
    """Template for generating locations"""
    user_message = (f"Create {quantity} location/s with a name and a description of the area. Keep the location "
                    f"consistent with the the tropes of {tropes} and the themes of {themes}. "
                    "Return this in JSON format.")
    return user_message


def choices_template(quantity: int, tropes: list, themes: list) -> str:
    """Template for generating story choices"""
    user_message = (f"Generate {quantity} choices our player can take that logically blend in generated locations, "
                    f"characters and items. Make sure the choices are consistent with the tropes of {tropes} and "
                    f"the themes of {themes}. Return this in JSON format.")
    return user_message
