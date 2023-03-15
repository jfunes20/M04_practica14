"""Este codigo define una clase que representa un coche, permite ver y modificar
sus atribitus mediante getters y setters y muestra la informacion atraves de un metodo info y tiene una funcion que lo pasa a diccionario.
"""
class Car:
    def __init__(self, marca, modelo, año, precio):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.precio = precio

    def getMarca(self):
        return self.marca
    def setMarca(self, marca):
        self.marca = marca
    def getModelo(self):
        return self.modelo
    def setModelo(self, modelo):
        self.modelo = modelo
    def getAño(self):
        return self.año
    def setAño(self, año):
        self.año = año
    def getPrecio(self):
        return self.precio
    def setPrecio(self, precio):
        self.precio = precio

    def info(self):
        print("Marca: " + self.marca)
        print("Modelo: " + self.modelo)
        print("Año salida: " + self.año)
        print("Precio: " + self.precio)

    def to_dict(self):
        return{
            "marca":self.marca,
            "modelo":self.modelo,
            "año":self.año,
            "precio":self.precio
        }

