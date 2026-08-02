import streamlit as st

from auth import unlock_app
from trading_engine import get_portfolio



if not unlock_app():
    st.stop()



st.title("💼 Athena Portfolio")



portfolio = get_portfolio()



st.metric(
    "💵 Fake Cash",
    f"${portfolio['cash']:,.2f}"
)



st.divider()



st.subheader("📊 Holdings")



if portfolio["stocks"]:

    for stock, data in portfolio["stocks"].items():

        st.write(
            f"""
            ## {stock}

            Shares: {data['shares']}

            Average Price: ${data['average_price']}
            """
        )

else:

    st.info("No stocks owned")



st.divider()



st.subheader("📜 Trade History")



for trade in portfolio["history"]:

    st.write(trade)
