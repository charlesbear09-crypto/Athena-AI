import json
import os
from datetime import datetime


PORTFOLIO_FILE = "portfolio.json"



def load_portfolio():

    if not os.path.exists(PORTFOLIO_FILE):

        return {
            "cash": 10000,
            "stocks": {},
            "history": [],
            "athena_log": []
        }


    with open(PORTFOLIO_FILE, "r") as file:

        return json.load(file)




def save_portfolio(portfolio):

    with open(PORTFOLIO_FILE, "w") as file:

        json.dump(
            portfolio,
            file,
            indent=4
        )




def log_athena(action, reason):

    portfolio = load_portfolio()


    portfolio["athena_log"].append({

        "time": str(datetime.now()),

        "action": action,

        "reason": reason

    })


    save_portfolio(portfolio)





def buy_stock(symbol, shares, price, reason="Manual trade"):

    portfolio = load_portfolio()


    cost = shares * price


    if cost > portfolio["cash"]:

        return False, "Not enough cash"



    portfolio["cash"] -= cost



    if symbol not in portfolio["stocks"]:

        portfolio["stocks"][symbol] = {

            "shares": 0,

            "average_price": price

        }



    old = portfolio["stocks"][symbol]


    total_shares = old["shares"] + shares


    average = (

        (old["shares"] * old["average_price"])

        + (shares * price)

    ) / total_shares



    old["shares"] = total_shares

    old["average_price"] = round(
        average,
        2
    )



    portfolio["history"].append({

        "type": "BUY",

        "stock": symbol,

        "shares": shares,

        "price": price

    })


    save_portfolio(portfolio)


    log_athena(

        f"Bought {shares} shares of {symbol}",

        reason

    )


    return True, "Purchase completed"





def sell_stock(symbol, shares, price, reason="Manual trade"):

    portfolio = load_portfolio()


    if symbol not in portfolio["stocks"]:

        return False, "No shares owned"



    if portfolio["stocks"][symbol]["shares"] < shares:

        return False, "Not enough shares"




    portfolio["stocks"][symbol]["shares"] -= shares


    portfolio["cash"] += shares * price



    portfolio["history"].append({

        "type": "SELL",

        "stock": symbol,

        "shares": shares,

        "price": price

    })



    save_portfolio(portfolio)


    log_athena(

        f"Sold {shares} shares of {symbol}",

        reason

    )


    return True, "Sale completed"





def get_portfolio():

    return load_portfolio()
