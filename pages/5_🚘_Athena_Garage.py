import streamlit as st
import os

from auth import unlock_app


if not unlock_app():
    st.stop()


st.title("🚘 Athena Garage Test")


st.write("Checking model file...")


path = "models/silverado.glb"


if os.path.exists(path):

    st.success("✅ Athena found the Silverado model!")

    st.write("File size:")

    st.write(
        os.path.getsize(path),
        "bytes"
    )

else:

    st.error(
        "❌ Athena cannot find the model"
    )


st.write("Current files:")

for root, dirs, files in os.walk("."):

    for file in files:

        if ".glb" in file:

            st.write(
                root,
                file
            )
