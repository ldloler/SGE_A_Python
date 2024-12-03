class cotxe:
    # Constructor
    def __init__(self, marca, model, numPortes, seients, tipus):
        # Atributs
        self.marca = marca
        self.model = model
        self.numPortes = numPortes
        self.seients = seients
        self.tipus = tipus

    # Getters i Setters
    # Marca
    def setMarca(self,new_marca):
        self.marca = new_marca

    def getMarca(self):
        return self.marca
    
    # Model
    def setModel(self, new_model):
        self.model = new_model

    def getModel(self):
        return self.model
    
    # Portes
    def setNumPortes(self, new_numPortes):
        self.numPortes = new_numPortes

    def getNumPortes(self):
        return self.numPortes
    
    # Seients
    def setSeients(self, new_seients):
        self.seients = new_seients

    def getSeients(self):
        return self.seients
    
    # Tipus
    def setTipus(self, new_tipus):
        self.tipus = new_tipus

    def getTipus(self):
        return self.tipus