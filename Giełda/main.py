from klasa_waluta import Waluta 
from klasa_portfel import Portfel
from klasa_osoba import Osoba


# waluty
BTC = Waluta("BTC", 100000)  
ETH = Waluta("ETH", 20000)   
LTC = Waluta("LTC", 5000)    
# Tworzenie użytkownika
osoba1 = Osoba(50000)  # masz na poczatek 50000zł

# Funkcja glowna
def program():
    while True:
        print(f'\nWitaj! Masz {osoba1.pieniadze} zł.')
        print('Dostępne waluty:')
        print(f'1. BTC - {BTC.wartosc} zł za 1 BTC')
        print(f'2. ETH - {ETH.wartosc} zł za 1 ETH')
        print(f'3. LTC - {LTC.wartosc} zł za 1 LTC')
        
        waluty = {"BTC": BTC, "ETH": ETH, "LTC": LTC}
        
        wybor_waluty = input('Którą walutę chcesz wybrać? (BTC/ETH/LTC): ').upper() # capslock jak piszesz to nie wywala bledu
        if wybor_waluty in waluty:
            wybrana_waluta = waluty[wybor_waluty]
            while True:
                akcja = input('Chcesz kupić czy sprzedać? (kup/sprzedaj): ').lower()
                if akcja == 'kup':
                    kwota = float(input('Podaj kwotę w zł, za którą chcesz kupić walutę: '))
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
        else:
            print('Nieznana waluta.')
        
        kontynuacja = input('Czy chcesz kontynuować? (tak/nie): ').lower()
        if kontynuacja != 'tak':
            break
    
    print(f'Kończymy na dziś. Masz {osoba1.pieniadze} zł.')
    for portfel in osoba1.listaPortfeli:
        print(f'{portfel.nazwa}: {portfel.iloscAktywa:.4f} jednostek')

program()










