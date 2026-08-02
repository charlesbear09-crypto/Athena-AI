from trading_engine import buy_stock, sell_stock, get_portfolio



def athena_think():

    portfolio = get_portfolio()


    decisions = []



    cash = portfolio["cash"]



    # Example strategy
    # This will later become GPT-powered


    if cash > 1000:

        buy_stock(

            "NVDA",

            1,

            180,

            "Athena identified available capital and selected a growth position."

        )


        decisions.append(
            "Bought NVDA because growth potential was detected."
        )



    return decisions
