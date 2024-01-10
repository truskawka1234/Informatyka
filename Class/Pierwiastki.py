class Pierwiastki:
    def __init__ (self,_okres,_grupa,_nazwa,_symbol):
        self.okres = _okres
        self.grupa = _grupa
        self.nazwa = _nazwa
        self.symbol = _symbol
    def inf(self):
        
        print('--'*11)
        #=================================
        print(f'nazwa = {self.nazwa}')
        print(f'symbol = {self.symbol}')
        print(f'okres = {self.okres}')
        print(f'grupa = {self.grupa}')
        #=================================

p1 = Pierwiastki(13,3,'Glin','Al',)
p1.inf()
p2 = Pierwiastki(14,3,'Krzem','Si')
p2. inf()
p3 = Pierwiastki(15,3,'Fosfor','P')
p3.inf()
p4 = Pierwiastki(16,3,'Siarka','S')
p4.inf()
p5 = Pierwiastki(17,3,'Chlor','Cl')
p5.inf()
p6 = Pierwiastki(18,3,'Argon','Ar')