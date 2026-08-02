import streamlit as st

PASSWORD = "2327"


def unlock_app():

    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False


    if not st.session_state.authenticated:

        st.title("🔐 Athena AI Locked")

        password = st.text_input(
            "Enter Athena Password",
            type="password"
        )


        if st.button("Unlock Athena"):

            if password == PASSWORD:
                st.session_state.authenticated = True
                st.rerun()

            else:
                st.error("Incorrect Password")


        return False


    return True
