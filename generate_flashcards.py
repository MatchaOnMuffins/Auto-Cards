import json
import uuid

import openai
import os

from mongo import get_database
import dotenv

dotenv.load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY_SELF")

# Initialize FastAPI app

valid_key = os.getenv("VALID_KEY")


db = get_database()


def format_prompt(prompt, num_flashcards=5):
    format_str = f"""
    The following, between the "___START_CONTEXT___" and "___END_CONTEXT___" blocks, is a set of notes that a user has created. 
    Help them create {num_flashcards}flashcards from these notes.
    ONLY include information between the "___START_CONTEXT___" and "___END_CONTEXT___" blocks. DO NOT include information from anywhere else.
    
    Valid flashcards are formatted as follows:
    
    FRONT: [question here]
    BACK: [answer here]
    
    For example, a valid flashcard would look like this:
    
    FRONT: What is the capital of the United States?
    BACK: Washington, D.C.
    
    ___START_CONTEXT___
    {prompt}
    ___END_CONTEXT___
    """

    return format_str


def get_flashcard_gpt_out(raw_notes_text, number_of_flashcards=5):
    pmpt = format_prompt(prompt=raw_notes_text, num_flashcards=number_of_flashcards)
    completion = openai.ChatCompletion.create(
        engine="gpt-4",
        messages=[
            {
                "role": "system",
                "content": "You are an assistant that creates flashcards from notes, only including information "
                "between the ___START_CONTEXT___ and ___END_CONTEXT___ blocks. You will only output data "
                "in the following format"
                "FRONT: [question here]"
                "BACK: [answer here]",
            },
            {"role": "user", "content": pmpt},
        ],
        stream=False,
    )
    return completion.choices[0].message["content"]


def parse_gpt_output(gpt_out):
    # gpt out is
    # FRONT: [question here]
    # BACK: [answer here]
    card_list = []

    for card in gpt_out.split("\n\n"):
        card = card.strip()
        if card == "":
            continue
        front, back = card.split("\n")
        front = front.replace("FRONT: ", "")
        back = back.replace("BACK: ", "")
        json_out = {"front": front, "back": back}
        # yield {"front": front, "back": back}
        card_list.append(json_out)

    return json.dumps(card_list)


def get_flash_cards(note_text, num_flashcards=5):
    """
    Gets the generated flashcards using the raw notes text.

    Parameters:
    - note_text: Raw notes text

    Modifies:
    - Inserts the generated flashcards into the database
    - Assigns a unique ID to each flashcard

    Returns:
    List of generated flashcards
    """
    gpt_out = get_flashcard_gpt_out(note_text, num_flashcards)
    # json seirialization
    flashcards = []
    for card in json.loads(parse_gpt_output(gpt_out)):
        card["id"] = str(uuid.uuid4())
        flashcards.append(card)

    print("CREATED FLASHCARDS:", flashcards)

    collection = db.MHacks16["flashcards"]
    collection.insert_many(flashcards)
    # remove the _id field
    for card in flashcards:
        card.pop("_id")

    return json.dumps(flashcards)
