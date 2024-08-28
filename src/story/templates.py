def character_template(type_of_char: str, story_trope: str, story_theme: str) -> str:
    user_message = ("Create a detailed description of a {type} character including their "
                    "name, a list of traits, age, gender, occupation, a dictionary of "
                    "their inventory and a brief backstory. Keep the character consistent "
                    "with the the trope of {trope} and the theme of {theme}. Return this "
                    "in JSON format.").format(type=type_of_char, trope=story_trope, theme=story_theme)
    return user_message


def item_template(story_trope: str, story_theme: str) -> str:
    user_message = ("Create a detailed description of an item including its name, "
                    "price, weight and type. Keep the item consistent "
                    "with the the trope of {trope} and the theme of {theme}. Return this "
                    "in JSON format.").format(trope=story_trope, theme=story_theme)
    return user_message


def location_template(location_characters: list, location_items: list, story_trope: str, story_theme: str) -> str:
    user_message = ("Create a location with a name, these character {characters}, these "
                    "items {items} and a description of the area. Keep the location "
                    "consistent with the the trope of {trope} and the theme of {theme}. "
                    "Return this in JSON format.").format(characters=location_characters, items=location_items,
                                                          trope=story_trope, theme=story_theme)
    return user_message


def main_template() -> str:
    pass

