import streamlit as st

# Define your flashcards
flashcards = [
    {"front": "front1", "back": "back1"},
    {"front": "front2", "back": "back2"},
    # Add more flashcards as needed
]

# Initialize session state
if "current_card" not in st.session_state:
    st.session_state.current_card = 0  # Index of the current flashcard
if "show_back" not in st.session_state:
    st.session_state.show_back = False  # Whether to show the back of the card

# Display the current flashcard
# Display the current flashcard
card = flashcards[st.session_state.current_card]
st.subheader("test")
with st.container():
    st.markdown(
        """
    <style>
    .container {
        border: 2px solid #000;
        border-radius: 15px;
        padding: 20px;
        width: 300px;
        height: 200px;
        display: flex;
        justify-content: center;
        align-items: center;
        text-align: center;
        background-color: #343434;
    }
    </style>
    """,
        unsafe_allow_html=True,
    )
    if st.session_state.show_back:
        st.markdown(
            f"<div class='container'>{card['back']}</div>", unsafe_allow_html=True
        )
        if st.button("Show front"):
            st.session_state.show_back = False
    else:
        st.markdown(
            f"<div class='container'>{card['front']}</div>", unsafe_allow_html=True
        )
        if st.button("Show back"):
            st.session_state.show_back = True

if st.button("Next card"):
    st.session_state.current_card = min(
        len(flashcards) - 1, st.session_state.current_card + 1
    )
    st.session_state.show_back = False
