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
    def setColor(self,new_color):
        self.color = new_color

    def getColor(self):
        return self.color
    
    # malaltia
    def setMalaltia(self, new_malaltia):
        self.malaltia = new_malaltia

    def getMalaltia(self):
        return self.malaltia
    
    # Portes
    def setAlimentPreferit(self, new_alimentPreferit):
        self.alimentPreferit = new_alimentPreferit

    def getAlimentPreferit(self):
        return self.alimentPreferit
    
    # localitzacio
    def setLocalitzacio(self, new_localitzacio):
        self.localitzacio = new_localitzacio

    def getLocalitzacio(self):
        return self.localitzacio
    
    # nom
    def setNom(self, new_nom):
        self.nom = new_nom

    def getNom(self):
        return self.nom