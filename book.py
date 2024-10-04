import random

# books = {}

class Book:
    def __init__(self, id, title, autor, release):
        self.id = id
        # self.id = random.randint(1,99999)
        self.title = title
        self.autor = autor
        self.release = release

    
    @property
    def get_info(self):
        return self.title, self.autor, self.release
    
#Inicializar la clase Book con valores
# book1 = Book('Juan Salvador Gaviota', 'Richard Bach', 1970)

#Guardar libros en el diccionario
# books.update({book1.id : book1.get_info})

# print(books)

