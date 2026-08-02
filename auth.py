import streamlit as st


PASSWORD = "2327"


def login():

    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False


    if not st.session_state.authenticated:

        st.title("🔐 Athena AI Secure Login")

        password = st.text_input(
            "Enter Password",
            type="password"
        )


        if st.button("Unlock Athena"):

            if password == PASSWORD:

                st.session_state.authenticated = True
                st.success("Athena Unlocked")
                st.rerun()

            else:

                st.error("Incorrect Password")


        return False


    return True
