import math as m

def delta():
    global a,b,c
    return pow(b,2)-4*a*c

def NombreRacine():
    if(delta() < 0):
        return 0
    elif(delta() == 0):
            return 1
    elif(delta() > 0):
        return 2
    
def Racine1():
     if(NombreRacine() == 1):
          return (-b/2*a)
     if(NombreRacine() == 2):
          return ( -b + m.sqrt(delta()) )/2*a

def Racine2():
     if(NombreRacine() == 2):
          return ( -b - m.sqrt(delta()) )/2*a
     
a = int(input("Donner le coefficient a: "))
b = int(input("Donner le coefficient b: "))
c = int(input("Donner le coefficient c: "))
print(f"Votre équation est: {a}x²+{b}x+{c} = 0")

if(NombreRacine() == 0):
     print("L'équation n'admet pas de solution dans l'ensemble R")
elif(NombreRacine() == 1):
     print(f"La solution de votre équation est: {Racine1()}")
else:
     print(f"Les solutions de votre équation sont: {Racine1()} et {Racine2()}")