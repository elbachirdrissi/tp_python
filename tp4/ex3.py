class Employee():
    def __init__(self, nom, prenom):
        self.__nom = nom
        self.__prenom = prenom
    def getNom(self):
        return self.__nom
    def getPrenom(self):
        return self.__prenom
    def setNom(self, nom):
        self.__nom = nom
    def setPrenom(self, prenom):
        self.__prenom = prenom
    def __str__(self):
        return 'Nom: {}\nPrenom: {}\n'.format(self.__nom, self.__prenom)
    def gains(self):
        pass

class Patron(Employee):
    def __init__(self, nom, prenom, salaire):
        super().__init__(nom, prenom)
        self.__salaire = salaire
    def getSalaire(self):
        return self.__salaire
    def setSalaire(self, salaire):
        self.__salaire = salaire
    def __str__(self):
        return super().__str__()+'Salaire: {}\n'.format(self.__salaire)
    def gains(self):
        return self.__salaire
    
class TravailleurCommision(Employee):
    def __init__(self, nom, prenom, salaire, commission, quantite):
        super().__init__(nom, prenom)
        self.__salaire = salaire
        self.__commission = commission
        self.__quantite = quantite
    def getSalaire(self):
        return self.__salaire
    def getCommission(self):
        return self.__commission
    def getQuantite(self):
        return self.__quantite
    def setSalaire(self, salaire):
        self.__salaire = salaire
    def setCommission(self, commission):
        self.__commission = commission
    def setQuantite(self, quantite):
        self.__quantite = quantite
    def __str__(self):
        return super().__str__()+'Salaire de base: {}\nCommission: {}\nQuantité: {}\n'.format(self.__salaire, self.__commission, self.__quantite)
    def gains(self):
        return self.__salaire + (self.__quantite * self.__commission)
    
class TravailleurHoraire(Employee):
    def __init__(self, nom, prenom, retribution, heures):
        super().__init__(nom, prenom)
        self.__retribution = retribution
        self.__heures = heures
    def getRetribution(self):
        return self.__retribution
    def getHeures(self):
        return self.__heures
    def setRetribution(self, retribution):
        self.__retribution = retribution
    def setHeures(self, heures):
        self.__heures = heures
    def __str__(self):
        return super().__str__()+'Retribution horaire: {}\nHeures de travail par mois: {}\n'.format(self.__retribution, self.__heures)
    def gains(self):
        return self.__retribution * self.__heures

choix = int(input("Chosir quelle classe vous voulez tester: \n 1:Patron \n 2:TravailleurCommision \n 3:TravailleurHoraire \n"))
if(choix == 1):
    patron = Patron('drissi','elbachir',9000)
    print(patron)
    nouv_nom = input("Donner le nouveau nom de patron: ")
    nouv_prenom = input("Donner le nouveau prénom de patron: ")
    nouv_salaire = float(input("Donner le nouveau salaire de patron: "))
    patron.setNom(nouv_nom)
    patron.setPrenom(nouv_prenom)
    patron.setSalaire(nouv_salaire)
    print(f"Après la modofocation: \nNom: {patron.getNom()} \nPrénom: {patron.getPrenom()} \nSalaire: {patron.gains()}")

elif(choix == 2):
    trvCommission = TravailleurCommision('raho','soufiane',9000,8,20)
    print(trvCommission)
    nouv_nom = input("Donner le nouveau nom de travailleur par commision: ")
    nouv_prenom = input("Donner le nouveau prénom de travailleur par commision: ")
    nouv_salaire = float(input("Donner le nouveau salaire de base: "))
    nouv_comission = float(input("Donner le nouveau montant de la commission: "))
    nouv_quantite = int(input("Donner la nouvelle quantite: "))
    trvCommission.setNom(nouv_nom)
    trvCommission.setPrenom(nouv_prenom)
    trvCommission.setSalaire(nouv_salaire)
    trvCommission.setCommission(nouv_comission)
    trvCommission.setQuantite(nouv_quantite)
    print(f"Après la modification: \nNom: {trvCommission.getNom()} \nPrénom: {trvCommission.getPrenom()} \nSalaire: {trvCommission.gains()} ")

elif(choix == 3):
    trvhor = TravailleurHoraire('khrisi','brahim',150,120)
    print(trvhor)
    nouv_nom = input("Donner le nouveau nom de travailleur horaire: ")
    nouv_prenom = input("Donner le prénom de travailleur horaire: ")
    nouv_retribution = float(input("Donner la noubelle retribution horaire: "))
    nouv_heures = int(input("Donner le nombre d'heures travaillé: "))
    trvhor.setNom(nouv_nom)
    trvhor.setPrenom(nouv_prenom)
    trvhor.setRetribution(nouv_retribution)
    trvhor.setHeures(nouv_heures)
    print(f"Après la modification: \nNom: {trvhor.getNom()} \nPrénom: {trvhor.getPrenom()} \nSalaire: {trvhor.gains()}")
