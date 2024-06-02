class Portfel:
    def __init__(self, nazwa, iloscAktywa=0):
        self.nazwa = nazwa
        self.iloscAktywa = iloscAktywa

    def kup(self, kwota, waluta):
        kupiona_ilosc = kwota / waluta.wartosc
        self.iloscAktywa += kupiona_ilosc
        print(f'Kupiono {kupiona_ilosc:.10f} {waluta.nazwa} za {kwota} PLN.')

    def sprzedaj(self, ilosc, waluta):
        if ilosc > self.iloscAktywa:
            print(f'Nie masz wystarczająco {waluta.nazwa} do sprzedania.')
            return 0
        else:
            uzyskana_kwota = ilosc * waluta.wartosc
            self.iloscAktywa -= ilosc
            print(f'Sprzedano {ilosc:.10f} {waluta.nazwa} za {uzyskana_kwota} PLN.')
            return uzyskana_kwota