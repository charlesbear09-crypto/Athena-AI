import streamlit as st


# Athena app password
PASSWORD = "2327"


def check_login():

    # Create login memory
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False


    # If not logged in, show login screen
    if not st.session_state.logged_in:

        st.title("🔐 Athena Secure Access")

        password = st.text_input(
            "Enter Athena Password",
            type="password"
        )


        if st.button("Login"):

            if password == PASSWORD:

                st.session_state.logged_in = True

                st.success("Access Granted")

                st.rerun()

            else:

                st.error("Incorrect Password")


    return st.session_state.logged_in
