from binance.client import Client

API_KEY = "YOUR_KEY"
API_SECRET = "YOUR_SECRET"

client = Client(API_KEY, API_SECRET)

def place_order(symbol, side, quantity):
    order = client.create_order(
        symbol=symbol,
        side=side,
        type="MARKET",
        quantity=quantity
    )
    return order
