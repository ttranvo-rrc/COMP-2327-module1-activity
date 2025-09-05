__author__ = "Tri Tranvo"
__version__ = "1.0.0"

from genre.genre import Genre

class LibraryItem:
    """
    Description: A class to manage LibraryItem objects.
    """

    def __init__(self, item_id: int ,title: str, author: str, genre: Genre, is_borrowed: bool):
        """
        Initializes class attributes to argument values.

        Args:
            item_id (int): An id number to uniquely identify 
            the library item.
            title (str): The title of the library item.
            author (str): The author of the library item.
            genre (Genre): The Genre of the library item.
            is_borrowed (bool): Identifies whether the library item
            is borrowed (True) or available (False).

        Raises:
            ValueError: When item_id is non numeric, 
            when title is blank, when author is blank, 
            when Genre is invalid, 
            when is_borrowed is not a true or false.

        """

        if isinstance(item_id, int):
            self.__item_id = item_id
        else:
            raise ValueError("Item Id must be numeric.")

        if len(title.strip()) > 0:
            self.__title = title
        else:
            raise ValueError("Title cannot be blank.")
        
        if len(author.strip()) > 0:
            self.__author = author
        else:
            raise ValueError("Author cannot be blank.")
        
        if isinstance(genre,Genre):
            self.__genre = genre
        else:
            raise ValueError("Invalid Genre.")

        if isinstance(is_borrowed, bool):
            self.__is_borrowed = is_borrowed
        else:
            raise ValueError("Is Borrowed must be a boolean value.")


    @property
    def item_id(self) -> int:
        """
        Accessor for item_id attribute

        Returns:
            int: The item id of the library item.

        """
        return self.__item_id

    @property
    def title(self) -> str:
        """
        Accessor for title attribute

        Returns:
            str: The title of the library item.

        """
        return self.__title
    

    @property
    def author(self) -> str:
        """
        Accessor for the author attribute

        Returns:
            str: The author of the library item.

        """
        return self.__author
    
    @property
    def genre(self) -> Genre:
        """
        Accessor for the genre attribute

        Returns:
            Genre: Enum value of genre.
            
        """
        return self.__genre
    
    @property
    def is_borrowed(self) -> bool:
        """
        Accessor for the is_borrowed attribute

        Returns:
            bool: True or false of the status of the library item.
        """
        return self.__is_borrowed
