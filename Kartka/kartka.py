# Wygeneruj tablice zawierającą n losowych elementów. Z zakresem min i max. *****[1]*****






import random 

n = 10
my_min = 1
my_max = 100
lista = []

for _ in range(n):
    random_element = random.randint(my_min, my_max)
    lista.append(random_element)
print(lista)










# Napisz program(nie max min) znajdujący max i min wartość. tablica zawiera 1,1,1,5,5,-2,10,1 ******[2]******







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









# Napisz program który powie ile razy powtórzył się n element na tablicy.*****[3]******





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







# Sprawdź ile liczb pierwszych zawiera tablica.******[4]******






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









# Przepisz wszystkie elementy mniejsze od n do 2 tablicy wyświetl tą tablice *******[5]*******
n = int(input("n = "))
tablica1 = [1,2,3,4,7,15,9,24,30]  

tablica2 = []


for element in tablica1:
    if element < n:
        tablica2.append(element)


print("Nowa tablica zawierająca elementy mniejsze od", n, "to:", tablica2)




















# Przyjmij n liczb od użytkownika sprawdź ile z wprowadzonych liczb jest parzystych. Zapisz liczby parzyste na nowej liście. *****[6]*******
#                                                           ********FOR********



n = int(input("Podaj liczbę n: "))
liczby = []
liczby_parzyste = []

for i in range(n):
    liczba = int(input(f"Podaj liczbę {i + 1}: "))
    liczby.append(liczba)

for liczba in liczby:
    if liczba % 2 == 0:
        liczby_parzyste.append(liczba)

print("Wprowadzone liczby:", liczby)
print("Liczby parzyste:", liczby_parzyste)







# Przyjmij n liczb od użytkownika sprawdź ile z wprowadzonych liczb jest parzystych. Zapisz liczby parzyste na nowej liścIE
#                                                          **********WHILE**********





n = int(input("Podaj liczbę n: "))
liczby = []
liczby_parzyste = []

i = 0
while i < n:
    liczba = int(input(f"Podaj liczbę {i + 1}: "))
    liczby.append(liczba)
    i += 1

i = 0
while i < len(liczby):
    if liczby[i] % 2 == 0:
        liczby_parzyste.append(liczby[i])
    i += 1

print("Wprowadzone liczby:", liczby)
print("Liczby parzyste:", liczby_parzyste)