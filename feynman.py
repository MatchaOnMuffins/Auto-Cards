from openai import OpenAI
import streamlit as st

import dotenv

dotenv.load_dotenv()
import os


st.title("Feynman Assistant")

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-4"


subjects = ["Math", "Physics", "Chemistry", "Biology", "Datascience", "Other"]
subject = st.sidebar.selectbox("Select a subject", subjects)

if subject == "Other":
    subject = st.sidebar.text_input("Please specify the subject")

st.session_state.subject = subject


# add clear chat button to sidebar
if st.sidebar.button("Clear chat"):
    st.session_state.messages = []


if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": "Hello, I am the Feynman Assistant. I am here to help you understand concepts. Please select a subject from the sidebar to begin.",
        }
    )

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""

        arr = [
            {"role": m["role"], "content": m["content"]}
            for m in st.session_state.messages
        ]
        arr.insert(
            0,
            {
                "role": "system",
                "content": f"You are a college student who struggling with {st.session_state['subject']}. Your friend is trying to explain a concept to you. You DO NOT know anything about the subject, so you ask them to explain it to you. If your friend says hi, ask them to explain {st.session_state['subject']} to you. remember, you DO NOT know anything, if the user asks you a question, only answer from the information they provided you already.",
            },
        )

        for response in client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=arr,
            stream=True,
        ):
            full_response += response.choices[0].delta.content or ""
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
    st.session_state.messages.append({"role": "assistant", "content": full_response})
