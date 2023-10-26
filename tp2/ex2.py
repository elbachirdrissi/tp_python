taille = int(input("Donner la taille du triangle: "))
for i in range(1,taille+1):
    print("*"* i)
print("_______________________")
for i in range(1,taille+1):
    print(str(i) * i)