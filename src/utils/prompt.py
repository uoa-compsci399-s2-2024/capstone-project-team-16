"""
Utility module for LLM prompt sending
"""
from openai import OpenAI

SESSION_MESSAGES = []


def chat_with_gpt(client: OpenAI, system_message: str, user_message: str,
                  context: bool, structure, freq_penalty: int = 0, tokens: int = 10,
                  pres_penalty: int = 0, temp: float = 1) -> str:
    """
    Sends off a prompt to ChatGPT and returns the response as a string

    :param OpenAI client: OpenAI client
    :param str system_message: The system message to be sent in the prompt
    :param str user_message: The user message to be sent in the prompt
    :param bool context: A boolean indicating whether the prompt is for narrative
    :param structure: An object specifying the format that the model must output
    :param int freq_penalty: A number between -2.0 and 2.0, positive values decrease the model's likelihood to repeat
    the same line verbatim, defaults to 0
    :param int tokens: The maximum number of tokens that can be generated in the chat completion, defaults to 10
    :param int pres_penalty: A number between -2.0 and 2.0, positive values increase the model's likelihood to talk
    about new topics, defaults to 0
    :param temp: A number between 0 and 2, representing what sampling temperature to use. The higher the number the more
    random and less focussed and deterministic the output will be, defaults to 1
    :return: A string containing the response to the prompt from the model
    :rtype: str
    """
    # For when we want to send prompts for story narrative
    if context:
        # Add the latest prompt to our global list
        SESSION_MESSAGES.append({"role": "system", "content": system_message})
        SESSION_MESSAGES.append({"role": "user", "content": user_message})

        completion = client.beta.chat.completions.parse(
            model="gpt-4o-mini",
            messages=SESSION_MESSAGES,
            frequency_penalty=freq_penalty,
            max_tokens=tokens,
            presence_penalty=pres_penalty,
            temperature=temp,
            response_format=structure
        )

        # Add the latest response to our global list
        SESSION_MESSAGES.append(
            {
                "role": "assistant",
                "content": completion.choices[0].message.content
            }
        )

    # For when we want to send prompts for non-story narrative, such as for weapon creation
    else:
        completion = client.beta.chat.completions.parse(
            model="gpt-4o-mini",
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


def get_session_messages():
    return SESSION_MESSAGES


def add_session_messages(session_messages):
    SESSION_MESSAGES.extend(session_messages)
