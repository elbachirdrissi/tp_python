nbr_article = int(input("Combien d'article vous avez ? "))
liste_nom = []
liste_qte = []
liste_prix = []
liste_total = []

for i in range(nbr_article):
    nom = input(f"Donner le nom de l'article {i+1}: ")
    liste_nom.append(nom)
    qte = int(input(f"Donner la quantité de l'article {i+1}: "))
    liste_qte.append(qte)
    prix = float(input(f"Donner le prix unitaire de l'article {i+1}: "))
    liste_prix.append(prix)
    total = prix * qte
    liste_total.append(total)
   
for prix in liste_total:
    print(f"Total pour l'article {i+1}: {prix} dh (HT)")


'''total = (total_1 + total_1*0.2) + (total_2 + total_2*0.2)
print(f"Le total de votre facture est: {total} dh (TTC)")'''