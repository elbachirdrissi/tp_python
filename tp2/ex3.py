import random
nbr_aleatoire = random.randint(1,100)
cmpt = 1
print("**** On va jouer a un petit jeu, je vais générer un nombre entre 1 et 100 et tu vas le devinez en 7 essais *****")
nbr_devine = int(input(">>> "))
while(nbr_devine != nbr_aleatoire and cmpt<7):
    cmpt += 1
    if(nbr_devine<1 or nbr_devine>100):
        print(">>> Oups, vous avez saisi un nombre en dehors de l'intervalle")
        nbr_devine = int(input(">>> "))
    elif(nbr_devine < nbr_aleatoire):
        print(">>> Oups, Entrez un nombre plus grand !")
        nbr_devine = int(input(">>> "))
    elif(nbr_devine > nbr_aleatoire):
        print(">>> Oups, Entrez un nombre plus petit !")
        nbr_devine = int(input(">>> "))
if(nbr_devine == nbr_aleatoire):
    print(f">>> Bravo {nbr_aleatoire} est le nombre que j'ai choisit \nVous l'avez deviné {cmpt} essais")
else:
    print(f"J'ai gagné, je suis le meilleur,\nLe nombre que j'ai devine est {nbr_aleatoire}\nAu revoir !")
