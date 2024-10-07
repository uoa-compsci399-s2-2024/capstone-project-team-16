import os
from dotenv import load_dotenv
from openai import OpenAI

from src.utils.mappers import dialog_mapper
from src.utils import prompt
from src.utils.structures import DismissiveDialogStructure, TalkativeDialogStructure
from src.utils.templates import dialog_system_message, dismissive_dialog_template, talkative_dialog_template


load_dotenv()
openai_api_key = os.getenv('OPENAI_API_KEY')
# initialise client
client = OpenAI(api_key=openai_api_key)

# Dialog Variables
character_name = "Alice"
character_traits = ["Loyal", "Optimistic", "Stubborn"]
player = "Bob"
theme = "Fantasy"


dialog_raw = prompt.chat_with_gpt(client,
                                   dialog_system_message(),
                                   dismissive_dialog_template(
                                       character_name,
                                       character_traits,
                                       player,
                                       theme),
                                   False,
                                   tokens=500,
                                   structure=DismissiveDialogStructure)
# Map the Dialog
dialog_text = dialog_mapper.dismissive_dialog_mapper(dialog_raw)
print(dialog_text)

dialog_raw = prompt.chat_with_gpt(client,
                                   dialog_system_message(),
                                   talkative_dialog_template(
                                       character_name,
                                       character_traits,
                                       player,
                                       theme),
                                   False,
                                   tokens=500,
                                   temp=1,
                                   structure=TalkativeDialogStructure)
# Map the Dialog
dialog_text = dialog_mapper.talkative_dialog_mapper(dialog_raw)
print(dialog_text[0])
count = 1
# Print user response
for i in range(1, len(dialog_text), 2):
    print(f"{count}. {dialog_text[i]}\n")
    print(f"\t\tFollow Up:{dialog_text[i-1]}\n")
    count += 1
print(f"{count}. End Conversation.\n")
