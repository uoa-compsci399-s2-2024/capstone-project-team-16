import string

from openai import OpenAI
from openai.types.chat import ChatCompletion

session_messages = list()


def chat_with_gpt(client: OpenAI, system_message: string, user_message: string, context: bool) -> ChatCompletion:
    # when we want to generate a prompt that needs relevant story details
    if context:
        session_messages.append({"role": "user", "content": user_message})
        completion = client.chat.completions.create(
            model="gpt-4o-mini-2024-07-18",
            messages=session_messages
        )
        session_messages.append({"role": "assistant", "content": completion.choices[0].message.content})

    # when we want to generate a prompt that doesn't need story like the creation of weapons
    else:
        completion = client.chat.completions.create(
            model="gpt-4o-mini-2024-07-18",
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": user_message}
            ]
        )

    return completion


def main():
    client = OpenAI()




