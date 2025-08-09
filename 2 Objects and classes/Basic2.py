class Library(object):
    def __init__(self):
        self.name = "Brian'Library"
        self.book_name = ["Bible", "Diary", "Journal"]
    
    def display_books(self):
        print("The books are", self.book_name)
        
    def add_book(self, book_name):  # add_book is a method and not the list
        self.book_name.append(book_name) # book_name is the actual list
        print("Added", book_name)
        
    def borrow_book(self, book_name):
        if book_name in self.book_name:
            self.book_name.remove(book_name)
            print("Removed", book_name)
        else:
            print("Book not available in the list")
        
    def return_book(self, book_name):
        self.book_name.append(book_name)
        print("Returned", book_name) 
        
        
my_Library = Library()

my_Library.display_books( )
my_Library.add_book("Python 101")
my_Library.borrow_book("Laptop")
my_Library.return_book("Bible")