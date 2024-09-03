import requests
import time

def get_bitcoin_price():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
    response = requests.get(url)
    data = response.json()
    price = data["bitcoin"]["usd"]
    return price

def main():
    while True:
        price = get_bitcoin_price()
        print(f"Current Bitcoin price: ${price:.2f}")
        time.sleep(60)  # Update every 1 minute

if __name__ == "__main__":
    main()