import streamlit as st
from openai import OpenAI

# Page settings
st.set_page_config(
    page_title="Athena AI",
    page_icon="🧠",
    layout="centered"
)

# Check API key
if "OPENAI_API_KEY" not in st.secrets:
    st.error("Missing OPENAI_API_KEY in Streamlit Secrets.")
    st.stop()

st.write("Key loaded:", bool(st.secrets.get("OPENAI_API_KEY")))

# Create OpenAI client
client = OpenAI(
    api_key=st.secrets["OPENAI_API_KEY"]
)


# Athena personality
SYSTEM_PROMPT = """
You are Athena, a personal AI assistant.

You are intelligent, helpful, organized, and professional.

You help with:
- coding
- business ideas
- learning
- planning
- research
- productivity
- problem solving

Explain things clearly and step by step.
"""


# Ask Athena
def ask_athena(message):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
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

    except Exception as e:
        return f"ERROR FROM OPENAI:\n\n{e}"


# App title
st.title("🧠 Athena AI")
st.write("Your personal AI assistant")


# Chat memory
if "messages" not in st.session_state:
    st.session_state.messages = []


# Display previous messages
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
