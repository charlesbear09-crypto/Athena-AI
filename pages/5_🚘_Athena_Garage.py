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
st.subheader("2004 Silverado Digital Twin")


html = """

<!DOCTYPE html>

<html>

<head>

<script type="module"
src="https://ajax.googleapis.com/ajax/libs/model-viewer/3.4.0/model-viewer.min.js">
</script>


<style>

body {
    margin:0;
    background:#111;
}


model-viewer {

width:100%;
height:700px;
background:#222;

}

</style>

</head>



<body>


<model-viewer

src="models/silverado.glb"

camera-controls

auto-rotate

auto-rotate-delay="0"

rotation-per-second="30deg"

camera-target="0m 0m 0m"

camera-orbit="0deg 75deg 5m"

field-of-view="60deg"

shadow-intensity="1"

environment-image="neutral"

exposure="1"

>


</model-viewer>



</body>

</html>

"""


components.html(
    html,
    height=750
)
