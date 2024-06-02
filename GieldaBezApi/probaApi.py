import requests
import time
def get_crypto_prices():
    response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd')
    data = response.json()
    btc_price = data['bitcoin']['usd']
    eth_price = data['ethereum']['usd']
    return btc_price, eth_price

while True:
    btc_price, eth_price, = get_crypto_prices()
    print(f"Cena BTC : {btc_price}$")
    print(f'Cena ETH : {eth_price}$')
    time.sleep(20)