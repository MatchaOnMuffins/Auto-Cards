import streamlit as st
from pages import Home, Flashcards, Feynman

# Define the pages
pages = {
    "Home": Home,
    "Flashcards": Flashcards,
    "Feynman": Feynman,
}

sets = []

set_ex = {'name': 'set1', 'cards': [
        {'front': 'front1', 'back': 'back1'}, 
        {'front': 'front2', 'back': 'back2'}]
}

sets.append(set_ex)
curr_card = 0;
curr_set = 0;

# Create a selectbox for navigation
#page = st.sidebar.selectbox("Navigation", list(pages.keys()))
if st.sidebar.button("Home"):
    pages["Home"]()
if st.sidebar.button("Flashcards"):
    pages["Flashcards"](sets, curr_set, curr_card)
if st.sidebar.button("Feynman"):
    pages["Feynman"]()
