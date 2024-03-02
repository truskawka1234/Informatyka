class Sklep:
    def __init__(self,marka,cena):
        self.marka = marka  
        self.cena = cena   #  STIHL (wszystkie akcesoria ogrodowe będą tej marki)
    def info_glowne(self):
        return f'nasza firma oferuje sprzęty marki{self.marka}'






class Osoby:
    def __init__ (self,imie,nazwisko):
        self.imie = imie 
        self.nazwisko = nazwisko





class Pracownik(Osoby):
    def __init__(self, imie, nazwisko,dzial_pracy,konto,wyplata):
        super().__init__(imie, nazwisko)
        self.dzial_pracy = dzial_pracy
        self.konto = konto
        self.wyplata = wyplata

    def info(self):
        return f'to jest nasz pracownik, nazywa sie{self.imie},{self.nazwisko} pracuję on na dziale{self.dzial_pracy}'
    

    def wynagrodzenie_mies(self):
        self.konto  += self.wyplata
        return f'{self.konto}'
    
   
    def wynagrodzenie_roczne(self):
         self.konto += self.wyplata*12
         return f'{self.konto}'

pracownik1 = Pracownik('Pawel','Piętka','trawników',500,1000)
print (pracownik1.info())
print (pracownik1.wynagrodzenie_roczne())

# ===========================================================================================




class Lopata(Sklep):
    def __init__(self, marka, cena, przedmiot):
        super().__init__(marka, cena)
        self.przedmiot = przedmiot

    def wiadomosc(self):
        return f'{self.przedmiot} marki {self.marka}, w cenie {self.cena}'


lopatka = Lopata('Sthil',140,'łopata')
print (lopatka.wiadomosc())











# class Klient(Osoby):     
#     def __init__(self, imie, nazwisko,saldo):
#         super().__init__(imie, nazwisko)
#         self.saldo = saldo
    
#     print("nasz asortyment : \n lopata(a) \n pila(b) \n grabie(c) ")
#     print('\n czego potrzebujesz ?')
#     inp = input('')
#     if inp == 'a':
#         print (Lopata.cena)
    

#     def liczenie(self):
#         if  self.saldo < Lopata.cena:
#             print('nie masz kasy biedaku')


#     def info(self):
#         return f'to jest nasz klient, nazywa sie {self.imie}, {self.nazwisko} saldo = {self.saldo}'

# osoba = Klient('kasia','kowalska',10)
# osoba.liczenie()















    
        