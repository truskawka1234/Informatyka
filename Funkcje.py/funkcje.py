#  stworz kalkulator 4 figur przestrzennych




import math 
def pole_kola(r):
    return math.pi*r**2

def pole_szescianu(a):
    return 6*a**2

def objetosc_prst(a,b,c):
    return a*b*c

def objetosc_szescianu(a):
    return a**3



while True:
    inp = input()
    if inp == "stop":
        break
    elif inp == "a":
        r = float(input("r = "))
        print(pole_kola(r))
    elif inp == "b":
        a = float(input("a = "))
        print(pole_szescianu(a))
    elif inp == "c":
        a = float(input("a = "))
        b = float(input("b = "))
        c = float(input("c = "))
        print(objetosc_prst(a,b,c))
    elif inp == "d":
        a = float(input("a = "))
        print(objetosc_szescianu(a))
    
    else:
        print("nie ma takiej komendy!!!")