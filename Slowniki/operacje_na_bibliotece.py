import uuid

# -----------------------------------------------------

def legenda() -> None:
    print("==="*20)
    print("0 - wyjdz z programu")
    print("1 - inf o asortymencie")
    print("2 - usun ksiazke ")
    print("3 - dodaj ksiazke")
    print("4 - edytuj ksiazke")
    print("==="*20)

# -----------------------------------------------------

def inf_ksiazka(dc:dict) -> None:
    for k,v in dc.items():
        print(f"{k} --- {v}")

def inf_biblioteka(lst:list) -> None:
    print(f"liczba ksiazek --- {len(lst)}")
    for ksizka in lst:
        print("==="*20)
        inf_ksiazka(ksizka)
        print("==="*20)

# -----------------------------------------------------
def czy_ksiazka_istnieje(lst: list, id_user_inp: str) -> bool:
    for i in range(len(lst)):
        if str(lst[i]["id"]) == id_user_inp:
            return True
    return False

def inex_instniejacej_kisiazki(lst: list, id_user_inp: str) -> int:
    for i in range(len(lst)):
        if str(lst[i]["id"]) == id_user_inp:
            return i
    return -1  

def usun_ksiazke(lst: list) -> None:
    inf_biblioteka(lst)
    print("Enter - zakoncz")
    inp = input("wklej id książki: ")
    if czy_ksiazka_istnieje(lst, inp):
        index = inex_instniejacej_kisiazki(lst, inp)
        if index != -1:
            lst.pop(index)
            print("ksiazka usunieta")
        else:
            print("ksiązka nie istnieje.")
    else:
        print("nie ma książki o takim ID")
# -----------------------------------------------------

def dodaj_tytul()-> str:
    print("podaj tytuł")
    inp = input("podaj tytul: ")
    return inp

def podaj_cene()-> float:
    print("Liczba !!!")
    inp = float(input("Cena: "))  
    return inp

def podaj_liczbe_stron()-> int:
    print("podaj liczbe stron")
    inp = int(input("liczba stron: "))
    return inp

def dodaj_ksiazke(lst: list)-> None:
    ksiazka = {
        "id":uuid.uuid4(),
        "tytul":dodaj_tytul(),
        "cena": podaj_cene(),
        "liczba_stron": podaj_liczbe_stron()
    }
    lst.append(ksiazka)

def edytuj_dane_ksiazki(lst:list) -> None:
    inf_biblioteka(lst)
    print("Enter - zakoncz")
    inp = input("Wklej ID książki: ")
    if czy_ksiazka_istnieje(lst, inp):
        index_ksiazki = inex_instniejacej_kisiazki(lst, inp)
        lst[index_ksiazki]["tytul"] = dodaj_tytul()
        lst[index_ksiazki]["cena"] = podaj_cene()
        lst[index_ksiazki]["liczba_stron"] =podaj_liczbe_stron()
    else:
        print("nie ma książki o takim ID")