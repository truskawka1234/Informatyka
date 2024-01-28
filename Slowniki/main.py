from biblioteka import biblioteka # <--- 1
import operacje_na_bibliotece
import os

def main() -> None:
    while True:
        operacje_na_bibliotece.legenda()
        inp = int(input("--->\t"))
        
        if inp == 0:
            
            z = "program zakonczyl dzialanie"
            print("\n"*5)
            print(f"\t {z.upper()}")
            print("\n"*5)
            break
        elif inp == 1:
            operacje_na_bibliotece.inf_biblioteka(biblioteka)
        elif inp == 2:
            operacje_na_bibliotece.usun_ksiazke(biblioteka)
        elif inp == 3:
            operacje_na_bibliotece.dodaj_ksiazke(biblioteka)
        elif inp == 4:
            operacje_na_bibliotece.edytuj_dane_ksiazki(biblioteka)
        else:
            print("Nie ma takiej operacji ") 

# -----------------------------------------------------
if __name__ == "__main__":
    main()
