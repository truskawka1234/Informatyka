import math
def czy_to_liczba_pierwsza(liczba):
    if liczba < 2:
        return False
    if liczba == 2:
        return True 
    if liczba % 2 == 0:
        return False  
    i = 3
    while math.sqrt(liczba) >= i:
        if liczba % i == 0:
            return False
        i += 1
    return True


print (czy_to_liczba_pierwsza(1))
print (czy_to_liczba_pierwsza(2))
print (czy_to_liczba_pierwsza(3))
print (czy_to_liczba_pierwsza(4))
print (czy_to_liczba_pierwsza(5))
print (czy_to_liczba_pierwsza(6))
print (czy_to_liczba_pierwsza(7))
print (czy_to_liczba_pierwsza(8))
print (czy_to_liczba_pierwsza(9))

# ---------------------------------------
liczby = [-3,-2,-1,0,1,2,3,4,5,6,7,]

def spr_czy_pierwsza(lst):
    for el in lst:
        print(f"{el} --- {czy_to_liczba_pierwsza(el)}")

spr_czy_pierwsza(liczby)