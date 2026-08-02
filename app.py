import streamlit as st

from auth import unlock_app
from trading_engine import get_portfolio
from market_data import get_prices
from athena_report import generate_report



if not unlock_app():
    st.stop()



st.set_page_config(
    page_title="Athena AI",
    page_icon="🤖",
    layout="wide"
)



st.title(
    "🤖 Athena AI Command Center"
)



portfolio = get_portfolio()


report = generate_report()


prices = get_prices()



# TOP METRICS

st.header("💰 Account Status")


a,b,c,d = st.columns(4)


with a:
    st.metric(
        "Cash",
        f"${portfolio['cash']:,.2f}"
    )


with b:
    st.metric(
        "Holdings",
        len(portfolio["stocks"])
    )


with c:
    st.metric(
        "Trades",
        len(portfolio["history"])
    )


with d:
    st.metric(
        "Athena Confidence",
        f"{report['confidence']}%"
    )



st.divider()



# MARKET WATCH

st.header("📈 Market Watch")


for stock, price in prices.items():

    st.write(
        f"""
        **{stock}**

        ${price}
        """
    )



st.divider()



# ATHENA REPORT

st.header("🧠 Athena Morning Briefing")


st.info(
    report["summary"]
)



st.divider()



# ACTIVITY

st.header("📜 Recent Athena Actions")


logs = portfolio.get(
    "athena_log",
    []
)



if logs:

    for item in logs[-5:]:

        st.write(
            item
        )

else:

    st.write(
        "No automated actions yet."
    )
