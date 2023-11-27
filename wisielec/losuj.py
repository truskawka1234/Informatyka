import random


def losuj_slowo():
    
    with open('slowa.txt', encoding="utf-8") as dane_z_pliku:
        slowa = dane_z_pliku.read().splitlines()

    slowo = random.choice(slowa)
    return(slowo)


#
def main():
    print(losuj_slowo())

if __name__ == "__main__":
    main()