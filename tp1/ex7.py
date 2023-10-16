nbr1 = float(input("Saisir un nombre: "))
nbr2 = float(input("Saisir un autre nombre: "))
ope = str(input("Saisir une opération (+,-,* ou /): "))
while(ope != '+' and ope != '-' and ope != '*' and ope != '/'):
    ope = str(input("Saisir une opération (+,-,* ou /): "))
    
if(ope == '+'):
    print(f"{nbr1} + {nbr2} = {nbr1+nbr2}")
elif(ope == '-'):
    print(f"{nbr1} - {nbr2} = {nbr1-nbr2}")
elif(ope == '*'):
    print(f"{nbr1} * {nbr2} = {nbr1*nbr2}")
elif(ope == '/'):
    print(f"{nbr1} / {nbr2} = {nbr1/nbr2}")