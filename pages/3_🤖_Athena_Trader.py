import streamlit as st

from auth import unlock_app
from athena_trader import analyze_portfolio



if not unlock_app():
    st.stop()



st.title("🤖 Athena Trading Assistant")



st.write(
    "Athena is monitoring your paper portfolio."
)



if st.button("🧠 Analyze Portfolio"):

    result = analyze_portfolio()

    st.success(result)
