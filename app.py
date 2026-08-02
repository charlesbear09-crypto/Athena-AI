import streamlit as st
from openai import OpenAI

# Page setup
st.set_page_config(
    page_title="Athena AI",
    page_icon="🧠",
    layout="centered"
)

# Connect to OpenAI
try:
    client = OpenAI(
        api_key=st.secrets["OPENAI_API_KEY"]
    )
except Exception:
    st.error("OpenAI API key is missing. Add OPENAI_API_KEY in Streamlit Secrets.")
    st.stop()


# Athena personality
SYSTEM_PROMPT = """
You are Athena, a personal AI assistant.

Your job is to help the user with:
- coding
- business ideas
- learning
- research
- planning
- productivity
- problem solving

You are intelligent, organized, and friendly.
Explain things clearly and give step-by-step help when needed.
"""


# Ask Athena
def ask_athena(user_message):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": user_message
            }
        ],
        temperature=0.7
    )

    return response.choices[0].message.content


# Title
st.title("🧠 Athena AI")
st.caption("Your personal AI assistant")


# Store conversation
if "messages" not in st.session_state:
    st.session_state.messages = []


# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])


# User message
if prompt = st.chat_input("Talk to Athena..."):
    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):
        st.write(prompt)


    with st.chat_message("assistant"):
        with st.spinner("Athena is thinking..."):
            try:
                answer = ask_athena(prompt)
                st.write(answer)

            except Exception as e:
                answer = f"Error: {e}"
                st.error(answer)


    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )
