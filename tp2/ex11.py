L=[]
nbr_elem = int(input("Donner le nombre des elements de votre liste: "))
for i in range(nbr_elem):
    elem = int(input(f"Saisir le nombre n°{i+1}: "))
    L.append(elem)
L.reverse()
print(L)