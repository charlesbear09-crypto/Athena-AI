import streamlit as st

from auth import unlock_app
from trading_engine import buy_stock, sell_stock


if not unlock_app():
    st.stop()



st.title("📈 Athena Paper Trading")


stocks = {

    "AAPL": 220,
    "TSLA": 320,
    "NVDA": 180,
    "MSFT": 520,
    "GOOGL": 190

}



stock = st.selectbox(
    "Select Stock",
    stocks.keys()
)



price = stocks[stock]


st.write(
    f"Current Price: ${price}"
)



shares = st.number_input(
    "Shares",
    min_value=1,
    value=1
)



col1, col2 = st.columns(2)



with col1:

    if st.button("🟢 BUY"):

        success, msg = buy_stock(
            stock,
            shares,
            price
        )

        if success:
            st.success(msg)

        else:
            st.error(msg)




with col2:

    if st.button("🔴 SELL"):

        success, msg = sell_stock(
            stock,
            shares,
            price
        )

        if success:
            st.success(msg)

        else:
            st.error(msg)
