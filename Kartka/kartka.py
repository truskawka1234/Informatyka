# Wygeneruj tablice zawierającą n losowych elementów. Z zakresem min i max. 

import random 

n = 10
my_min = 1
my_max = 100
lista = []

for _ in range(n):
    random_element = random.randint(my_min, my_max)
    lista.append(random_element)
print(lista)










# Napisz program(nie max min) znajdujący max i min wartość. tablica zawiera 1,1,1,5,5,-2,10,1

lista = [1,1,1,5,5,-2,10,1]


my_min = (lista[0])
my_max = (lista[0])

for el in lista:
    if el > my_max:
        my_max = el 
    if el < my_min:
        my_min = el
print("my_max =", my_max)

print("my_min =", my_min)






# Napisz program który powie ile razy powtórzył się n element na tablicy. 


import random

n = 20  
min_value = 1  
max_value = 10  

random_list = [random.randint(min_value, max_value) for _ in range(n)]


random_element = random.choice(random_list)


count = random_list.count(random_element)


print("Losowa tablica:", random_list)
print(f"Losowy element: {random_element}")
print(f"Liczba wystąpień losowego elementu: {count}")



# Sprawdź ile liczb pierwszych zawiera tablica.
tablica = [1, 2, 3, 4, 5, 6, 7, 8, 9]
liczby_pierwsze = []
indeks = 0

while indeks < len(tablica):
    liczba = tablica[indeks]
    if liczba > 1:
        jest_pierwsza = True
        for i in range(2, liczba):
            if liczba % i == 0:
                jest_pierwsza = False
                break
        if jest_pierwsza:
            liczby_pierwsze.append(liczba)
    indeks += 1

print("Liczby pierwsze w tablicy:", liczby_pierwsze)
print("Ilość liczb pierwszych:", len(liczby_pierwsze))