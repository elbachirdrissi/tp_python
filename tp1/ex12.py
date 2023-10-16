grade = input("Saisir votre grade (A,B,C,D ou E): ")
nbr_heure = int(input("Saisir le nombre d'heure que tu as travaillé: "))

if(grade == 'A'):
        salaire = (nbr_heure * 200) + (1000 * nbr_heure/20)
        print(f"Votre salaire est: {round(salaire,2)} DH")
elif(grade == 'B'):
        salaire = (nbr_heure * 150) + (800 * nbr_heure/20)
        print(f"Votre salaire est: {round(salaire,2)} DH")
elif(grade == 'C'):
        salaire = (nbr_heure * 120) + (500 * nbr_heure/15)
        print(f"Votre salaire est: {round(salaire,2)} DH")
elif(grade == 'D'):
        salaire = (nbr_heure * 100) + (350 * nbr_heure/15)
        print(f"Votre salaire est: {round(salaire,2)} DH")
elif(grade == 'E'):
        salaire = (nbr_heure * 80) + (100 * nbr_heure/10)
        print(f"Votre salaire est: {round(salaire,2)} DH")