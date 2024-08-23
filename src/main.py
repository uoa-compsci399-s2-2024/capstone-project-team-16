import string

from openai import OpenAI

from dotenv import load_dotenv

import os

session_messages = list()


def chat_with_gpt(client: OpenAI, system_message: string, user_message: string,
                  context: bool, freq_penalty: int = 0, tokens: int = 10,
                  pres_penalty: int = 0, temp: int = 1) -> string:
    # when we want to generate a prompt that needs relevant story details
    if context:
        # add the latest prompt to our global list
        session_messages.append({"role": "user", "content": user_message})

        completion = client.chat.completions.create(
            model="gpt-4o-mini-2024-07-18",
            messages=session_messages,
            frequency_penalty=freq_penalty,
            max_tokens=tokens,
            presence_penalty=pres_penalty,
            temperature=temp
        )
        # add the latest response to our global list
        session_messages.append({"role": "assistant", "content": completion.choices[0].message.content})

    # when we want to generate a prompt that doesn't need story like the creation of weapons
    else:
        completion = client.chat.completions.create(
            model="gpt-4o-mini-2024-07-18",
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": user_message}
            ],
            frequency_penalty=freq_penalty,
            max_tokens=tokens,
            presence_penalty=pres_penalty,
            temperature=1
        )

    return completion.choices[0].message.content


def main():
    # load environment variables and fetch api key
    load_dotenv()
    openai_api_key = os.getenv('OPENAI_API_KEY')

    # initialise client
    client = OpenAI(api_key=openai_api_key)

    # starter prompt for testing
    result = chat_with_gpt(client, "you are a helpful chatbot", "list me 10 famous football players", False)


if __name__ == "__main__":
    main()



