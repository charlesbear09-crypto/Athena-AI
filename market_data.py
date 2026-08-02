import random


# Temporary market simulator
# Later we connect real market APIs


STOCKS = {

    "NVDA": 180,
    "AAPL": 220,
    "TSLA": 320,
    "MSFT": 520,
    "GOOGL": 190

}



def get_prices():

    prices = {}


    for stock, price in STOCKS.items():

        change = random.uniform(
            -5,
            5
        )


        prices[stock] = round(
            price + change,
            2
        )


    return prices
