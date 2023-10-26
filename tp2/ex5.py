L=[]
nbr_elem = int(input("Donner le nombre des elements de votre liste: "))
for i in range(nbr_elem):
    elem = int(input(f"Saisir le nombre n°{i+1}: "))
    L.append(elem)
print(L)
val_ajoute = int(input("Saisir la valeur a ajouter: "))
L.append(val_ajoute)
L.sort()
print(L)