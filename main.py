import json

#Imports de les classes del Jhamel_A
from jhamel_A.Car import Car
from jhamel_A.book import book

#Imports de les classes del Roc_B
from roc_B.Cat import Cat
from roc_B.School import School

#Guardem les instàncies de les classes en les seves llistes corresponents

#Instàncies del Jhamel_A
cars = [
    Car('Toyota', 'Camry', '2019', '20000'),
    Car('Ford', 'Mustang', '2021', '35000'),
    Car('Honda', 'Civic', '2018', '18000'),
    Car('Chevrolet', 'Corvette', '2022', '65000'),
    Car('Tesla', 'Model 3', '2020', '45000')
]

books = [
    book("Cien años de soledad", "Gabriel García Márquez", 1967, "Editorial Sudamericana", "Español", 20),
    book("The Great Gatsby", "F. Scott Fitzgerald", 1925, "Scribner's", "Inglés", 15),
    book("El Código Da Vinci", "Dan Brown", 2003, "Doubleday", "Español", 25),
    book("To Kill a Mockingbird", "Harper Lee", 1960, "J. B. Lippincott & Co.", "Inglés", 18),
    book("El Hobbit", "J. R. R. Tolkien", 1937, "George Allen & Unwin Ltd.", "Español", 22)
]

#Instàncies del Roc_B
cats = [
    Cat("Siamès", 3.5, "blanc", "mascle"),
    Cat("Persa", 4.0, "negre", "femella"),
    Cat("Maine Coon", 5.2, "gris", "mascle"),
    Cat("Azul ruso", 5.2, "gris", "femella"),
    Cat("Serval", 6.1, "atigrat", "mascle")
]

schools = [
    School(500, 20, 1000, True, "Barcelona", ["ESO", "Batxillerat"]),
    School(300, 12, 800, False, "Girona", ["ESO"]),
    School(700, 30, 1500, True, "Tarragona", ["ESO", "Batxillerat", "CFGS"]),
    School(400, 18, 900, False, "Lleida", ["ESO", "Batxillerat"]),
    School(550, 25, 1200, True, "Figueres", ["ESO", "Batxillerat"])
]

#Passem les instàncies de les llistes a format diccionari

#Llistes del Jhamel_A
cars_list = [c.to_dict() for c in cars]
books_list = [b.to_dict() for b in books]

#Llistes del Roc_B
cats_list = [c.to_dict() for c in cats]
schools_list = [s.to_dict() for s in schools]

#Encapsulem les 4 llistes en un objecte contenidor
data = {"cars":cars_list, "books":books_list, "cats":cats_list, "schools":schools_list}

#Guardem l'objecte contenidor en un fitxer 
with open("json_API/data.json",'w') as file:
    json.dump(data, file)