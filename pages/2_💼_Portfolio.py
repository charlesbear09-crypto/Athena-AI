import streamlit as st

from auth import check_login
from trading_engine import get_portfolio


# Lock page
if not check_login():
    st.stop()


st.title("💼 Athena Portfolio")


portfolio = get_portfolio()


# Cash display
st.metric(
    "💵 Fake Cash",
    f"${portfolio['cash']:,.2f}"
)


st.divider()


# Stocks owned
st.subheader("📊 Owned Stocks")


if len(portfolio["stocks"]) > 0:

    for symbol, data in portfolio["stocks"].items():

        st.write(
            f"""
            ### {symbol}

            Shares: {data['shares']}

            Average Buy Price: ${data['average_price']}

            """
        )

else:

    st.info("No stocks owned yet.")



st.divider()


# History
st.subheader("📜 Trade History")


if len(portfolio["history"]) > 0:

    for trade in portfolio["history"]:

        st.write(
            f"""
            {trade['action']} 
            {trade['shares']} shares of 
            {trade['stock']} 
            at ${trade['price']}
            """
        )

else:

    st.write("No trades yet.")
