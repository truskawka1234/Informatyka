


# Napisz funkcję która przyjmuje trzy listy i powie w której z nich znajduje się największa średnia.

def zad1 (lst1,lst2,lst3):
    srednia = lambda lst: sum(lst)/len(lst)
    all_lst = [lst1,lst2,lst3]
    w = []
    for lst in all_lst:
        w.append(srednia(lst))
    return w.index(max(w))
print (zad1([1,2,3,4],[5,6,7,8],[20,21,19]))



# Napisz funkcję która generuje losową listę o wielkości k i zakresie n i m.
from random import randint 
zad2 = lambda k,n,m:[randint(n,m) for i in range (k)]
print (zad2(10,5,20))




# Napisz funkcję która przyjmuje listę i podniesie wszystkie elementy do kwadratu
zad3 = lambda lista: list(map(lambda el: el**2, lista))
print (zad3([2,4,7])) 




# Napisz funkcję która przyjmuje listę i podniesie wszystkie elementy do 1/2
zad4 = lambda lista :list(map(lambda el: el**1/2, lista))
print (zad4([2,4,7,8]))



# Napisz funkcję która przyjmuje listę jako argument w zwróci ile występuje liczb parzystych  
zad5 = lambda lista: len (list(filter(lambda x: x % 2 == 0, lista)))
print(zad5([2,4,6]))