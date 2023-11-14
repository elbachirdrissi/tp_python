def conversion_temps(heures, minutes, secondes):
    return (heures*3600 + minutes*60 + secondes)
def conversion_distance(kilomètre, mètres, centimètres):
    return (kilomètre*1000 + mètres + centimètres*0.01)
def vittese(km, m, cm, heu, min, sec):
    return conversion_distance(km, m, cm) / conversion_temps(heu, min, sec)

'''
print("Saisir la premier horaires")
h1 = int(input("Donner le nombre des heures: "))
m1 = int(input("Donner le nombre des minutes: "))
s1 = int(input("Donner le nombre des secondes: "))
print("Saisir la deuxième horaires")
h2 = int(input("Donner le nombre des heures: "))
m2 = int(input("Donner le nombre des minutes: "))
s2 = int(input("Donner le nombre des secondes: "))
temps_écoulé =  conversion_temps(h2,m2,s2)-conversion_temps(h1,m1,s1)
print(f"Le temps écoulé entre les deux horaires est: {temps_écoulé} secondes")
'''

km = int(input("Donner le nombre des kilomètres: "))
m = int(input("Donner le nombre des mètres: "))
cm = int(input("Donner le nombre des centimètres: "))
heu = int(input("Donner le nombre des heures: "))
min = int(input("Donner le nombre des minutes: "))
sec = int(input("Donner le nombre des secondes: "))
print(f"Votre vittese est: {vittese(km, m, cm, heu, min, sec)} m/s")