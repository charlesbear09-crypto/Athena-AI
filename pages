import streamlit as st
import yfinance as yf
import pandas as pd


st.set_page_config(
    page_title="Athena Stocks",
    page_icon="📈"
)


st.title("📈 Athena Stock Dashboard")

st.write(
    "Track stocks and build your watchlist."
)


# Watchlist

default_stocks = [
    "AAPL",
    "MSFT",
    "NVDA",
    "TSLA"
]


stocks = st.multiselect(
    "Choose stocks to watch:",
    [
        "AAPL",
        "MSFT",
        "NVDA",
        "TSLA",
        "GOOGL",
        "AMZN",
        "META",
        "AMD"
    ],
    default=default_stocks
)



for ticker in stocks:

    stock = yf.Ticker(ticker)

    data = stock.history(
        period="1mo"
    )


    st.subheader(ticker)

    st.line_chart(
        data["Close"]
    )


    current = data["Close"].iloc[-1]

    st.write(
        "Current price:",
        round(current,2)
    )
