from xml.dom.minidom import Document
import streamlit as st
from mongo import get_database
from generate_flashcards import get_flash_cards
import textract
import tempfile
import base64
import pandas as pd
from nlp import get_top_ranked_phrases


db = get_database().MHacks16


def displayPDF(uploaded_file):
    # Read file as bytes:
    bytes_data = uploaded_file

    # Convert to utf-8
    base64_pdf = base64.b64encode(bytes_data).decode("utf-8")

    # Embed PDF in HTML
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="400" type="application/pdf"></iframe>'

    # Display file
    st.markdown(pdf_display, unsafe_allow_html=True)


def CreateFlashcards():
    st.title("Create Flashcards")

    # upload flashcards
    uploaded_file = st.file_uploader(
        "Choose a PDF file that contains your notes", type="pdf"
    )

    if uploaded_file is not None:
        file_bytes = uploaded_file.getvalue()
        displayPDF(file_bytes)
        try:
            with tempfile.NamedTemporaryFile(delete=True) as temp:
                temp.write(file_bytes)
                temp.flush()
                text = textract.process(temp.name, encoding="utf-8", extension=".pdf")
            db["notes"].insert_one({"text": text.decode("utf-8"), "user": "demouser"})

            nlp_result = get_top_ranked_phrases(text.decode("utf-8"))
            df = pd.DataFrame(nlp_result, columns=["Phrase", "Rank", "Count"])
            st.write(df)
            st.line_chart(df, x="Count", y="Rank")
            get_flash_cards(text.decode("utf-8"))
            st.write("Flashcards created successfully!")

        except Exception as e:
            print(e)
            st.write("An error occurred while processing the file.")
