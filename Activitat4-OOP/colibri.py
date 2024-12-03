class colibri:
    # Constructor
    def __init__(self, nom, color, localitzacio, alimentPreferit, malaltia):
        # Atributs
        self.color = color
        self.malaltia = malaltia
        self.alimentPreferit = alimentPreferit
        self.localitzacio = localitzacio
        self.nom = nom

    # Getters i Setters
    # color
    def setcolor(self,new_color):
        self.color = new_color

    def getcolor(self):
        return self.color
    
    # malaltia
    def setmalaltia(self, new_malaltia):
        self.malaltia = new_malaltia

    def getmalaltia(self):
        return self.malaltia
    
    # Portes
    def setalimentPreferit(self, new_alimentPreferit):
        self.alimentPreferit = new_alimentPreferit

    def getalimentPreferit(self):
        return self.alimentPreferit
    
    # localitzacio
    def setlocalitzacio(self, new_localitzacio):
        self.localitzacio = new_localitzacio

    def getlocalitzacio(self):
        return self.localitzacio
    
    # nom
    def setnom(self, new_nom):
        self.nom = new_nom

    def getnom(self):
        return self.nom