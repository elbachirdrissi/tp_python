nbr1 = int(input("Saisir le premier nombre: "))
nbr2 = int(input("Saisir la deuxième nombre: "))
if( (nbr1>0 and nbr2>0 ) or (nbr1<0 and nbr2<0)):
    print("le produit des deux nombres est positif")
else:
    print("le produit des deux nombres est négatif")