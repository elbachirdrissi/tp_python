nbr_article = int(input("Combien d'article vous avez ? "))
liste_nom = []
liste_qte = []
liste_prix = []
total_ht = []
total_ttc = []
som_ttc = 0

for i in range(nbr_article):
    nom = input(f"Donner le nom de l'article {i+1}: ")
    liste_nom.append(nom)
    qte = int(input(f"Donner la quantité de l'article {i+1}: "))
    liste_qte.append(qte)
    prix = float(input(f"Donner le prix unitaire de l'article {i+1}: "))
    liste_prix.append(prix)
    total = prix * qte
    total_ht.append(total)
    ttc = total + total*0.2
    total_ttc.append(ttc)
   
for prix in total_ht:
    print(f"Total pour l'article {i+1}: {prix} dh (HT)")

for i in total_ttc:
    som_ttc += i

print(f"Le total de votre facture est:: {som_ttc} dh (TTC)")