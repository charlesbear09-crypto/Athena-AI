import streamlit as st
from openai import OpenAI
import json
import os

# -------------------------
# Setup
# -------------------------

st.set_page_config(
    page_title="Athena AI",
    page_icon="🧠"
)

client = OpenAI(
    api_key=st.secrets["OPENAI_API_KEY"]
)


MEMORY_FILE = "memory.json"


# -------------------------
# Memory System
# -------------------------

def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return []

    with open(MEMORY_FILE, "r") as f:
        return json.load(f)


def save_memory(memory):
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=4)


memory = load_memory()



# -------------------------
# Athena Personality
# -------------------------

def build_context():

    memory_text = "\n".join(memory)

    return f"""
You are Athena, a personal AI assistant.

You are:
- intelligent
- organized
- strategic
- helpful

Your abilities:
- coding help
- business planning
- learning
- research
- productivity

User memory:
{memory_text}

Use memory when helpful.
"""



# -------------------------
# AI Function
# -------------------------

def ask_athena(message):

    response = client.chat.completions.create(

        model="gpt-4o-mini",

        messages=[

            {
                "role":"system",
                "content":build_context()
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
# File Reader
# -------------------------

def read_file(upload):

    text = upload.read().decode(
        "utf-8",
        errors="ignore"
    )

    return text



# -------------------------
# Interface
# -------------------------

st.title("🧠 Athena AI")
st.write("Personal AI Assistant")


# Upload files

st.sidebar.header("Knowledge Upload")

uploaded = st.sidebar.file_uploader(
    "Upload a text file",
    type=["txt","md"]
)


if uploaded:

    content = read_file(uploaded)

    st.sidebar.success(
        "File loaded"
    )


    if st.sidebar.button("Save to Athena memory"):

        memory.append(
            content[:2000]
        )

        save_memory(memory)

        st.sidebar.success(
            "Saved!"
        )



# Chat memory

if "chat" not in st.session_state:

    st.session_state.chat=[]



for msg in st.session_state.chat:

    with st.chat_message(msg["role"]):

        st.write(msg["content"])



prompt = st.chat_input(
    "Talk to Athena..."
)


if prompt:


    st.session_state.chat.append(
        {
            "role":"user",
            "content":prompt
        }
    )


    with st.chat_message("user"):
        st.write(prompt)



    with st.chat_message("assistant"):

        with st.spinner(
            "Athena thinking..."
        ):

            answer = ask_athena(prompt)

            st.write(answer)



    st.session_state.chat.append(
        {
            "role":"assistant",
            "content":answer
        }
    )



# -------------------------
# Memory commands
# -------------------------

st.sidebar.divider()

st.sidebar.write(
    "Memory entries:",
    len(memory)
)


new_memory = st.sidebar.text_input(
    "Teach Athena something:"
)


if st.sidebar.button("Remember"):

    if new_memory:

        memory.append(
            new_memory
        )

        save_memory(memory)

        st.sidebar.success(
            "Athena learned it"
        )
