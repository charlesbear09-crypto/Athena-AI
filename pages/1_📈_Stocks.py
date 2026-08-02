import streamlit as st
from trading_engine import buy_stock, sell_stock


st.title("📈 Athena Paper Trading")


st.write("Practice trading with fake money before using real investments.")


# Example stocks (we will connect live prices later)
stocks = {
    "AAPL": 220,
    "TSLA": 320,
    "NVDA": 180,
    "MSFT": 520,
    "GOOGL": 190
}


selected_stock = st.selectbox(
    "Choose Stock",
    stocks.keys()
)


price = stocks[selected_stock]


st.subheader(selected_stock)

st.write(
    f"Current Fake Market Price: ${price}"
)


shares = st.number_input(
    "Number of Shares",
    min_value=1,
    step=1
)


col1, col2 = st.columns(2)


with col1:

    if st.button("🟢 BUY"):

        success, message = buy_stock(
            selected_stock,
            shares,
            price
        )

        if success:
            st.success(message)
        else:
            st.error(message)



with col2:

    if st.button("🔴 SELL"):

        success, message = sell_stock(
            selected_stock,
            shares,
            price
        )

        if success:
            st.success(message)
        else:
            st.error(message)



st.divider()

st.info(
    "Athena will eventually analyze these trades and help manage your strategy."
)
