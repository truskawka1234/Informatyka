 class kolory:
    reset = "\033[0m"
    czerwony = "\033[31m"
    zolty = "\033[33m"
    jasny_zielony = "\033[92m"
    niebieski = "\033[34m"
    Magenta = "\033[35m"
    Cyan = '\033[96m'
    pogrubienie = "\033[1m"
    podkreslenie = "\033[4m"
    tlo_jasny_cyan = "\033[106m"

class Narzedzie_Ogrodowe:
    def __init__(self, nazwa, cena, waga):
        self.nazwa = nazwa
        self.cena = cena
        self.waga = waga
    print(f'\n{kolory.pogrubienie}WITAMY W NASZYM SKLEPIE poniżej mamy działy na jakie jest podzielony nasz sklep {kolory.reset}\n')
    def wyswietl_informacje(self):
        return f'{self.nazwa}\ncena: {self.cena}zł\nwaga: {self.waga}kg'


# =============grabie============================
class Grabie(Narzedzie_Ogrodowe):
    def __init__(self, nazwa, cena, waga, szerokosc):
        super().__init__(nazwa, cena, waga)
        self.szerokosc = szerokosc
    
    def wyswietl_informacje(self):
        print (super().wyswietl_informacje())
        return f'szerokosc: {self.szerokosc}cm'


# ==========szpadel=======================
class Szpadel(Narzedzie_Ogrodowe):
    def __init__(self, nazwa, cena, waga, rodzaj_uchwytu):
        super().__init__(nazwa, cena, waga)
        self.rodzaj_uchwytu = rodzaj_uchwytu

    def wyswietl_informacje(self):
        print(super().wyswietl_informacje())
        return f'uchwyt: {self.rodzaj_uchwytu}'


# =============sekator=====================
class Sekator(Narzedzie_Ogrodowe):
    def __init__(self, nazwa, cena, waga,dlugosc_ostrzy):
        super().__init__(nazwa, cena, waga)
        self.dlugosc_ostrzy = dlugosc_ostrzy

    def wyswietl_informacje(self):
        print(super().wyswietl_informacje())
        return f'dlugość ostrzy: {self.dlugosc_ostrzy}cm'


# ===========kosiarka========================= 
class Kosiarka(Narzedzie_Ogrodowe):
    def __init__(self, nazwa, cena, waga, moc, pojemnosc_worka,wysokosc_koszenia,szerokosc_koszenia):
        super().__init__(nazwa, cena, waga)
        self.moc = moc
        self.pojemnosc_worka = pojemnosc_worka
        self.wysokosc_koszenia = wysokosc_koszenia
        self.szerokosc_koszenia = szerokosc_koszenia


    def wyswietl_informacje(self):
        print(super().wyswietl_informacje())
        return f'moc silnika: {self.moc}KM\npojemność worka na trawę: {self.pojemnosc_worka}L\nwysokość koszenia: {self.wysokosc_koszenia}cm\nszerokość koszenia: {self.szerokosc_koszenia}cm\n'

#=======================wypisywanie=========================================

grabie1 = Grabie(f'\n{kolory.Cyan}{kolory.pogrubienie}{kolory.podkreslenie}GRABIE{kolory.reset}',60, 2,45)
szpadel1 = Szpadel(f'\n{kolory.jasny_zielony}{kolory.pogrubienie}{kolory.podkreslenie}SZPADEL{kolory.reset}',150,3,'plastikowy')
sekator1 = Sekator(f'\n{kolory.Magenta}{kolory.pogrubienie}{kolory.podkreslenie}SEKATOR{kolory.reset}',40,0.5,35)
kosiarka1 = Kosiarka(f'\n{kolory.zolty}{kolory.pogrubienie}{kolory.podkreslenie}KOSIARKA{kolory.reset}',3500,500,15.2,70,'od 30 do 90',102)






# =====================PRACOWNIK I JEGO WYNAGORDZENIE MIESIĘCZNE I ROCZNE =======================================
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
        return f'{kolory.jasny_zielony}{kolory.pogrubienie}{self.dzial_pracy}{kolory.reset} na tym dziale pracuje:{kolory.Magenta} {self.imie} {self.nazwisko}{kolory.reset}'
    

    def wynagrodzenie_mies(self):
        self.konto  += self.wyplata
        return f'\njego wypłata miesięczna wynosi: {kolory.podkreslenie}{self.konto}zł{kolory.reset}'
    
   
    def wynagrodzenie_roczne(self):
         self.konto += self.wyplata*12
         return f'a roczna wypłata wynosi: {kolory.podkreslenie}{self.konto}zł{kolory.reset}'

pracownik1 = Pracownik('Pawel','Piętka','trawniki(1)',500,1000)
pracownik2 = Pracownik('Adam','Kluczyk','Łopaty(2)',300,1200)
pracownik3 = Pracownik('Piotrek','Kozłowski','Sekatory(3)',150,1500)
pracownik4 = Pracownik('Mateusz','Podradziński','Grabie(4)',0,500)

print (pracownik1.info(),pracownik1.wynagrodzenie_mies(),pracownik1.wynagrodzenie_roczne())
print('')
print (pracownik2.info(),pracownik2.wynagrodzenie_mies(),pracownik2.wynagrodzenie_roczne())
print('')
print (pracownik3.info(),pracownik3.wynagrodzenie_mies(),pracownik3.wynagrodzenie_roczne())
print('')
print (pracownik4.info(),pracownik4.wynagrodzenie_mies(),pracownik4.wynagrodzenie_roczne())


# ======================================================================CLASS KLIENT I KUPOWANIE=========================================================================================

class Klient(Osoby):
    def __init__(self, imie, nazwisko, saldo):
        super().__init__(imie, nazwisko)
        self.saldo = saldo
    
    
    def dane(self):
        print(f'\nnazwyasz się {self.imie} {self.nazwisko} masz na koncie: {self.saldo}zł')


    
    def wybor(self):
        print(f'\n{kolory.pogrubienie}wybierz dział w którym planujesz zakupic dany produkt z jego działu (wpisz cyfrę ktora stoi obok nazwy działu){kolory.reset}')
        
        inp = input()
        if inp == '1':
            print(f'{kolory.pogrubienie}{kolory.niebieski}\nOto produkt ktory obecnie znajduję sie na dziale{kolory.reset} {kolory.jasny_zielony}{kolory.pogrubienie} trawniki{kolory.reset}')
            print(kosiarka1.wyswietl_informacje())
            klient1.kup_kosiarki()



        elif inp == '2':
            print(f'{kolory.pogrubienie}{kolory.niebieski}\nOto produkt ktory obecnie znajduję sie na dziale{kolory.reset} {kolory.jasny_zielony}{kolory.pogrubienie} Łopaty{kolory.reset}')
            print(szpadel1.wyswietl_informacje())
            klient1.kup_szpadel()
            
            
        elif inp == '3':
            print(f'{kolory.pogrubienie}{kolory.niebieski}\nOto produkt ktory obecnie znajduję sie na dziale{kolory.reset} {kolory.jasny_zielony}{kolory.pogrubienie} Sekatory{kolory.reset}')
            print(sekator1.wyswietl_informacje())
            klient1.kup_sekator()
        elif inp =='4':
            print(f'{kolory.pogrubienie}{kolory.niebieski}\nOto produkt ktory obecnie znajduję sie na dziale{kolory.reset} {kolory.jasny_zielony}{kolory.pogrubienie} Grabie{kolory.reset}')
            print(grabie1.wyswietl_informacje())
            klient1.kup_grabie()
        else:
            print('zły wybór')
    
# ---------------------------------------------------------------------------------------------------------
    
    
#############################################################################
    def kup_kosiarki(self):                                                 #
        if self.saldo >= kosiarka1.cena:                                    #
            self.saldo -= kosiarka1.cena                                    #
            print("Zakupiono produkt.")                                     #
            print(f"Stan konta po zakupie: {self.saldo} zł")                #
        elif self.saldo < kosiarka1.cena:                                   #
            print("Nie masz wystarczająco pieniędzy na koncie.")            #
                                                                            #
                                                                            #
    def kup_szpadel(self):                                                  #
        if self.saldo >= szpadel1.cena:                                     #
            self.saldo -= szpadel1.cena                                     #
            print("Zakupiono produkt.")                                     #
            print(f"Stan konta po zakupie: {self.saldo} zł")                #
        elif self.saldo < szpadel1.cena:                                    #
            print("Nie masz wystarczająco pieniędzy na koncie.")            #
                                                                            #
                                                                            #
    def kup_sekator(self):                                                  #
        if self.saldo >= sekator1.cena:                                     #   
            self.saldo -= sekator1.cena                                     #   
            print("Zakupiono produkt.")                                     #   
            print(f"Stan konta po zakupie: {self.saldo} zł")                #                           
        elif self.saldo < sekator1.cena:                                    #       
            print("Nie masz wystarczająco pieniędzy na koncie.")            #                               
                                                                            #
    def kup_grabie(self):                                                   #
        if self.saldo >= grabie1.cena:                                      #   
            self.saldo -= grabie1.cena                                      #   
            print("Zakupiono produkt.")                                     #
            print(f"Stan konta po zakupie: {self.saldo} zł")                #
        elif self.saldo < grabie1.cena:                                     #
            print("Nie masz wystarczająco pieniędzy na koncie.")            #
#############################################################################







# ===============wywołanie klienta====================================
klient1 = Klient('Darek','Majewski',2000)
klient1.dane()
klient1.wybor()
        








