pois = float(input("Saisir votre poids (en Kg): "))
taille = float(input("Saisir votre taile (en m): "))
imc = pois / taille
if(imc >= 40):
    print("obésité morbide ou massive")
elif(35<=imc and imc<40):
    print("obésité sévère")
elif(30<=imc and imc<35):
    print("obésité modérée")
elif(25<=imc and imc<30):
    print("Surpoids")
elif(18.5<=imc and imc<25):
    print("corpulence normale")
elif(16.5<=imc and imc<18.5):
    print("Maigreur")
elif(imc < 16.5):
    print("Famine")