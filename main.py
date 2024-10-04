from book import Book
from library import Library

counter = 0

#>Bienvenido: Que operacion desea realizar?
    #Agregar - Agrega un libro a la bilioteca
    #Listar - Lista los libros
    #Buscar - Busca un libro
    #Borrar - Borra un libro de la biblioteca


#Agregar - Agrega un libro a la bilioteca
def add_book_to_library():
    book_id = int( input('Ingrese un id: ') )
    
    book_title = input('Ingrese el nombre del libro: ')
    
    book_autor = input('Autor: ')
    
    book_release = int(input('Año de publicacion: '))

    new_book = Book(book_id, book_title, book_autor, book_release)

    library.add(book_id = book_id, book = new_book)


#Borrar - Borra un libro de la biblioteca
def delete_book_of_library():
    book_id_delete = int( input('Ingrese el id del libro que desea borrar: ') )
    
    print(f'El libro se ha borrado con exito libro id: {book_id_delete}')
    library.delete(book_id_delete)


#Listar - Lista los libros
def list_library_books():
    print(f'Lista de libros {library.list_books}') 


#Buscar - Busca un libro
def search_book_in_library():
    book_title_search = input('Ingrese el titulo del libro que desea buscar: ')
    for book in library.list_books:
        if book_title_search == library.list_books[book][0]:
            print(library.list_books[book])
        else:
            print('No se encontró un libro con esa id')


library = Library()



def main_function():
    quit = True
    while quit :
        command = input("Que desea hacer? Escribe 'ayuda' para obtener la lista de comandos: ").lower()
        match command:
            case 'agregar':
                add_book_to_library()
            case 'listar':
                list_library_books()
            case 'buscar':
                search_book_in_library()
            case 'borrar':
                delete_book_of_library()
            case 'borrar':
                quit = False
            case 'ayuda':
                print(""" 
    #Agregar - Agrega un libro a la bilioteca
    #Listar - Lista los libros
    #Buscar - Busca un libro
    #Borrar - Borra un libro de la biblioteca
    #Salir - Para salir del programa
 """)
                
main_function()






