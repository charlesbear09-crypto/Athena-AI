import streamlit as st

from auth import unlock_app
from trading_engine import get_portfolio


if not unlock_app():
    st.stop()



st.set_page_config(
    page_title="Athena AI",
    page_icon="🤖",
    layout="wide"
)



st.title("🤖 Athena AI Command Center")

st.write(
    "Your AI investment assistant dashboard"
)



portfolio = get_portfolio()



# ACCOUNT SECTION

st.header("💰 Account Overview")


col1, col2, col3, col4 = st.columns(4)


with col1:
    st.metric(
        "Cash",
        f"${portfolio['cash']:,.2f}"
    )


with col2:
    st.metric(
        "Positions",
        len(portfolio["stocks"])
    )


with col3:
    st.metric(
        "Trades",
        len(portfolio["history"])
    )


with col4:
    st.metric(
        "Athena Actions",
        len(portfolio.get("athena_log", []))
    )



st.divider()



# HOLDINGS

st.header("📊 Current Holdings")


if portfolio["stocks"]:

    for stock, data in portfolio["stocks"].items():

        st.write(
            f"""
            **{stock}**

            Shares: {data['shares']}

            Average Price: ${data['average_price']}
            """
        )

else:

    st.info(
        "Athena has no current positions."
    )



st.divider()



# ATHENA ACTIVITY

st.header("🧠 Athena Activity")


logs = portfolio.get(
    "athena_log",
    []
)


if logs:

    for log in logs[-5:]:

        st.info(
            f"""
            Time:
            {log['time']}

            Action:
            {log['action']}

            Reason:
            {log['reason']}
            """
        )

else:

    st.write(
        "Athena has not made any decisions yet."
    )



st.divider()



# DAILY RECAP

st.header("📋 Daily Recap")


st.write(
    f"""
    Athena Summary:

    • Portfolio contains {len(portfolio['stocks'])} positions

    • {len(portfolio['history'])} total trades recorded

    • Athena has completed {len(logs)} automated actions

    • System status: ONLINE
    """
)



st.success(
    "🤖 Athena is monitoring your paper trading account."
)
