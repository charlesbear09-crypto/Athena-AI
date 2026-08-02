st.title("🤖 Athena Trading Assistant")


st.write(
    "Athena is monitoring your paper trading account."
)


st.divider()


if st.button("🧠 Analyze Portfolio"):

    report = analyze_portfolio()

    st.success(report)


st.divider()


st.info(
    """
    Athena abilities:
    
    ✅ Read portfolio
    ✅ Analyze positions
    ✅ Monitor trades
    
    Future upgrades:
    
    📈 Live market data
    🤖 AI trade suggestions
    🟢 Buy approval system
    🔴 Sell approval system
    """
)
