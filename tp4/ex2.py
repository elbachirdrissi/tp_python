class Batiment():
    def __init__(self, adr):
        self.__adr = adr
    def get_adr(self):
        return self.__adr
    def set_adr(self,adr):
        self.__adr = adr
    def __str__(self):
        return 'Adresse = {}'.format(self.__adr)
    
class Maison(Batiment):
    def __init__(self, adr, NbrPiec):
        super().__init__(adr)
        self.__NbrPiec = NbrPiec
    def get_NbrPiec(self):
        return self.__NbrPiec
    def set_NbrPiec(self,NbrPiec):
        self.__NbrPiec = NbrPiec
    def __str__(self):
        return super().__str__()+'\nNombre des piéces = {}'.format(self.__NbrPiec)

class Immeuble(Batiment):
    def __init__(self, adr, NbrAppt):
        super().__init__(adr)
        self.__NbrAppt = NbrAppt
    def get_NbrAppt(self):
        return self.__NbrAppt
    def set_NbrAppt(self,NbrAppt):
        self.__NbrAppt = NbrAppt
    def __str__(self):
        return super().__str__()+'\nNombre des appartements = {}'.format(self.__NbrAppt)

choix = int(input("Chosir quelle classe vous voulez tester: \n 1:Batiment \n 2:Maison \n 3:Immeuble \n"))

if(choix == 1):
    bt = Batiment("hay al amal")
    print(bt)
    nouv_adr = input("Donner le nouvelle adresse du batiment: ")
    bt.set_adr(nouv_adr)
    print(f"Après la modification: adresse = {bt.get_adr()}")

elif(choix == 2):
    mais = Maison("azmour",5)
    print(mais)
    nouv_adr = input("Donner le nouvelle adresse du maison: ")
    nouv_nbrPiec = int(input("Donner le nouvelle nombre de piéces du maison: "))
    mais.set_adr(nouv_adr)
    mais.set_NbrPiec(nouv_nbrPiec)
    print(f"Après la modification: \n adresse = {mais.get_adr()} \n Nombre des piéces = {mais.get_NbrPiec()}")

elif(choix == 3):
    ime = Immeuble("targa",30)
    print(ime)
    nouv_adr = input("Donner le nouvelle adresse de l'immeuble: ")
    nouv_nbrApp = int(input("Donner le nouvelle nombre d'appartement: "))
    ime.set_adr(nouv_adr)
    ime.set_NbrAppt(nouv_nbrApp)
    print(f"Après la modification: \n adresse = {ime.get_adr()} \n Nombre des piéces = {ime.get_NbrAppt()}")
