"""
Description: Unit tests for the Book class.
Usage: To execute all tests in the terminal execute 
the following command in the root folder:
    python -m unittest tests/test_library_item.py

"""
__author__ = "Tri Tranvo"
__version__ = "1.0.0"

import unittest

from library_item.library_item import LibraryItem
from genre.genre import Genre

class TestLibraryItem(unittest.TestCase):

    def setUp(self):
        self.library_item = LibraryItem(777, "Hobbit", "Tolkien", Genre.FANTASY, False)
   
    def test_init_valid_inputs_attributes_set(self):
        library_item = LibraryItem(777, "Hobbit", "Tolkien", Genre.FANTASY, False)

        self.assertEqual(777, library_item._LibraryItem__item_id)
        self.assertEqual("Hobbit", library_item._LibraryItem__title)
        self.assertEqual("Tolkien", library_item._LibraryItem__author)
        self.assertEqual(Genre.FANTASY, library_item._LibraryItem__genre)
        self.assertEqual(False, library_item._LibraryItem__is_borrowed)

    def test_init_non_numeric_item_id_raises_valueerror(self):
        with self.assertRaises(ValueError):
            library_item= LibraryItem("777", "Hobbit", "Tolkien", Genre.FANTASY, False)

    def test_init_blank_title_raises_valueerror(self):
        with self.assertRaises(ValueError):
            library_item = LibraryItem(777, "   ", "Tolkien", Genre.FANTASY, False)

    def test_init_blank_author_raises_valueerror(self):
        with self.assertRaises(ValueError):
            library_item = LibraryItem(777, "Hobbit", "   ", Genre.FANTASY, False)

    def test_init_invalid_genre_raises_valueerror(self):
        with self.assertRaises(ValueError):
            library_item = LibraryItem(777, "Hobbit", "Tolkien", "INVALID", False)
    
    def test_init_non_boolean_is_borrowed_raises_valueerror(self):
        with self.assertRaises(ValueError):
            library_item = LibraryItem(777, "Hobbit", "Tolkien", Genre.FANTASY, "Maybe")

    def test_item_id_accessor_valid_instance_returns_item_id(self):
        actual =self.library_item.item_id

        self.assertEqual(777, actual)

    def test_title_accessor_valid_instance_returns_title(self):
        actual = self.library_item.title

        self.assertEqual("Hobbit", actual)

    def test_author_accessor_valid_instance_returns_author(self):
        actual= self.library_item.author

        self.assertEqual("Tolkien", actual)

    def test_genre_accessor_valid_instance_returns_genre(self):
        self.assertEqual(Genre.FANTASY, self.library_item.genre)

    def test_is_borrowed_accessor_valid_instance_returns_is_borrowed(self):
        self.assertEqual(False, self.library_item.is_borrowed)
