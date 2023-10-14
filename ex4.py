nbr_seconde = int(input("Entrez un nombre de secondes : "))
ancien_nbr_sec = nbr_seconde

heures = nbr_seconde // 3600
nbr_seconde %= 3600
minutes = nbr_seconde // 60
secondes = nbr_seconde % 60

print(f"{ancien_nbr_sec} secondes = {heures}h {minutes}min {secondes}sec")