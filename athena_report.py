from trading_engine import get_portfolio


def generate_report():

    portfolio = get_portfolio()


    trades = len(
        portfolio["history"]
    )


    positions = len(
        portfolio["stocks"]
    )


    confidence = 70


    if positions > 3:
        confidence -= 10


    if trades > 5:
        confidence += 10



    return {

        "summary":
        f"""
        Athena scanned your account.

        Current positions:
        {positions}

        Total trades:
        {trades}

        Athena confidence:
        {confidence}%
        """,


        "confidence":
        confidence

    }
