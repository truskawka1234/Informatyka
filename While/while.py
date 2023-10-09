# wypisz n razy kocham programowac
n = int(input())
while n > 0:
    print("kocham programowac")
    n -= 1





#Zsumuj wszystkie liczby ktore są są podzielne przez 5 do wartości podanej przez użytkownika. 

x = int(input("x = "))
dzielnik_1 = int(input("dzielnik_1 = "))
dzielnik_2 = int(input("dzielnik_2 = "))
suma = 0 
suma_liczb = 0
while 0 <= x:
    if x % dzielnik_1 == 0 and x % dzielnik_2 == 0:
        suma +=1 
        suma_liczb = suma_liczb + x 
    x -= 1 
print ("tyle jest liczb" , suma )
print ("suma_liczb" , suma_liczb )






#Napisz program który wyświetli n potęg liczby 2.

n = int(input(" n = "))
while 0 <= n:
    print(2**n)
    n-=1






#Napisz program który z wypisze wszystkie liczby które NIE są podzielne przez 3.  Do wartości podanej przez użytkownika. 
x = int(input("x = "))
while 0 <= x :
    if x % 3 != 0:
        print (x)
    x -= 1 







#Napiszmy program który wyświetli nam wszystkie liczby podzielne przez 9. Do wartości podanej przez użytkownika.
x = int(input("x = "))
while 0 <= x :
    if x % 9 == 0:
        print(x)
    x -= 1 

# Utwórz pustą listę o nazwie "numbers".
numbers = [1,2,3,4,5]

# # Poproś użytkownika o podanie 5 liczb i dodaj je do listy.

i = 0 
while i < 5:
    x = int(input())
    numbers.append(x)
    i += 1
print(numbers)

# # Oblicz sumę liczb znajdujących się w liście "numbers".

i = 0
suma = 0
while i < len(numbers):
    suma += numbers[i]
    i += 1

print(suma)

# #Znajdź największą liczbę w liście "numbers"

i = 0 
my_max = (numbers)[0]
while i < len(numbers):
    if my_max < numbers[i]:
        my_max = numbers[i]
    i += 1
print(my_max)

# # Znajdź najmniejszą liczbę w liście "numbers

i = 0
my_min = (numbers)[0]
while i > len(numbers):
    if my_min < numbers[i]:
        my_min = numbers[i]
    i += 1
print(my_min)

# #Znajdź średnią arytmetyczną liczb w liście "numbers".

i = 0
suma = 0
while i < len(numbers):
    suma += numbers[i]
    i += 1

print(suma/len(numbers))

# # Znajdź ilość liczb parzystych w liście "numbers".

i = 0
ile = 0
while i < len(numbers):
    if numbers[i] % 2 == 0:
        ile += 1
    i += 1    
print(ile)

# # Stwórz nową listę o nazwie "duplicates" zawierającą powtarzające się elementy z listy "numbers".

numbers = [1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10]
duplicate = []
i = 0 
while i < len(numbers):
    if numbers.count(numbers[i]) > 1 and numbers[i] not in duplicate:
        duplicate.append(numbers[i])
    i += 1
print (duplicate)

# # Usuń wszystkie powtarzające się elementy z listy "numbers".


numbers = [1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10]
new_list = []
i = 0 
while i < len(numbers):
    if numbers[i] not in new_list:
        new_list.append(numbers[i])
    i += 1
numbers = new_list
print(new_list)

# # Stwórz nową listę o nazwie "squares" zawierającą kwadraty liczb z listy "numbers".



numbers = [1,2,3,4,5]
squares = []
i = 0
while i < len(numbers):
    squares.append(numbers[i]**2)
    i += 1
print(squares)