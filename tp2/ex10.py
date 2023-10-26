L1=[]
L2=[]
L3=[]
nbr_elem = int(input("Donner le nombre des elements: "))
print('Veuillez remplir la premier liste: ')
for i in range(nbr_elem):
    elem = int(input(f"Saisir le nombre n°{i+1}: "))
    L1.append(elem)
print('Veuillez remplir la deuxième liste: ')
for i in range(nbr_elem):
    elem = int(input(f"Saisir le nombre n°{i+1}: "))
    L2.append(elem)
E1 = set(L1)
E2 = set(L2)
E3 = E1 & E2
L3 = list(E3)
print(f"L'intersection des deux listes est: {L3}")