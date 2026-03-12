import requests
import time
url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
while True:
    response = requests.get(url)
    data = response.json()
    price = data["bitcoin"]["usd"]
    print("BTC price now is", price, "dollars")
    if price > 70000:
        print("BTC price is above 70000 dollars!")
    time.sleep(5)