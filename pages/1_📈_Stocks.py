st.title("📈 Athena Paper Trading")

st.write(
    "Practice trading with fake money before using real investments."
)


# Fake stock prices for now
stocks = {
    "AAPL": 220,
    "TSLA": 320,
    "NVDA": 180,
    "MSFT": 520,
    "GOOGL": 190
}


selected_stock = st.selectbox(
    "Choose Stock",
    list(stocks.keys())
)


price = stocks[selected_stock]


st.subheader(selected_stock)

st.write(
    f"Current Price: ${price}"
)


shares = st.number_input(
    "Number of Shares",
    min_value=1,
    value=1,
    step=1
)


buy_col, sell_col = st.columns(2)


with buy_col:

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



with sell_col:

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
    "🤖 Athena is connected to this paper trading account."
)
