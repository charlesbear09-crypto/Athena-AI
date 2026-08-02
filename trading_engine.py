import json
import os


PORTFOLIO_FILE = "portfolio.json"


def load_portfolio():
    if not os.path.exists(PORTFOLIO_FILE):
        return {
            "cash": 10000,
            "stocks": {},
            "history": []
        }

    with open(PORTFOLIO_FILE, "r") as file:
        return json.load(file)


def save_portfolio(portfolio):
    with open(PORTFOLIO_FILE, "w") as file:
        json.dump(portfolio, file, indent=4)


def buy_stock(symbol, shares, price):
    portfolio = load_portfolio()

    cost = shares * price

    if cost > portfolio["cash"]:
        return False, "Not enough fake cash."

    portfolio["cash"] -= cost

    if symbol not in portfolio["stocks"]:
        portfolio["stocks"][symbol] = {
            "shares": 0,
            "average_price": price
        }

    old_shares = portfolio["stocks"][symbol]["shares"]
    old_average = portfolio["stocks"][symbol]["average_price"]

    new_total_shares = old_shares + shares

    new_average = (
        (old_shares * old_average) + (shares * price)
    ) / new_total_shares

    portfolio["stocks"][symbol]["shares"] = new_total_shares
    portfolio["stocks"][symbol]["average_price"] = round(new_average, 2)


    portfolio["history"].append({
        "action": "BUY",
        "stock": symbol,
        "shares": shares,
        "price": price
    })

    save_portfolio(portfolio)

    return True, "Bought successfully."


def sell_stock(symbol, shares, price):
    portfolio = load_portfolio()

    if symbol not in portfolio["stocks"]:
        return False, "You do not own this stock."

    if portfolio["stocks"][symbol]["shares"] < shares:
        return False, "Not enough shares."

    portfolio["stocks"][symbol]["shares"] -= shares

    money = shares * price

    portfolio["cash"] += money


    portfolio["history"].append({
        "action": "SELL",
        "stock": symbol,
        "shares": shares,
        "price": price
    })


    if portfolio["stocks"][symbol]["shares"] == 0:
        del portfolio["stocks"][symbol]


    save_portfolio(portfolio)

    return True, "Sold successfully."


def get_portfolio():
    return load_portfolio()
