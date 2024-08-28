def character_template(quantity: int, type_of_char: str, tropes: list, themes: list) -> str:
    user_message = ("Create a detailed description of {quantity} {type} character/s including their "
                    "name, a list of traits, age, gender, occupation, a dictionary of "
                    "their inventory and a brief backstory. Keep the character consistent "
                    "with the the tropes of {trope} and the themes of {theme}. Return this "
                    "in JSON format.").format(quantity=quantity, type=type_of_char,
                                              tropes=tropes, themes=themes)
    return user_message


def item_template(quantity: int, tropes: list, themes: list) -> str:
    user_message = ("Create a detailed description of {quantity} item/s including its name, "
                    "price, weight and type. Keep the item consistent "
                    "with the the tropes of {tropes} and the themes of {themes}. Return this "
                    "in JSON format.").format(quantity=quantity, tropes=tropes, themes=themes)
    return user_message


def location_template(quantity: int, tropes: list, themes: list) -> str:
    user_message = ("Create {quantity} location/s with a name and a description of the area. Keep the location "
                    "consistent with the the tropes of {tropes} and the themes of {themes}. "
                    "Return this in JSON format.").format(quantity=quantity, tropes=tropes, themes=themes)
    return user_message


def main_template() -> str:
    pass

