import streamlit as st
from openai import OpenAI

# Get API key from Streamlit Secrets
api_key = st.secrets["OPENAI_API_KEY"]

# Create OpenAI client
client = OpenAI(api_key=api_key)


# Athena Brain
def ask_athena(prompt):
    response = client.chat.completions.create(
        model="gpt-4.1",
        messages=[
            {
                "role": "system",
                "content": """
You are Athena.

You are an advanced AI assistant.

You are intelligent, friendly, and professional.

You help with:
- Coding
- Homework
- Business
- General knowledge
- Problem solving

Never mention ChatGPT unless directly asked.

Always respond as Athena.
"""
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content


# Website UI
st.title("⚡ Athena AI")
st.write("Your personal AI assistant")

user_input = st.text_input("Ask Athena anything:")

if user_input:
    with st.spinner("Athena is thinking..."):
        answer = ask_athena(user_input)

    st.write("### Athena:")
    st.write(answer)
