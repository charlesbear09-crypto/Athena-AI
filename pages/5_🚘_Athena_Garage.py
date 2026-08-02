import streamlit as st
import streamlit.components.v1 as components
import os

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


model_file = "models/silverado.glb"


if os.path.exists(model_file):

    with open(model_file, "rb") as f:

        model_bytes = f.read()


    import base64

    model_data = base64.b64encode(model_bytes).decode()


    html = f"""
    <!DOCTYPE html>
    <html>

    <head>

    <script type="module"
    src="https://unpkg.com/@google/model-viewer/dist/model-viewer.min.js">
    </script>

    </head>


    <body>


    <model-viewer

    src="data:model/gltf-binary;base64,{model_data}"

    camera-controls

    auto-rotate

    style="
    width:100%;
    height:600px;
    background:#111;
    "

    >

    </model-viewer>


    </body>

    </html>
    """


    components.html(
        html,
        height=650
    )


else:

    st.error(
        "Athena cannot find silverado.glb"
    )



st.divider()



st.header("🤖 Athena Vehicle Scan")


st.success(
"""
Digital Twin Connected

Systems Ready:

✅ Exterior Model
✅ Rotation
✅ Zoom
✅ Inspection Mode (coming)
✅ Modification Simulator (coming)
"""
)
