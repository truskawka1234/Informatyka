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