import random
import os
from losuj import losuj_slowo

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
    
    pogrubienie = "\033[1m"
    podkreslenie = "\033[4m"


# wprowadzanie danych i zmiennych

def gra(imie, zycia, liczba_znakow_od, liczba_znakow_do):
    koniec_gry = False 
    haslo = []
    uzyte = []
    slowo = str(losuj_slowo())
    while True:
        if len(slowo) in range(liczba_znakow_od, liczba_znakow_do):
            break
        else: 
            slowo = str(losuj_slowo())
            continue


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
                        exit()
                        
                    
        else:
            if litera not in uzyte:
                uzyte.append(litera)
            print("  NIE MA TAKIEJ LITERY W TYM SŁOWIE" )
            
            zycia -= 1
            if zycia < 1:
                koniec_gry = True
    
        for i in range(len(haslo)):
            print(f'{haslo[i]}', end ='')
        print()
    
    
        print(f'\n niepasujące litery = {len(uzyte)} : ', end='')
        for i in range(len(uzyte)):
            print(f'{uzyte[i]},', end='')
    
    
        print('\n pozostałe próby = ', zycia)





zycia = 0

imie = input("Podaj swoje imię: ")
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
        gra(imie, zycia=8, liczba_znakow_od=1, liczba_znakow_do=5)
        break
    elif poziom == ("2"):
        gra(imie, zycia=5, liczba_znakow_od=6, liczba_znakow_do=8)
        break
    elif poziom == ("3"):
        gra(imie, zycia=3, liczba_znakow_od=9, liczba_znakow_do=20)
        break
    else:
       print("zly wybór")
       os.system('cls' if os.name == 'nt' else 'clear')
       if i == 9:
            print('Koniec prób')
            exit()

#gra(zycia)
os.system('cls' if os.name == 'nt' else 'clear')
print(f'{kolory.tlo_czerwony}Koniec gry{kolory.pogrubienie} {imie} przegrałeś!{kolory.reset} {kolory.podkreslenie}\nPozostało ci {zycia} żyć\n{kolory.reset}')



