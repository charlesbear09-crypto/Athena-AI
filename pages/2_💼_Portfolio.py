import streamlit as st

from trading_engine import get_portfolio


st.title("💼 Athena Portfolio")


portfolio = get_portfolio()


# Cash
st.metric(
    "💵 Fake Cash",
    f"${portfolio['cash']:,.2f}"
)


st.divider()


# Holdings
st.subheader("📊 Owned Stocks")


if portfolio["stocks"]:

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


# Trade history
st.subheader("📜 Trade History")


if portfolio["history"]:

    for trade in portfolio["history"]:

        st.write(
            f"""
            **{trade['action']}**

            Stock: {trade['stock']}

            Shares: {trade['shares']}

            Price: ${trade['price']}
            """
        )

else:

    st.write("No trades yet.")
