nom_1 = input("Donner le nom du 1er article: ")
qte_1 = int(input("Donner la quantité du 1er article: "))
prix_1 = float(input("Donner le prix unitaire du 1er article: "))

nom_2 = input("Donner le nom du 2eme article: ")
qte_2 = int(input("Donner la quantité du 2eme article: "))
prix_2 = float(input("Donner le prix unitaire du 2eme article: "))

total_1 = qte_1*prix_1
total_2 = qte_2*prix_2
print(f"Total pour l'article {nom_1}: {total_1} dh (HT)")
print(f"Total pour l'article {nom_2}: {total_2} dh (HT)")

total = (total_1 + total_1*0.2) + (total_2 + total_2*0.2)
print(f"Le total de votre facture est: {total} dh (TTC)")