class Waluta:
    def __init__(self, nazwa, wartosc):
        self.nazwa = nazwa
        self.wartosc = wartosc
    
    def aktualizuj_wartosc(self, nowa_wartosc):
        self.wartosc = nowa_wartosc