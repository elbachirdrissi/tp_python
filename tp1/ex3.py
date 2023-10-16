distance = float(input("Saisir la distance de parcours en Km: "))
temps = float(input("Saisir le temps de parcours en minute: "))
vitesse = str( distance/temps * 60/1000)
print(f"Votre vitesse est: {vitesse} m/s")