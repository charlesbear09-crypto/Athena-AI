import streamlit as st

from auth import unlock_app
from truck_ai import (
    load_truck,
    save_truck,
    add_mod,
    add_maintenance,
    athena_mechanic
)



if not unlock_app():

    st.stop()



st.title("🚘 Athena Garage")



truck = load_truck()



st.subheader(truck["vehicle"])



# BUILD CUSTOMIZER

st.header("🎨 Build Setup")


paint = st.selectbox(
    "Paint",
    [
        "Factory Silver",
        "Candy Purple",
        "Gloss Black",
        "Pearl White"
    ]
)


wheels = st.selectbox(
    "Wheels",
    [
        "Factory Wheels",
        "Chrome Wheels",
        "Black Street Wheels"
    ]
)


suspension = st.selectbox(
    "Suspension",
    [
        "Factory",
        "Lowered",
        "Air Suspension"
    ]
)


engine = st.selectbox(
    "Engine",
    [
        "4.8L Stock",
        "4.8L Cam Build",
        "6.2L Swap"
    ]
)



if st.button("Save Build"):

    truck["paint"] = paint
    truck["wheels"] = wheels
    truck["suspension"] = suspension
    truck["engine"] = engine

    save_truck(truck)

    st.success(
        "Athena saved your build."
    )



st.divider()



# MODS

st.header("🔩 Add Modification")


mod = st.text_input(
    "Example: Headers"
)


if st.button("Add Mod"):

    add_mod(mod)

    st.success(
        "Modification saved."
    )



st.write(
    "Current Mods:"
)


for m in truck["mods"]:

    st.write(
        "• " + m
    )



st.divider()



# COST TRACKER

st.header("💰 Build Cost Planner")


parts = {

    "Camshaft": 500,

    "Headers": 800,

    "Exhaust": 1200,

    "Air Suspension": 3000,

    "6.2L Swap": 6000,

    "Wheels/Tires": 2500

}


total = 0


for part, price in parts.items():

    if st.checkbox(
        f"{part} (${price})"
    ):

        total += price



st.metric(
    "Estimated Build Cost",
    f"${total:,}"
)



st.divider()



# MAINTENANCE

st.header("🛠 Maintenance Tracker")


maintenance = st.text_input(
    "Example: Oil change at 200,000 miles"
)


if st.button("Save Maintenance"):

    add_maintenance(
        maintenance
    )

    st.success(
        "Maintenance saved."
    )



st.divider()



# ATHENA MECHANIC

st.header("🤖 Athena Mechanic")


for advice in athena_mechanic():

    st.info(advice)
