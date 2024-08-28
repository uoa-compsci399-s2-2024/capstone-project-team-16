from openai import AsyncOpenAI

from dotenv import load_dotenv

import os
import asyncio

session_messages = list()


async def main() -> None:
    # load environment variables and fetch api key
    load_dotenv()
    openai_api_key = os.getenv('OPENAI_API_KEY')

    # initialise client
    client = AsyncOpenAI(api_key=openai_api_key)


if __name__ == "__main__":
    asyncio.run(main())



