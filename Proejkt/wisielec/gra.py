import random
import os
from losuj import losuj_slowo, losuj_slowo_ekstremalne

class kolory:
    reset = "\033[0m"
    czerwony = "\033[31m"
    zolty = "\033[33m"
    niebieski = "\033[34m"
    Magenta = "\033[35m"
    Cyan = '\033[96m'
    jasny_czerwony = "\033[91m"
    jasny_zielony = "\033[92m"
    jasny_zolty = "\033[93m"
    jasny_zielony = "\033[92m"
    jasny_niebieski = "\033[94m"
    jasny_Magenta = "\033[95m"
    jasny_cyan = "\033[96m"
    tlo_magenta = "\033[45m"
    tlo_jasny_cyan = "\033[106m"
    tlo_bialy= "\033[107m"
    tlo_zielony = "\033[42m"
    tlo_czerwony = "\033[101m"
    tlo_niebieski = "\033[44m"
    tlo_zolty = "\033[43m"
    tlo_czarny  = "\033[40m"

    pogrubienie = "\033[1m"
    podkreslenie = "\033[4m"


# wprowadzanie danych i zmiennych
def gra_ekstremalna(imie, slowo, zycia):
    koniec_gry = False 
    haslo = []
    uzyte = []
    miejsce_litery = 0
    zycia_domyslnie = zycia
    

    print(f'{kolory.jasny_zielony}Twoja liczba żyć:{kolory.reset} {zycia} ')
    #print(slowo)
    for i in range(len(slowo)):
        haslo.append("_")
# główna pętla gry 
    for i in range(len(haslo)):
        print(f'{haslo[i]}', end ='')


    while koniec_gry == False:
        print(f'{kolory.pogrubienie} \npodaj litere: {kolory.reset}')
        while True:
            
            litera = input()
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f' {kolory.tlo_magenta}{kolory.pogrubienie} WISIELEC {kolory.reset}')
            if len(litera) == 1:
                break

            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f'{kolory.jasny_czerwony}Podaj tylko jedną literę{kolory.reset}')
                continue
    
    
# sprawdzam czy litera nalezy do danego slowa
        if slowo[miejsce_litery] == litera:
            haslo[miejsce_litery] = litera
            miejsce_litery = miejsce_litery+1
            uzyte.clear()
            zycia = zycia_domyslnie
            if '_' not in haslo:
                print(f'\n{kolory.tlo_zielony}Brawo {kolory.pogrubienie}{imie} ukończyłes grę {kolory.reset}\n{kolory.podkreslenie}pozostało ci {zycia} żyć{kolory.reset}')
                print()
                exit()
                      
                    
        else:
            if litera not in uzyte:
                uzyte.append(litera)
            print("  NIE MA TAKIEJ LITERY NA TEJ POZYCJI" )
            
            zycia -= 1
            if zycia < 1:
                koniec_gry = True
        print(slowo)        
        for i in range(len(haslo)):
            print(f'{haslo[i]}', end ='')
        print()
    
        print(f'\n Próbujesz odgadnąć literę z pozycji nr = {miejsce_litery+1}')
        print(f'\n niepasujące litery na tej pozycji = {len(uzyte)} : ', end='')
        for i in range(len(uzyte)):
            print(f'{uzyte[i]},', end='')
    
        print('\n pozostałe próby = ', zycia)
    print(f'{kolory.tlo_czerwony}Koniec gry{kolory.pogrubienie} {imie} przegrałeś!{kolory.reset} {kolory.podkreslenie}\nPozostało ci {zycia} żyć\n{kolory.reset}{slowo}')

# --------gra----------

def gra(imie, slowo, zycia):
    koniec_gry = False 
    haslo = []
    uzyte = []
    
    print(f'{kolory.jasny_zielony}Twoja liczba żyć:{kolory.reset} {zycia} ')
    #print(slowo)
    for i in range(len(slowo)):
        haslo.append("_")
# główna pętla gry 
    
    for i in range(len(haslo)):
        print(f'{haslo[i]}', end ='')
        
        

    while koniec_gry == False:
        print(f'{kolory.pogrubienie} \npodaj litere: {kolory.reset}')
        while True:
            
            
            litera = input()
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f' {kolory.tlo_magenta}{kolory.pogrubienie} WISIELEC {kolory.reset}')
            if len(litera) == 1:
                break
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f'{kolory.jasny_czerwony}Podaj tylko jedną literę{kolory.reset}')
                continue
    
# sprawdzam czy litera nalezy do danego slowa
        if litera in slowo:
            for i in range(len(slowo)):
                if slowo[i] == litera:
                    haslo[i] = litera
                    if '_' not in haslo:
                        print(f'\n{kolory.tlo_zielony}Brawo {kolory.pogrubienie}{imie} ukończyłes grę {kolory.reset}\n{kolory.podkreslenie}pozostało ci {zycia} żyć{kolory.reset}')
                        print(f'\nPodczas całej rozgrywki użyłeś takie litery {uzyte}')
                        print()
                        return
                                    
        else:
            if litera not in uzyte:
                uzyte.append(litera)
            print("  NIE MA TAKIEJ LITERY W TYM SŁOWIE" )
            
            zycia -= 1
            if zycia < 1:
                koniec_gry = True
            print(slowo)
        for i in range(len(haslo)):
            print(f'{haslo[i]}', end ='')
        print()
        
    
        print(f'\n niepasujące litery = {len(uzyte)} : ', end='')
        for i in range(len(uzyte)):
            print(f'{uzyte[i]},', end='')
    
            
        print(f'\n{kolory.jasny_zielony} pozostałe próby ={kolory.reset} ', zycia)
    os.system('cls' if os.name == 'nt' else 'clear')    
    print(f'{kolory.tlo_czerwony}Koniec gry{kolory.pogrubienie} {imie} przegrałeś!{kolory.reset} {kolory.podkreslenie}\nPozostało ci {zycia} żyć\n{kolory.reset}{slowo}')


os.system('cls' if os.name == 'nt' else 'clear')
print(f'{kolory.pogrubienie}{kolory.tlo_magenta} ---MENU--- {kolory.reset}')

print(f'\n{kolory.pogrubienie}0 - wyjdź z programu')
print(f'1 - jak grać w tą grę')
print('2 - informacje')
print(f'3 - rozpocznij grę {kolory.reset}')
menu = input(f'{kolory.Cyan}\nco chcesz zrobić: {kolory.reset}')
while True:
    if menu == ('1'):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f'{kolory.pogrubienie}{kolory.tlo_niebieski} instrukcja {kolory.reset}')
        print(f'{kolory.jasny_zielony} |1. Komputer losuje tajne słowo.''\n |2. Twoim zadaniem jest odgadnąć to słowo, zgadując pojedyncze litery.''\n |3. Masz ograniczoną liczbę prób - na przykład, 7''\n |4. Wprowadzasz jedną literę na raz''\n |5. Graj do momentu odgadnięcia słowa lub przegranej.')
        print(f'{kolory.reset}')
        print(f'\n{kolory.pogrubienie}0 - wyjdź z programu')
        print(f'1 - jak grać w tą grę')
        print('2 - informacje')
        print(f'3 - rozpocznij grę {kolory.reset}')
        menu = input(f'{kolory.Cyan}\nco chcesz zrobić: {kolory.reset}')
    elif menu == ('2'):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f'{kolory.pogrubienie}{kolory.tlo_zolty}informacje {kolory.reset}')
        print(f'{kolory.Magenta}|Autor: Mikołaj Jarzębski\n|Gra została stworzona w języku Python jako projekt rozrywkowy.\n|słowa do zgadywania w tej grze zostały utworzone przy po mocy internetu{kolory.reset}')
        print(f'\n{kolory.pogrubienie}0 - wyjdź z programu')
        print(f'1 - jak grać w tą grę')
        print('2 - informacje')
        print(f'3 - rozpocznij grę {kolory.reset}')
        menu = input(f'{kolory.Cyan}\nco chcesz zrobić: {kolory.reset}')

    elif menu == ('3'):

        zycia = 0
        os.system('cls' if os.name == 'nt' else 'clear')
        imie = input(f'{kolory.pogrubienie}Podaj swoje imię:{kolory.reset} ')
        os.system('cls' if os.name == 'nt' else 'clear')

        print(f'\n {kolory.pogrubienie}{kolory.Magenta}---GRA WISIELEC---{kolory.reset}')


        print(f'{kolory.pogrubienie}1- łatwy')
        print('2- średni')
        print(f'3- trudny{kolory.reset}')


# to jes zabezpieczenie
        for i in range(10):
            poziom = input(f'{kolory.jasny_zielony} wybierz poziom {kolory.reset}')
            os.system('cls' if os.name == 'nt' else 'clear')
            if poziom == ("1"):
                slowo = str(losuj_slowo(liczba_znakow_od=1, liczba_znakow_do=5))
                gra(imie, slowo, zycia=8)
                break
            elif poziom == ("2"):
                slowo = str(losuj_slowo(liczba_znakow_od=6, liczba_znakow_do=8))
                gra(imie, slowo, zycia=5)
                break
            elif poziom == ("3"):
                slowo = str(losuj_slowo(liczba_znakow_od=9, liczba_znakow_do=20))
                gra(imie, slowo, zycia=3)

                czy_poziom_ekstremalny = input("Gratuluje ukończyłes njatrudniejszy poziom czy chcesz spróbować czegoś jeszcze trudniejszego T/N " )
                czy_poziom_ekstremalny = czy_poziom_ekstremalny.lower()
                print(czy_poziom_ekstremalny)
                os.system('cls' if os.name == 'nt' else 'clear')
                if czy_poziom_ekstremalny == "t":
                    slowo = str(losuj_slowo_ekstremalne())
                    gra_ekstremalna(imie, slowo, zycia=10)
                elif czy_poziom_ekstremalny == "n":
                    break
                else: 
                    print("nie poprawna odpowiedź")
                break
            else:
                print("zly wybór")
            os.system('cls' if os.name == 'nt' else 'clear')
            if i == 9:
                    print('Koniec prób')
                    exit()
        break
    elif menu == '0':
        print(f'{kolory.pogrubienie}{kolory.jasny_zielony}Dowidzenia{kolory.reset}')
        exit()
    else:
        print('1- jak grać w tą grę')
        print('2- informacje')
        print('3- rozpocznij grę')
        menu = input('co chcesz zrobić: ')


 
#gra(zycia)


#os.system('cls' if os.name == 'nt' else 'clear')
#print(f'{kolory.tlo_czerwony}Koniec gry{kolory.pogrubienie} {imie} przegrałeś!{kolory.reset} {kolory.podkreslenie}\nPozostało ci {zycia} żyć\n{kolory.reset}{slowo}')
