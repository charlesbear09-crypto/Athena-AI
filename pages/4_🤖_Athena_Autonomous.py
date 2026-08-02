import streamlit as st

from auth import unlock_app
from athena_brain import athena_think
from trading_engine import get_portfolio



if not unlock_app():

    st.stop()



st.title("🤖 Athena Autonomous Trader")



st.write(
    "Athena is monitoring your paper portfolio."
)



if st.button("Run Athena"):

    decisions = athena_think()


    for decision in decisions:

        st.success(decision)




st.divider()



portfolio = get_portfolio()



st.subheader("Athena Activity Log")



for log in portfolio["athena_log"]:

    st.write(

        f"""
        {log['time']}

        Action:
        {log['action']}

        Why:
        {log['reason']}
        """

    )
