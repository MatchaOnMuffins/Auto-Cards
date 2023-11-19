import streamlit as st


def Home():
    st.markdown("# 1. Introduction")

    st.markdown("# 2. Tech Stack")
    st.write("Database: Mongo DB: No SQL database, easy data management and retrieval, SDK dramatically simplifies development. (potentially vector data storage)")
    st.write("Server: Docterized app on GCP")
    st.write("OpenAI: GPT-4-8k, provided by UM ITS")
    st.write("Frontend: Streamlit, easy to use, easy to deploy")

    st.markdown("# 3. Features")
    st.markdown("### Feynman")
    st.write("The Feynman Technique is a learning method that involves explaining a concept in simple terms, identifying gaps in understanding, and refining the explanation. This approach, named after physicist Richard Feynman, helps deepen comprehension and clarify complex ideas.")
    st.write("We achieved this by using GPT-4 to respond as if it didn't know anything about a particular subject. The user would then attempt to explain the subject, and GPT-4 would respond using only information told to it by the user. This would allow the user to identify gaps in their knowledge and refine their explanation.")
    st.markdown("### Flashcards")
    st.write("Everyone takes notes, but not everyone is willing to create flashcards for them. We wanted to make this process easier by allowing users to create flashcards from their notes with the click of a button. This would allow them to study more efficiently and effectively.")
    st.write("Currently, we support uploading a pdf file of the notes, which will then get converted to flashcards by GPT-4.")

    st.markdown("# 4. Usage")
    st.write("An example usage of the Feynman feature would be a user wanted to better their understanding about differential equations. The user would click on the Feynman feature, select other as the subject, and then put \"Differential Equations\" as the specified topic. The user would then be able to explain the subject of differential equations to the bot in a back and forth conversation.")
    
    st.write("An example usage of the Flashcards feature would be if a user had notes for my EECS 280 course, and wanted to create flashcards for them. They would click on the \"Upload Flashcards\" tab, upload the pdf file of their notes, and then the flashcards will be automatically generated and added to the database. The flashcards will then be viewed by going to the \"Flashcards\" tab, where the user can then study them.")

    st.markdown("# 5. Future Improvements")
    st.write("Adding support for youtube videos would be a good addition.")


def Flashcards(sets, curr_set, curr_card):
    flashcard_sets = [
        {
            "name": "set1",
            "cards": [
                {"front": "front1", "back": "back1"},
                {"front": "front2", "back": "back2"},
            ],
        },
        {
            "name": "set2",
            "cards": [
                {"front": "front1", "back": "back1"},
                {"front": "front2", "back": "back2"},
            ],
        },
        {
            "name": "set3",
            "cards": [
                {"front": "front1", "back": "back1"},
                {"front": "front2", "back": "back2"},
            ],
        },
    ]

    selected_set = st.sidebar.selectbox(
        "Select Flashcard Set", [s["name"] for s in flashcard_sets]
    )

    if "flipped" not in st.session_state:
        st.session_state.flipped = False

    card = flashcard_sets[curr_set]["cards"][curr_card]

    if st.session_state.flipped:
        if st.button(card["front"]):
            st.session_state.flipped = True
    else:
        if st.button(card["back"]):
            st.session_state.flipped = False
