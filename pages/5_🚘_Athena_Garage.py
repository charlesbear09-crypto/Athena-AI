import streamlit as st

from auth import unlock_app


if not unlock_app():
    st.stop()


st.set_page_config(
    page_title="Athena Garage",
    page_icon="🚘",
    layout="wide"
)


st.title("🚘 ATHENA GARAGE")
st.subheader("2004 Chevrolet Silverado 1500 Single Cab 4.8L V8")


st.divider()


# Truck overview

col1, col2 = st.columns(2)


with col1:

    st.header("🚚 Vehicle Profile")

    st.write(
    """
    **Vehicle:** 2004 Silverado 1500

    **Body:** Single Cab

    **Engine:** 4.8L Vortec V8

    **Transmission:** Automatic

    **Drive System:** Rear Wheel Drive

    **Status:** Stock Configuration
    """
    )


with col2:

    st.header("🤖 Athena Analysis")

    st.info(
    """
    Athena Scan:

    Current platform:
    Reliable V8 truck.

    Suggested build path:

    • Suspension upgrade
    • Wheel/tire setup
    • Exhaust system
    • Cam upgrade
    • 6.2L swap possibility

    Build goal:
    Street performance + show truck.
    """
    )



st.divider()



# Systems

st.header("🔧 Vehicle Systems")


systems = [

    "Engine Bay",

    "Transmission",

    "Suspension",

    "Brakes",

    "Interior",

    "Exterior",

    "Electrical"

]


selected = st.selectbox(
    "Inspect System",
    systems
)



if selected == "Engine Bay":

    st.write(
    """
    🔥 Engine Bay

    Current:
    4.8L Vortec V8

    Athena Notes:

    Possible upgrades:

    ✓ Camshaft
    ✓ Headers
    ✓ Intake
    ✓ Exhaust
    ✓ 6.2L Swap
    """
    )


elif selected == "Suspension":

    st.write(
    """
    Suspension Scan:

    Current:
    Factory suspension

    Future options:

    ✓ Lowering kit
    ✓ Air suspension
    ✓ Performance shocks
    """
    )


elif selected == "Exterior":

    st.write(
    """
    Exterior Customization:

    Planned build:

    ✓ Candy purple paint
    ✓ Dark tint
    ✓ Chrome wheels
    ✓ Larger tires
    ✓ Street style appearance
    """
    )


else:

    st.write(
    f"Athena is scanning {selected}..."
    )



st.divider()


st.header("🧠 Athena Build Assistant")


question = st.text_input(
    "Ask Athena about this truck"
)


if question:

    st.success(
        "Athena response: "
        "This system will connect to your AI model next."
    )
