from trading_engine import get_portfolio


def analyze_portfolio():

    portfolio = get_portfolio()

    report = "🤖 Athena Portfolio Analysis\n\n"


    cash = portfolio["cash"]
    stocks = portfolio["stocks"]


    report += f"Available Cash: ${cash:,.2f}\n\n"


    if len(stocks) == 0:

        report += "No stocks owned yet.\n"
        report += "Athena recommends researching opportunities."


    else:

        report += "Current Holdings:\n\n"


        for symbol, data in stocks.items():

            report += (
                f"{symbol}\n"
                f"Shares: {data['shares']}\n"
                f"Average Price: ${data['average_price']}\n\n"
            )


        if len(stocks) > 5:

            report += (
                "Risk Warning: "
                "Portfolio has many positions."
            )

        else:

            report += (
                "Portfolio concentration looks manageable."
            )


    return report
