from openai import OpenAI

from dotenv import load_dotenv

import os

session_messages = list()


def main() -> None:
    # load environment variables and fetch api key
    load_dotenv()
    openai_api_key = os.getenv('OPENAI_API_KEY')

    # initialise client
    client = OpenAI(api_key=openai_api_key)


if __name__ == "__main__":
    main()



