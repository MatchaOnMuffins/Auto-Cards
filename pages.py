import streamlit as st

def Home():
    st.title('This is the home page')

def Flashcards(sets, curr_set, curr_card):
    flashcard_sets = [
        {'name': 'set1', 'cards': [
            {'front': 'front1', 'back': 'back1'},
            {'front': 'front2', 'back': 'back2'}]
        },
        {'name': 'set2', 'cards': [
            {'front': 'front1', 'back': 'back1'},
            {'front': 'front2', 'back': 'back2'}]
        },
        {'name': 'set3', 'cards': [
            {'front': 'front1', 'back': 'back1'},
            {'front': 'front2', 'back': 'back2'}]
        }
    ]

    hi

    selected_set = st.sidebar.selectbox("Select Flashcard Set", [s['name'] for s in flashcard_sets])

    if 'flipped' not in st.session_state:
        st.session_state.flipped = False
    
    card = flashcard_sets[curr_set]['cards'][curr_card]

    if (st.session_state.flipped):
        if st.button(card['front']):
            st.session_state.flipped = True
    else:
        if st.button(card['back']):
            st.session_state.flipped = False

def Feynman():
    st.title('This is page 2')
    sets = []
    set_ex = {'name': 'set1', 'cards': [
        {'front': 'front1', 'back': 'back1'}, 
        {'front': 'front2', 'back': 'back2'}]
    }


    sets.append(set_ex)
    for set in sets:
        for set in sets:
            st.sidebar.button(f"{set['name']}")
