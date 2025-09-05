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
        self.library_item = LibraryItem("Hobbit", "Tolkien", Genre.FANTASY)
   
    def test_init_valid_inputs_attributes_set(self):
        library_item = LibraryItem("Hobbit", "Tolkien", Genre.FANTASY)

        self.assertEqual("Hobbit", library_item._LibraryItem__title)
        self.assertEqual("Tolkien", library_item._LibraryItem__author)
        self.assertEqual(Genre.FANTASY, library_item._LibraryItem__genre)

    def test_init_blank_title_raises_valueerror(self):
        with self.assertRaises(ValueError):
            library_item = LibraryItem("   ", "Tolkien", Genre.FANTASY)

    def test_init_blank_author_raises_valueerror(self):
        with self.assertRaises(ValueError):
            library_item = LibraryItem("Hobbit", "   ", Genre.FANTASY)

    def test_init_invalid_genre_raises_valueerror(self):
        with self.assertRaises(ValueError):
            library_item = LibraryItem("Hobbit", "Tolkien", "Invalid")

    def test_title_accessor_valid_instance_returns_title(self):
        actual = self.library_item.title

        self.assertEqual("Hobbit", actual)

    def test_author_accessor_valid_instance_returns_author(self):
        actual= self.library_item.author

        self.assertEqual("Tolkien", actual)

    def test_genre_accesor_valid_instance_returns_genre(self):
        self.assertEqual(Genre.FANTASY, self.library_item.genre)
