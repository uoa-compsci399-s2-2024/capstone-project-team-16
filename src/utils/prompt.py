""" Utility module for LLM prompt sending """
from openai import OpenAI

SESSION_MESSAGES = []


def chat_with_gpt(client: OpenAI, system_message: str, user_message: str,
                  context: bool, structure, freq_penalty: int = 0, tokens: int = 10,
                  pres_penalty: int = 0, temp: float = 1) -> str:
    """Sends off a prompt to ChatGPT"""

    # when we want to generate a prompt that needs relevant story details
    if context:
        # add the latest prompt to our global list
        SESSION_MESSAGES.append({"role": "user", "content": user_message})

        completion = client.beta.chat.completions.parse(
            model="gpt-4o-mini-2024-07-18",
            messages=SESSION_MESSAGES,
            frequency_penalty=freq_penalty,
            max_tokens=tokens,
            presence_penalty=pres_penalty,
            temperature=temp,
            response_format=structure
        )
        # add the latest response to our global list
        SESSION_MESSAGES.append(
            {
                "role": "assistant",
                "content": completion.choices[0].message.content
            }
        )

    # when we want to generate a prompt that doesn't need story like the creation of weapons
    else:
        completion = client.beta.chat.completions.parse(
            model="gpt-4o-mini-2024-07-18",
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": user_message}
            ],
            frequency_penalty=freq_penalty,
            max_tokens=tokens,
            presence_penalty=pres_penalty,
            temperature=temp,
            response_format=structure
        )

    return completion.choices[0].message.content
