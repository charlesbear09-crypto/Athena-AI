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
st.subheader("2004 Silverado 1500 Single Cab 4.8L V8")


st.divider()


st.header("🧊 Athena Digital Twin")


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
    height:650px;
    background:#222;

}

</style>

</head>



<body>


<model-viewer

src="/models/silverado.glb"

camera-controls

auto-rotate

shadow-intensity="1"

exposure="1"

camera-orbit="0deg 75deg 3m"

field-of-view="45deg"

>

</model-viewer>


</body>


</html>

"""


components.html(
    html,
    height=700
)



st.divider()


st.success(
"""
🤖 Athena Digital Twin Online

Systems:

✅ Silverado Model Connected
✅ 3D Viewer Active
🔄 Part Scanner Loading
🔄 Modification System Loading
"""
)
