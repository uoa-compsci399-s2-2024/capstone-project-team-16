from openai import AsyncOpenAI

from ..main import SESSION_MESSAGES


async def chat_with_gpt(client: AsyncOpenAI, system_message: str, user_message: str,
                        context: bool, freq_penalty: int = 0, tokens: int = 10,
                        pres_penalty: int = 0, temp: int = 1) -> str:
    # when we want to generate a prompt that needs relevant story details
    if context:
        # add the latest prompt to our global list
        SESSION_MESSAGES.append({"role": "user", "content": user_message})

        completion = await client.chat.completions.create(
            model="gpt-4o-mini-2024-07-18",
            messages=SESSION_MESSAGES,
            frequency_penalty=freq_penalty,
            max_tokens=tokens,
            presence_penalty=pres_penalty,
            temperature=temp
        )
        # add the latest response to our global list
        SESSION_MESSAGES.append({"role": "assistant", "content": completion.choices[0].message.content})

    # when we want to generate a prompt that doesn't need story like the creation of weapons
    else:
        completion = await client.chat.completions.create(
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
