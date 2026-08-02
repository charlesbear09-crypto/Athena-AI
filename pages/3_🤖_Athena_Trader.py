from auth import check_login

if not check_login():
    st.stop()

import streamlit as st

from auth import check_login
from athena_trader import analyze_portfolio


if not check_login():
    st.stop()


st.title("🤖 Athena Trading Assistant")


st.write(
    "Athena is monitoring your paper trading account."
)


if st.button("Analyze Portfolio"):

    report = analyze_portfolio()

    st.success(report)
