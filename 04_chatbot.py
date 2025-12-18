
import streamlit as st
from ollama import chat


st.set_page_config(
    page_icon="🌍",
    page_title="Streamlit Chatbot",
    initial_sidebar_state="collapsed",
    layout="centered"
)

st.title("☺️ Michaels Chatbot")

# Vorbereitung einer neuen Session (damit
# ich die ausgetauschten Nachrichten nicht
# verliere)
if "messages" not in st.session_state:
    st.session_state["messages"] = []

for message in st.session_state["messages"]:
    st.chat_message(message["role"]).markdown(message["content"])

prompt = st.chat_input(
    "Frag was du willst..."
)

if prompt:

    # Schritt 1: Frage erfassen und ausgeben
    user_message = {"role": "user", "content": prompt}
    st.session_state["messages"].append(user_message)
    st.chat_message("user").markdown(prompt)

    # Schritt 2: Antwort generieren
    response = chat(model="peterparker", messages=st.session_state["messages"])
    answer = response["message"]["content"]

    # Schritt 3: Antwort erfassen und ausgeben
    ai_message = {"role": "ai", "content": answer}
    st.session_state["messages"].append(ai_message)
    st.chat_message("ai").markdown(answer)




