import streamlit as st

from athena_trader import analyze_portfolio


st.title("🤖 Athena Trading Assistant")


st.write(
    "Athena is monitoring your paper trading account."
)


st.divider()


if st.button("🧠 Analyze Portfolio"):

    report = analyze_portfolio()

    st.success(report)


st.divider()


st.subheader("Athena Status")


st.write(
    """
    ✅ Portfolio access connected

    ✅ Paper trading engine connected

    ✅ Trade history connected

    🔄 Future upgrades:
    
    - Live stock prices
    - AI market analysis
    - Buy/Hold/Sell recommendations
    - Trade approval system
    """
)
