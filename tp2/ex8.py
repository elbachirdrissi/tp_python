L=[]
M=[]
cmpt = 0
nbr_elem = int(input("Donner le nombre des elements de votre liste: "))
for i in range(nbr_elem):
    elem = int(input(f"Saisir le nombre n°{i+1}: "))
    L.append(elem)
print(L)
nbr_cherche = int(input("Donner le nombre a chercher: "))
for i, val in enumerate(L):
    if(val==nbr_cherche):
        cmpt +=1
        M.append(i)
print(f"{nbr_cherche} est répété dans la liste {cmpt} fois")
print(f"Les indices des répititions sont: {M}")