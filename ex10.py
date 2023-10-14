login = input("Saisir votre login: ")
pwd = input("Saisir votre mot de passe: ")
if(login == pwd == 'admin'):
    print("Bienvenue :)")
else:
    print("Erreur ! le login ou le mot de passe sont incorrecte")