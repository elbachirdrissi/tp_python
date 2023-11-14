def somme(m,n):
    som = 0
    for i in range(m,n):
        som += i
    return som

a = int(input("Donner le nombre de début: "))
b = int(input("Donner le nombre d'arret: "))
print(f"La somme de {a} à {b} est: {somme(a,b)}")