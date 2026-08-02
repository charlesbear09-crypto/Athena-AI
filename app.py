import streamlit as st
from openai import OpenAI
import json
import os


# -------------------------
# Page Setup
# -------------------------

st.set_page_config(
    page_title="Athena AI",
    page_icon="🧠",
    layout="centered"
)


# -------------------------
# Login System
# -------------------------

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False


if not st.session_state.authenticated:

    st.title("🔒 Athena Login")

    password = st.text_input(
        "Enter Athena password:",
        type="password"
    )

    if st.button("Login"):

        if password == st.secrets["ATHENA_PASSWORD"]:

            st.session_state.authenticated = True
            st.success("Access granted")
            st.rerun()

        else:
            st.error("Incorrect password")

    st.stop()



# -------------------------
# OpenAI Connection
# -------------------------

client = OpenAI(
    api_key=st.secrets["OPENAI_API_KEY"]
)



# -------------------------
# Memory System
# -------------------------

MEMORY_FILE = "memory.json"


def load_memory():

    if not os.path.exists(MEMORY_FILE):
        return []

    with open(MEMORY_FILE, "r") as file:
        return json.load(file)



def save_memory(memory):

    with open(MEMORY_FILE, "w") as file:
        json.dump(memory, file, indent=4)



memory = load_memory()



# -------------------------
# Athena Personality
# -------------------------

def get_context():

    saved_memory = "\n".join(memory)

    return f"""
You are Athena, a personal AI assistant.

You are:
- intelligent
- organized
- strategic
- helpful

Help with:
- coding
- business
- learning
- research
- planning
- productivity

Remember useful information about the user.

User memory:
{saved_memory}
"""



# -------------------------
# Ask Athena
# -------------------------

def ask_athena(message):

    response = client.chat.completions.create(

        model="gpt-4o-mini",

        messages=[

            {
                "role":"system",
                "content":get_context()
            },

            {
                "role":"user",
                "content":message
            }

        ],

        temperature=0.7
    )

    return response.choices[0].message.content



# -------------------------
# Athena Interface
# -------------------------

st.title("🧠 Athena AI")
st.caption("Private personal AI assistant")


if st.button("Logout"):

    st.session_state.authenticated = False
    st.rerun()



# Chat memory

if "messages" not in st.session_state:

    st.session_state.messages = []



for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.write(message["content"])



prompt = st.chat_input(
    "Talk to Athena..."
)



if prompt:


    st.session_state.messages.append(
        {
            "role":"user",
            "content":prompt
        }
    )


    with st.chat_message("user"):
        st.write(prompt)



    with st.chat_message("assistant"):

        with st.spinner("Athena is thinking..."):

            answer = ask_athena(prompt)

            st.write(answer)



    st.session_state.messages.append(
        {
            "role":"assistant",
            "content":answer
        }
    )



# -------------------------
# Teach Athena Memory
# -------------------------

st.sidebar.title("🧠 Athena Memory")


new_memory = st.sidebar.text_input(
    "Teach Athena something:"
)


if st.sidebar.button("Remember"):

    if new_memory:

        memory.append(new_memory)

        save_memory(memory)

        st.sidebar.success(
            "Athena remembered it"
        )


st.sidebar.write(
    "Memory items:",
    len(memory)
)
