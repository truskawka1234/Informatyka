class Ludzie:
    def __init__ (self, _imie, _nazwisko, _wzrost, _waga, _wiek):
        self.imie = _imie 
        self.nazwisko = _nazwisko
        self.wzrost = _wzrost
        self.waga = _waga 
        self.wiek = _wiek
    
    def inf(self):
        print(f"imie {self.imie}")
        print(f"nazwisko {self.nazwisko}")
        print(f"wrost{self.wzrost}")
        print(f"waga{self.waga}")
        print("---"*10)
l1 = Ludzie(" Grezgorz", " Braun" , " 178" , " 80", "56 ")
l2 = Ludzie("kot","kot","36","5","5")
l3 = Ludzie("pies", "pies", "40","7","4")
l4 = Ludzie("kazama","jakiś","150","90","18")


l1.inf()
l2.inf()
l3.inf()
l4.inf()

