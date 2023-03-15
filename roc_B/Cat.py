class Cat:
    
    # Constructor de la classe
    def __init__(self, raza, peso, color, sexo):
        self.raza = raza
        self.peso = peso 
        self.color = color
        self.sexo = sexo

    # Mètode que mostra per pantalla les dades de la classe
    def info(self):
        print("Dades del gat:")
        print(f"Raça: {self.raza}")
        print(f"Pes: {self.peso}")
        print(f"Color: {self.color}m2")
        print(f"Sexe: {self.sexo}")
    
    #Mètode que ens retorna els atributs d'una instància en format de diccionari
    def to_dict(self):
        return {
            "raza": self.raza,
            "peso": self.peso,
            "color": self.color,
            "sexo": self.sexo
        }
    
    # Getters i Setters per als atributs de la classe Cat
    def getRaza(self):
        return self.raza
    
    def setRaza(self, raza):
        self.raza = raza
        
    def getPeso(self):
        return self.peso
    
    def setPeso(self, peso):
        self.peso = peso
        
    def getColor(self):
        return self.color
    
    def setColor(self, color):
        self.color = color
        
    def getSexo(self):
        return self.sexo
    
    def setSexo(self, sexo):
        self.sexo = sexo