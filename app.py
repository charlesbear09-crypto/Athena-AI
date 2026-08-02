from openai import OpenAI
from google.colab import userdata
import traceback

# =====================================
# ATHENA AI
# =====================================

# Get API key from Colab Secrets
api_key = userdata.get("OPENAI_API_KEY").strip()

# Create OpenAI client
client = OpenAI(api_key=api_key)


# --------------------------
# Athena Brain
# --------------------------

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


# --------------------------
# Main Program
# --------------------------

print("=" * 45)
print("            ATHENA AI")
print("=" * 45)
print("Type 'exit' to quit.\n")

while True:

    command = input("You: ")

    if command.lower() == "exit":
        print("\nAthena: Goodbye!")
        break

    try:
        answer = ask_athena(command)
        print("\nAthena:", answer)
        print()

    except Exception:
        print("\nSomething went wrong:\n")
        traceback.print_exc()
        print()
