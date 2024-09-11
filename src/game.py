"""Game Loop"""

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

def get_location(world: World) -> Location:
    '''Function to get next location'''
    pass

def display_location(location: Location) -> None:
    '''Function to display location'''
    print(location.description)

def pass_choice(choice: str) -> None:
    '''Function to process the users choice'''
    pass











def game_loop(player: Character, world: World) -> None:

    game_over = False

    while not game_over:
        current_location = get_location(world)
        display_location(current_location)
        user_choice = choice_selection(world.choices)
        pass_choice(user_choice)
        
