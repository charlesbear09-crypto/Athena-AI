import streamlit as st
from trading_engine import get_portfolio


st.title("💼 Athena Portfolio")


portfolio = get_portfolio()


st.metric(
    "Fake Cash",
    f"${portfolio['cash']:,.2f}"
)


st.subheader("Owned Stocks")


if portfolio["stocks"]:

    for stock, data in portfolio["stocks"].items():

        st.write(
            f"""
            **{stock}**

            Shares: {data['shares']}

            Average Buy Price: ${data['average_price']}
            """
        )

else:
    st.write("No stocks owned yet.")


st.subheader("Trade History")


for trade in portfolio["history"]:
    st.write(trade)
