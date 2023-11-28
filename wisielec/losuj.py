import random


def losuj_slowo(liczba_znakow_od=1, liczba_znakow_do=10):
    
    with open('slowa.txt', encoding="utf-8") as dane_z_pliku:
        slowa = dane_z_pliku.read().splitlines()

    slowo = random.choice(slowa)
    while True:
        if len(slowo) in range(liczba_znakow_od, liczba_znakow_do):
            break
        else: 
            slowo = slowo = random.choice(slowa)
            continue
    return(slowo)

def losuj_slowo_ekstremalne():
    
    with open('slowa_ekstremalne.txt', encoding="utf-8") as dane_z_pliku:
        slowa = dane_z_pliku.read().splitlines()

    slowo = random.choice(slowa)
    return(slowo)



def main():
    print(losuj_slowo())

if __name__ == "__main__":
    main()