import unittest
from repositories.book_repository import book_repository
from repositories.user_repository import user_repository
from entities.book import Book
from entities.user import User


class TestTodoRepository(unittest.TestCase):
    def setUp(self):
        book_repository.delete_all()
        user_repository.delete_all()

        self.ekakirja = Book('eka', 1)
        self.tokakirja = Book('toka', 2)
        self.user_nalle = User('nalle', 'puh123')
        self.user_nasu = User('nasu', 'nasu123')

    def test_create(self):
        book_repository.create(self.ekakirja)
        books = book_repository.find_all()

        self.assertEqual(len(books), 1)
        self.assertEqual(books[0].title, self.ekakirja.title)

    def test_find_all(self):
        book_repository.create(self.ekakirja)
        book_repository.create(self.tokakirja)
        books = book_repository.find_all()

        self.assertEqual(len(books), 2)
        self.assertEqual(books[0].title, self.ekakirja.title)
        self.assertEqual(books[1].title, self.tokakirja.title)

    def test_find_by_username(self):
        nalle = user_repository.create(self.user_nalle)
        nasu = user_repository.create(self.user_nasu)

        book_repository.create(Book(title='jee', bookshelf=1, user=nalle))
        book_repository.create(Book(title='juu', bookshelf=1, user=nasu))

        nalle_books = book_repository.find_by_username(
            self.user_nalle.username)

        self.assertEqual(len(nalle_books), 1)
        self.assertEqual(nalle_books[0].title, 'jee')

        nasu_books = book_repository.find_by_username(
            self.user_nasu.username)

        self.assertEqual(len(nasu_books), 1)
        self.assertEqual(nasu_books[0].title, 'juu')

    def test_delete(self):
        created_book = book_repository.create(self.ekakirja)
        books = book_repository.find_all()

        self.assertEqual(len(books), 1)

        book_repository.delete(created_book.id)

        books = book_repository.find_all()

        self.assertEqual(len(books), 0)
