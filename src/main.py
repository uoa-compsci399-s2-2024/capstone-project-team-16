""" Main module """
import os

from openai import OpenAI

from dotenv import load_dotenv

from initialisation import initialise_game


def main() -> None:
    """ Main function to run game """
    # load environment variables and fetch api key
    load_dotenv()
    openai_api_key = os.getenv('OPENAI_API_KEY')

    # initialise client
    client = OpenAI(api_key=openai_api_key)

    # initialise the game
    initialise_game(client)

if __name__ == "__main__":
    main()
