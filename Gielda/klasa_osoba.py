from klasa_portfel import Portfel
class Osoba:
    def __init__(self, pieniadze):
        self.pieniadze = pieniadze
        self.listaPortfeli = []

    def znajdz_portfel(self, nazwa_waluty):
        for portfel in self.listaPortfeli:
            if portfel.nazwa == nazwa_waluty:
                return portfel
        return None

    def kup_walute(self, kwota, waluta):
        portfel = self.znajdz_portfel(waluta.nazwa)
        if portfel is None:
            portfel = Portfel(waluta.nazwa)
            self.listaPortfeli.append(portfel)
        portfel.kup(kwota, waluta)
        self.pieniadze -= kwota

    def sprzedaj_walute(self, nazwa_waluty, ilosc, waluta):
        portfel = self.znajdz_portfel(nazwa_waluty)
        if portfel is None:
            print(f'Nie masz portfela z walutą {nazwa_waluty}.')
            return
        uzyskana_kwota = portfel.sprzedaj(ilosc, waluta)
        self.pieniadze += uzyskana_kwota