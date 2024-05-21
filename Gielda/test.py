# class Waluta:
#     def __init__(self, nazwa, wartosc):
#         self.nazwa = nazwa
#         self.wartosc = wartosc

# class Portfel:
#     def __init__(self, nazwa, iloscAktywa=0):
#         self.nazwa = nazwa
#         self.iloscAktywa = iloscAktywa

#     def kup(self, kwota, waluta):
#         kupiona_ilosc = kwota / waluta.wartosc # wzor
#         self.iloscAktywa += kupiona_ilosc
#         print(f'Kupiono {kupiona_ilosc:.4f} {waluta.nazwa} za {kwota} PLN.')

#     def sprzedaj(self, ilosc, waluta):
#         if ilosc > self.iloscAktywa:
#             print(f'Nie masz wystarczająco {waluta.nazwa} do sprzedania.')
#             return 0
#         else:
#             uzyskana_kwota = ilosc * waluta.wartosc # wzor
#             self.iloscAktywa -= ilosc
#             print(f'Sprzedano {ilosc:.4f} {waluta.nazwa} za {uzyskana_kwota} PLN.')
#             return uzyskana_kwota

# class Osoba:
#     def __init__(self, pieniadze):
#         self.pieniadze = pieniadze
#         self.listaPortfeli = []

#     def znajdz_portfel(self, nazwa_waluty):
#         for portfel in self.listaPortfeli:
#             if portfel.nazwa == nazwa_waluty:
#                 return portfel
#         return None

#     def kup_walute(self, kwota, waluta):
#         portfel = self.znajdz_portfel(waluta.nazwa)
#         if portfel is None:
#             portfel = Portfel(waluta.nazwa)
#             self.listaPortfeli.append(portfel)
#         portfel.kup(kwota, waluta)
#         self.pieniadze -= kwota

#     def sprzedaj_walute(self, nazwa_waluty, ilosc, waluta):
#         portfel = self.znajdz_portfel(nazwa_waluty)
#         if portfel is None:
#             print(f'Nie masz portfela z walutą {nazwa_waluty}.')
#             return
#         uzyskana_kwota = portfel.sprzedaj(ilosc, waluta)
#         self.pieniadze += uzyskana_kwota

# # Przykladowe waluty
# BTC = Waluta("BTC", 100000)  
# ETH = Waluta("ETH", 20000)   
# LTC = Waluta("LTC", 5000)    
# # Tworzenie użytkownika
# osoba1 = Osoba(50000)  # uzytkownik ma na poczatku 50000 PLN

# # Funkcja glowna
# def program():
#     while True:
#         print(f'\nWitaj! Masz {osoba1.pieniadze} PLN.')
#         print('Dostępne waluty:')
#         print(f'1. BTC - {BTC.wartosc} PLN za 1 BTC')
#         print(f'2. ETH - {ETH.wartosc} PLN za 1 ETH')
#         print(f'3. LTC - {LTC.wartosc} PLN za 1 LTC')
        
#         waluty = {"BTC": BTC, "ETH": ETH, "LTC": LTC}
        
#         wybor_waluty = input('Którą walutę chcesz wybrać? (BTC/ETH/LTC): ').upper() # capslock jak piszesz to nie wywala bledu
#         if wybor_waluty in waluty:
#             wybrana_waluta = waluty[wybor_waluty]
#             while True:
#                 akcja = input('Chcesz kupić czy sprzedać? (kup/sprzedaj): ').lower()
#                 if akcja == 'kup':
#                     kwota = float(input('Podaj kwotę w PLN, za którą chcesz kupić walutę: '))
#                     if kwota > osoba1.pieniadze:
#                         print('Nie masz wystarczająco środków.')
#                     else:
#                         osoba1.kup_walute(kwota, wybrana_waluta)
#                     break
#                 elif akcja == 'sprzedaj':
#                     ilosc = float(input(f'Podaj ilość {wybor_waluty}, którą chcesz sprzedać: '))
#                     osoba1.sprzedaj_walute(wybor_waluty, ilosc, wybrana_waluta)
#                     break
#                 else:
#                     print('Nieznana akcja.')
#         else:
#             print('Nieznana waluta.')
        
#         kontynuacja = input('Czy chcesz kontynuować? (tak/nie): ').lower()
#         if kontynuacja != 'tak':
#             break
    
#     print(f'Kończymy na dziś. Masz {osoba1.pieniadze} PLN.')
#     for portfel in osoba1.listaPortfeli:
#         print(f'{portfel.nazwa}: {portfel.iloscAktywa:.4f} jednostek')

# program()