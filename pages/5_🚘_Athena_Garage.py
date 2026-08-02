import streamlit as st
import streamlit.components.v1 as components

from auth import unlock_app


if not unlock_app():
    st.stop()


st.set_page_config(
    page_title="Athena Garage",
    page_icon="🚘",
    layout="wide"
)


st.title("🚘 ATHENA GARAGE")

st.header("🧊 Athena Digital Twin")


html = """
<!DOCTYPE html>

<html>

<head>

<script type="module"
src="https://unpkg.com/@google/model-viewer/dist/model-viewer.min.js">
</script>

</head>


<body>


<model-viewer

src="models/silverado.glb"

camera-controls

auto-rotate

camera-orbit="0deg 70deg 3m"

field-of-view="45deg"

style="
width:100%;
height:600px;
background:#222;
">

</model-viewer>


</body>

</html>
"""


components.html(
    html,
    height=650
)


st.divider()


st.success("Athena Digital Twin System Online")
