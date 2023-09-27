print ("A: pwadrat ")
print ("B: prostokat")
print ("C: trojkot")
print ("D: trojkot rownoboczny")
print ("E: romb")
print ("F: romb dwa")
print ("G: kolo ")
print ("H: trapez ")
print ("I: rownoleglobok")

co = input ("co mam zrobic: ")
if co == ("A"):
    a = float (input ("a ="))
    P = (a**2)
    print (f"P = {P}")
elif co== ("B"):
    a= float(input("a = "))
    b= float(input("b = "))
    P= (a*b)
    print (f"P = {P}")
elif co==("C"):
    a= float(input("a = "))
    h= float(input("h="))
    P= ((a*h)/2)
    print(f"P = {P}")
elif co==("D"):
    import math 
    a= float(input("a="))
    P= (math.sqrt(3)/4)*(a**2)
    print(f"P = {P}")
elif co== ("E"):
    a= float (input ("a="))
    h= float (input ("h="))
    P= (a*h)
    print (f"P = {P}")
elif co== ("F"):
    e= float (input ("e="))
    f= float (input ("f="))
    P= ((e*f)/2)
    print (f"P = {P}")
elif co== ("G"):
    import math
    r = float(input ("r="))
    P = (math.pi)* (r**2)
    print(f"P = {P}")
elif co== ("H"):
    a = float(input("a="))
    b = float(input("b="))
    h = float(input("h="))
    P= ((a+b)*h /2 )
    print(f"P = {P}")
elif co== ("I"):
    a = float (input ("a ="))
    h = float (input ("h ="))
    P = (a*h)
    print (f"P = {P}")











    