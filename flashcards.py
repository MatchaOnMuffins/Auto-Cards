import random
import streamlit as st
from mongo import get_database
import json

db = get_database().MHacks16


def Flashcards():
    st.title("Flashcards")
    st.write("Here are your flashcards")

    # Initialize session state variables
    if "flipped" not in st.session_state:
        st.session_state["flipped"] = False

    if "current_card" not in st.session_state:
        st.session_state["current_card"] = 0

    # Retrieve all flashcards (assuming each document in the collection is a flashcard)
    flashcards = list(db["flashcards"].find())

    # Check if there are flashcards in the collection
    if not flashcards:
        st.write("No flashcards available.")
        return

    # Display current flashcard
    flashcard = flashcards[st.session_state["current_card"]]
    card_style = """
    <div style="
        border:2px solid black;
        padding:10px;
        margin:10px;
        text-align:center;
        height: 300px;
        border-radius: 25px;
        color: black;
        background-color: #EBEBEBEB;
        font-size: 20px;
    ">
        {content}
    </div>
    """

    if st.session_state["flipped"]:
        card_content = flashcard["back"]
    else:
        card_content = flashcard["front"]

    st.markdown(card_style.format(content=card_content), unsafe_allow_html=True)

    # Display buttons
    c1, c2, c3, c4, c5 = st.columns(5)

    button_flip = c1.button("Flip")
    if button_flip:
        st.session_state["flipped"] = not st.session_state["flipped"]

    button_next = c2.button("Next")
    if button_next:
        st.session_state["flipped"] = False
        st.session_state["current_card"] = (st.session_state["current_card"] + 1) % len(
            flashcards
        )

    button_prev = c3.button("Previous")
    if button_prev:
        st.session_state["flipped"] = False
        st.session_state["current_card"] = (st.session_state["current_card"] - 1) % len(
            flashcards
        )

    button_reset = c4.button("Reset")
    if button_reset:
        st.session_state["flipped"] = False
        st.session_state["current_card"] = 0

    button_shuffle = c5.button("Shuffle")
    if button_shuffle:
        st.session_state["flipped"] = False
        st.session_state["current_card"] = 0
        random.shuffle(flashcards)

