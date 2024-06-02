from klasaOsoba import Osoba
from klasaPortfel import Portfel
from klasaWaluta import Waluta
import requests
import time


def get_crypto_prices():
    response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,litecoin&vs_currencies=usd')
    data = response.json()
    btc_price = data['bitcoin']['usd']
    eth_price = data['ethereum']['usd']
    ltc_price = data['litecoin']['usd']
    return btc_price, eth_price, ltc_price

def aktualizuj_ceny_walut():
    btc_price, eth_price, ltc_price = get_crypto_prices()
    BTC.aktualizuj_wartosc(btc_price)
    ETH.aktualizuj_wartosc(eth_price)
    LTC.aktualizuj_wartosc(ltc_price)
BTC = Waluta("BTC", 0)
ETH = Waluta("ETH", 0)
LTC = Waluta('LTC',0)
osoba1 = Osoba(50000)

def program():
    while True:
        aktualizuj_ceny_walut()  # Aktualizacja cem walut 
        print(f'\nWitaj! Masz {osoba1.pieniadze} PLN.')
        print('Dostępne waluty:')
        print(f'1. BTC - {BTC.wartosc} USD za 1 BTC')
        print(f'2. ETH - {ETH.wartosc} USD za 1 ETH')
        print(f'2. LTC - {LTC.wartosc} USD za 1 LTC')

        waluty = {"BTC": BTC, "ETH": ETH, "LTC":LTC}
        
        start_time = time.time()
        while True:
            wybor_waluty = input('Którą walutę chcesz wybrać? (BTC/ETH/LTC): ').upper()
            if wybor_waluty in waluty:
                wybrana_waluta = waluty[wybor_waluty]
                print(f'Aktualna wartość {wybor_waluty} to {wybrana_waluta.wartosc} USD')
                break
            if time.time() - start_time > 20:
                print('Aktualizacja cen walut:')
                aktualizuj_ceny_walut()
                print(f'BTC - {BTC.wartosc} USD za 1 BTC')
                print(f'ETH - {ETH.wartosc} USD za 1 ETH')
                start_time = time.time()
            else:
                print('Nieznana waluta.')

        while True:
            akcja = input('Chcesz kupić czy sprzedać? (kup/sprzedaj): ').lower()
            if akcja == 'kup':
                kwota = float(input('Podaj kwotę w PLN, za którą chcesz kupić walutę: '))
                if kwota > osoba1.pieniadze:
                    print('Nie masz wystarczająco środków.')
                else:
                    osoba1.kup_walute(kwota, wybrana_waluta)
                break
            elif akcja == 'sprzedaj':
                ilosc = float(input(f'Podaj ilość {wybor_waluty}, którą chcesz sprzedać: '))
                osoba1.sprzedaj_walute(wybor_waluty, ilosc, wybrana_waluta)
                break
            else:
                print('Nieznana akcja.')
        
        kontynuacja = input('Czy chcesz kontynuować? (tak/nie): ').lower()
        if kontynuacja != 'tak':
            break
    
    print(f'Kończymy na dziś. Masz {osoba1.pieniadze} PLN.')
    for portfel in osoba1.listaPortfeli:
        print(f'{portfel.nazwa}: {portfel.iloscAktywa:.4f} jednostek')

program()