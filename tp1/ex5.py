nbr = int(input("saisir un nombre: "))
if(nbr%2==0):
    print("Ce nombre est pair")
elif(nbr%3==0):
    print("Ce nombre est impair, mais il est multiple de 3")
else:
    print("Ce nombre ni pair ni multiple de 3")