import streamlit as st
from openai import OpenAI
st.write("Key loaded:", bool(st.secrets.get("OPENAI_API_KEY")))
# Page setup
st.set_page_config(
    page_title="Athena AI",
    page_icon="🧠",
    layout="centered"
)

# Load API key
try:
    client = OpenAI(
        api_key=st.secrets["OPENAI_API_KEY"]
    )
except Exception:
    st.error("OpenAI API key not found. Add OPENAI_API_KEY to your Streamlit Secrets.")
    st.stop()


# Athena personality
SYSTEM_PROMPT = """
You are Athena, a personal AI assistant.

You are helpful, intelligent, organized, and professional.
You help with:
- learning
- coding
- business ideas
- planning
- research
- problem solving
- productivity

Give clear answers and explain things step by step.
"""


# Function to ask Athena
def ask_athena(message):
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": message
            }
        ],
        temperature=0.7
    )

    return response.choices[0].message.content


# App UI
st.title("🧠 Athena AI")
st.caption("Your personal AI assistant")


# Chat memory
if "messages" not in st.session_state:
    st.session_state.messages = []


# Show previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])


# User input
user_input = st.chat_input("Talk to Athena...")

if user_input:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    with st.chat_message("user"):
        st.write(user_input)


    with st.chat_message("assistant"):
        with st.spinner("Athena is thinking..."):
            answer = ask_athena(user_input)
            st.write(answer)


    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )
