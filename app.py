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

You are intelligent, helpful, organized, and professional.

You help with:
- coding
- business ideas
- learning
- research
- planning
- productivity
- problem solving

Explain things clearly and step by step.
"""


# Ask Athena
def ask_athena(user_message):
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
                    "content": user_message
                }
            ],
            temperature=0.7
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"OpenAI Error: {e}"


# App title
st.title("🧠 Athena AI")
st.caption("Your personal AI assistant")


# Chat memory
if "messages" not in st.session_state:
    st.session_state.messages = []


# Show old messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])


# Chat input
prompt = st.chat_input("Talk to Athena...")

if prompt:

    # Save user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    # Display user message
    with st.chat_message("user"):
        st.write(prompt)


    # Generate Athena response
    with st.chat_message("assistant"):
        with st.spinner("Athena is thinking..."):
            answer = ask_athena(prompt)
            st.write(answer)


    # Save Athena response
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )
