"""Game Loop"""

from actions import move_character
from utils.templates import demo_choices_movement_template
from utils.prompt import chat_with_gpt

def choice_selection(choices: list[str]) -> str:
    '''Function to get user input for the choice'''

    for i, choice in enumerate(choices, start=1):
        print(f"{i}. {choice}")
    
    while True:
        try:
            selection = int(input("> "))
            if 1 <= selection <= len(choices):
                return choices[selection - 1]
            else:
                print("Invalid number")
        except:
            print("Not number") #will need to change these

def get_choices() -> list[str]:
    ''''Function to get choices when that is written'''
    pass


def display_location(location: Location) -> None:
    '''Function to display location'''
    print(location.description)

def pass_choice(choice: str) -> None:
    '''Function to process the users choice'''
    pass



def game_loop(player: Character, world: World, client: OpenAI) -> None:

    game_over = False

    while not game_over:
        current_location = player.current_location
        choices = chat_with_gpt(
            client=client,
            system_message="You are a knowledgable chatbot that generates choices",
            user_message=demo_choices_movement_template(current_location.neighbors),
            context=False
        ) #need a mapper to convert the output to a list of choices
        player_choice = choice_selection(choices)
        move_character(
            character_object=player,
            current_location=current_location,
            new_location=player_choice,
            client=client,
            world_object=world
        )