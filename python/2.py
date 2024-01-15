import math
a = float(input("entrer la valeur de a"))
b = float(input("entrer la valeur de a"))
c = float(input("entrer la valeur de a"))
delta = b**2 - 4*a*c
if delta < 0:
    print("pas de solutions")
elif delta == 0:
    x=(-b)/(2*a)
    print("la solutions est:",x)
else:
    x1 = (-b-math.sqrt(delta))/(2*a)
    x2 = (-b+math.sqrt(delta))/(2*a)
    print("on a deux solutions",round(x1,2),round(x2,2))