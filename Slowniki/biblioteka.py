import uuid
import random
# -----------------------------------------------------
biblioteka = [] # <---

def dodaj_testowe_slowniki(lst:biblioteka) -> None:
    ksiazka = {
        "id":uuid.uuid4(),
        "tytul":"...",
        "cena": random.randint(30,100),
        "liczba_stron": random.randint(100,300)
    }
    biblioteka.append(ksiazka)

# -----------------------------------------------------
dodaj_testowe_slowniki(biblioteka)
dodaj_testowe_slowniki(biblioteka)
dodaj_testowe_slowniki(biblioteka)