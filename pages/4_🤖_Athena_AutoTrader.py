import streamlit as st

from auth import unlock_app
from athena_autotrader import athena_scan_market


if not unlock_app():
    st.stop()



st.title("🤖 Athena Autonomous Trader")


st.write(
    "Athena is monitoring your paper account."
)



if st.button("Run Athena Market Scan"):

    actions = athena_scan_market()


    if actions:

        for action in actions:

            st.success(
                f"""
                {action['action']} {action['stock']}

                Reason:
                {action['reason']}
                """
            )

    else:

        st.info(
            "Athena made no trades."
        )
