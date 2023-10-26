choix = input("Taper 'EM' si vous voulez convertir de l'euro en mad, ou 'ME' si vous voulez convertir de mad en euro: ")
E=[]
S=[]
print("Saisir les valeurs:")
elem = int(input())
while(elem > 0):
    E.append(elem)
    elem = int(input())
if(choix == 'EM' or choix =='em'):
    for i in E:
        i = i*10.86
        S.append(i)
if(choix == 'ME' or choix =='me'):
    for i in E:
        i = i/10.86
        S.append(i)
print(f"Les valeurs saisies apres la convertion sont: {S}")