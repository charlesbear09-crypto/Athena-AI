import streamlit as st
import streamlit.components.v1 as components
import os
import base64

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


    model_data = base64.b64encode(
        model_bytes
    ).decode()


    html = f"""
    <!DOCTYPE html>

    <html>

    <head>

    <script type="module"
    src="https://unpkg.com/@google/model-viewer/dist/model-viewer.min.js">
    </script>


    <style>

    body {{
        margin: 0;
        background: #111;
    }}


    model-viewer {{

        width: 100%;

        height: 650px;

        background: #222;

    }}

    </style>


    </head>



    <body>


    <model-viewer

    src="data:model/gltf-binary;base64,{model_data}"

    camera-controls

    auto-rotate

    rotation-per-second="20deg"

    camera-orbit="0deg 75deg 3m"

    field-of-view="45deg"

    shadow-intensity="1"

    exposure="1"

    environment-image="neutral"

    >

    </model-viewer>



    </body>

    </html>
    """


    components.html(
        html,
        height=700
    )


else:

    st.error(
        "❌ Athena cannot find models/silverado.glb"
    )



st.divider()



# Vehicle Data

left, right = st.columns(2)



with left:

    st.header("🚚 Vehicle Profile")

    st.write(
    """
    **Vehicle:**
    2004 Silverado 1500

    **Cab:**
    Single Cab

    **Engine:**
    4.8L Vortec V8

    **Transmission:**
    Automatic

    **Status:**
    Digital Twin Connected
    """
    )



with right:

    st.header("🤖 Athena Scan")

    st.success(
    """
    Systems Online:

    ✅ 3D Viewer

    ✅ Exterior Inspection

    🔄 Part Scanner

    🔄 Modification Simulator

    🔄 Engine Breakdown
    """
    )



st.divider()



st.header("🔧 Future Inspection Systems")


part = st.selectbox(
    "Select Area",
    [
        "Engine Bay",
        "Interior",
        "Suspension",
        "Brakes",
        "Electrical",
        "Body"
    ]
)


st.info(
    f"Athena is preparing {part} inspection mode."
)
