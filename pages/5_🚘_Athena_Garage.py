import streamlit as st

from auth import unlock_app

if not unlock_app():
    st.stop()

st.title("🚘 Athena Garage")

st.write("Launch the 3D Garage below.")

st.link_button(
    "Open Athena Garage",
    "/garage/index.html"
)
