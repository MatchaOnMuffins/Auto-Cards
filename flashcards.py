import streamlit as st
from mongo import get_database

db = get_database().MHacks16


def Flashcards():
    st.title("Flashcards")
    st.write("Here are your flashcards")
