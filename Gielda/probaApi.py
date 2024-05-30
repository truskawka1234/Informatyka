import requests
import time

def get_crypto_prices():
    response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd')
    data = response.json()
    btc_price = data['bitcoin']['usd']
    eth_price = data['ethereum']['usd']
    return btc_price, eth_price 

while True:
    btc_price, eth_price = get_crypto_prices()
    print(f"Cena BTC : {btc_price}$")
    print(f'Cena ETH : {eth_price}$')
    time.sleep(20)

# sprawdziłem tak na szybko tą doukumentacje api z coingecko i jest tylko ograniczenie od 5 do 15 zapytan na minute i
# teraz se odpaliłem ten kod tak żeby se troche pochodził i przez 7 min wszystko działało wiec git i przez te 7 min chyba zrobił 25 zapytań więc spoko
