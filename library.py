class Library:
    
    def __init__(self):
        self.list_of_books = {}


    def add (self, book_id, book):
        self.list_of_books.update({book_id : book.get_info})


    @property
    def list_books(self):
        return self.list_of_books


    def delete(self, book_id):
        self.list_of_books.pop(book_id, None)
