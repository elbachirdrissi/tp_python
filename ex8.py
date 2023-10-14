nbr_note = int(input("Saisir le nombre des notes que vous avez: "))
som = som_coeff = 0 

for i in range(nbr_note):
    note = float(input(f"Note {i+1}: "))
    coeff = int(input(f"Coefficient de la note {i+1}: "))
    som_coeff += coeff
    som += note*coeff

moy = som/som_coeff
print(f"Moyenne de ces {nbr_note} notes: {moy}")

if(moy<7):
    print("Non Validé")
elif(moy>7 and moy<10):
    print("Rattrapage")
else:
    print("Semetre validé")