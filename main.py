import json

from jhamel_A.Car import Car
from jhamel_A.book import book


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

cars_list = [c.to_dict() for c in cars]
books_list = [b.to_dict() for b in books]

data = {"cars":cars_list, "books":books_list}

with open("json_API/data.json",'w') as file:
    json.dump(data, file)