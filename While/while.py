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
