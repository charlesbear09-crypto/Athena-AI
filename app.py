import streamlit as st

from auth import unlock_app


if not unlock_app():
    st.stop()


st.title("🤖 Athena AI")


st.write(
    """
    Welcome to Athena.

    Your AI assistant for:
    
    📈 Paper Trading
    
    💼 Portfolio Tracking
    
    🧠 AI Market Analysis
    """
)


st.divider()


st.success("Athena is unlocked.")
