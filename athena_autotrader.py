from trading_engine import buy_stock, sell_stock, get_portfolio


def athena_scan_market():

    portfolio = get_portfolio()

    actions = []


    # Example AI rules (we will replace with real AI later)

    if portfolio["cash"] > 500:

        success, message = buy_stock(
            "NVDA",
            1,
            180
        )

        if success:

            actions.append({
                "action": "BUY",
                "stock": "NVDA",
                "reason": 
                "Athena detected available cash and identified NVDA as a growth opportunity."
            })


    return actions
