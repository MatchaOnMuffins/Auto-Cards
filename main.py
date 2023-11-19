import streamlit as st
from pages import Home
from feynman import Feynman
from flashcards import Flashcards
from create_flashcards import CreateFlashcards


# Define the pages
pages = {
    "About Us": Home,
    "Feynman": Feynman,
    "Flashcards": Flashcards,
    "Upload Flashcards": CreateFlashcards
}


# create a navbar
st.sidebar.title("Navigation")
page = st.sidebar.selectbox("What would you like to explore?", list(pages.keys()))
if page == "About Us":
    pages["About Us"]()
elif page == "Flashcards":
    pages["Flashcards"]()
elif page == "Feynman":
    pages["Feynman"]()
elif page == "Upload Flashcards":
    pages["Upload Flashcards"]()
