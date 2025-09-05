""""
Description: A client program written to verify correctness of 
the activity classes.
"""
__author__ = "ACE Faculty, Tri Tranvo"
__version__ = "1.0.0"
__credits__ = ""

from genre.genre import Genre
from library_item.library_item import LibraryItem

def main():
    """Test the functionality of the methods encapsulated 
    in this project.
    """ 
    # In the statements coded below, ensure that any statement that could result 
    # in an exception is handled.  When exceptions are 'caught', display the exception 
    # message to the console.

    # 1. Code a statement which creates an instance of the LibraryItem class with valid inputs.
    # Use your own unique valid values for the inputs to the class.

    try:
        book = LibraryItem(777, "Hobbit", "Tolkien", Genre.FANTASY, False)
    except ValueError as e:
        print(e)
         
    # 2. Using the instance defined above, and the class Accessors, print 
    # each of the attributes of the LibraryItem instance.

    print(f"{book.item_id}, {book.title}, {book.author},"
          + f" {book.genre.name}, {book.is_borrowed}")   
    

    # 3. Code a statement which creates an instance of the LibraryItem class with one or more invalid inputs.
    # Use your own unique valid values for the inputs to the class.

    try:
        invalid_book = LibraryItem(123, "Where is my book",
                                "Who wrote this book", Genre.NON_FICTION, "False")
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()