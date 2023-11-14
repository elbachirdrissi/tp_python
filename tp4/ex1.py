class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
    def get_x(self):
        return self.__x
    def get_y(self):
        return self.__y
    def set_x(self,x):
        self.__x = x
    def set_y(self,y):
        self.__y = y
    def __str__(self):
        return '\n x={} \n y={}'.format(self.__x,self.__y)

class Rectangle(Point):
    def __init__(self, x, y, longeur, largeur):
        super().__init__(x,y)
        self.__longeur = longeur
        self.__largeur = largeur
    def get_longeur(self):
        return self.__longeur
    def get_largeur(self):
        return self.__largeur
    def set_longeur(self,longeur):
        self.__longeur = longeur
    def set_largeur(self,largeur):
        self.__largeur = largeur
    def aire(self):
        return self.__largeur*self.__longeur
    def __str__(self):
        return super().__str__()+'\n largeur={} \n longeur={}'.format(self.__largeur,self.__longeur)

class Parallelepipede(Rectangle):
    def __init__(self, x, y, longeur, largeur, hauteur):
        super().__init__(x, y, longeur, largeur)
        self.__hauteur = hauteur
    def get_hauteur(self):
        return self.__hauteur
    def set_hauteur(self,hauteur):
        self.__hauteur = hauteur
    def aire(self):
        return 2*(super().aire() + self.get_largeur() * self.__hauteur + self.get_longeur() * self.__hauteur)
    def Volume(self):
        return self.get_largeur()*self.get_longeur()*self.get_hauteur()
    def __str__(self):
        return super().__str__() + '\n hauteur={}'.format(self.__hauteur)

choix = int(input("Chosir quelle classe vous voulez tester: \n 1:Point \n 2:Rectangle \n 3:Parallelepipede \n"))
if(choix == 1):
    #Test de la classe point    
    pt = Point(2,4)
    print(pt)
    nouv_x = int(input("Donner le nouvelle valeur de l'abscisse: "))
    nouv_y = int(input("Donner le nouvelle valeur du ordonnee: "))
    pt.set_x(nouv_x)
    pt.set_y(nouv_y)
    print(f"Après la modification: x={pt.get_x()} et y={pt.get_y()}")

elif(choix == 2):
    #Test de la classe Rectangle
    rec = Rectangle(2,4,12,12)
    print(rec)
    nouv_x = int(input("Donner le nouvelle valeur de l'abscisse: "))
    nouv_y = int(input("Donner le nouvelle valeur du ordonnee: "))
    nouv_lon = int(input("Donner le nouvelle longeur: "))
    nouv_lar = int(input("Donner le nouvelle largeur: "))
    rec.set_x(nouv_x)
    rec.set_y(nouv_y)
    rec.set_longeur(nouv_lon)
    rec.set_largeur(nouv_lar)
    print(f"Après la modification: \n x={rec.get_x()} \n y={rec.get_y()} \n longeur={rec.get_longeur()} \n largeur={rec.get_largeur()}")
    print(f"L'aire du rectangle est: {rec.aire()}")

elif(choix == 3):
    #Test de la classe Parallelepipede
    par = Parallelepipede(2,4,12,12,12)
    print(par)
    nouv_x = int(input("Donner le nouvelle valeur de l'abscisse: "))
    nouv_y = int(input("Donner le nouvelle valeur du ordonnee: "))
    nouv_lon = int(input("Donner le nouvelle longeur: "))
    nouv_lar = int(input("Donner le nouvelle largeur: "))
    nouv_hau = int(input("Donner le nouvelle hauteur: "))
    par.set_x(nouv_x)
    par.set_y(nouv_y)
    par.set_longeur(nouv_lon)
    par.set_largeur(nouv_lar)
    par.set_hauteur(nouv_hau)
    print(f"Après la modification: \n x={par.get_x()} \n y={par.get_y()} \n longeur={par.get_longeur()} \n largeur={par.get_largeur()} \n hauteur={par.get_hauteur()}")
    print(f"L'aire de parallelepipede est: {par.aire()} \n Le volume de parallelepipede est: {par.Volume()}")
