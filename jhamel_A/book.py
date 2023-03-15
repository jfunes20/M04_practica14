"""Este codigo define una clase que representa un libro, permite ver y modificar
sus atribitus mediante getters y setters y muestra la informacion atraves de un metodo info
y tiene una funcion que lo pasa a diccionario.
"""
class book:
    def __init__(self, titulo, autor, fecha, editor, idioma, precio):
        self.titulo = titulo
        self.autor = autor
        self.fecha = fecha
        self.editor = editor
        self.idioma = idioma
        self.precio = precio

    def getTitulo(self):
        return self.titulo
    def setTitulo(self, titulo):
        self.titulo = titulo
    def getAutor(self):
        return self.autor
    def setAutor(self, autor):
        self.autor = autor
    def getFecha(self):
        return self.fecha
    def setFecha(self, fecha):
        self.fecha = fecha
    def getEditor(self):
        return self.editor
    def setEditor(self, editor):
        self.editor = editor
    def getIdioma(self):
        return self.idioma
    def setIdioma(self, idioma):
        self.idioma = idioma
    def getPrecio(self):
        return self.precio
    def setPrecio(self, precio):
        self.precio = precio

    def info(self):
        print("Titulo: " + self.titulo)
        print("Autor: " + self.autor)
        print("Fecha de salida: " + self.fecha)
        print("Editor: " + self.editor)
        print("Idioma: " + self.idioma)
        print("Precio: " + self.precio + "\n")

    def to_dict(self):
        return{
            "titulo":self.titulo,
            "autor":self.autor,
            "fecha":self.fecha,
            "editor":self.editor,
            "idoma":self.idioma,
            "precio":self.precio
        }

