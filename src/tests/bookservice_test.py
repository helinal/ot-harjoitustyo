import unittest
from services.book_service import (
    BookService,
    InvalidCredentialsError,
    UsernameExistsError
)
from entities.user import User


class FakeBookRepository:
    def __init__(self, books=None):
        self.books = books or []

    def find_all(self):
        return self.books

    def find_by_username(self, username):
        user_books = filter(
            lambda book: book.user and book.user.username == username,
            self.books
        )

        return list(user_books)

    def create(self, book):
        self.books.append(book)

        return book

    def delete(self, book_id):
        books_without_id = filter(lambda book: book.id != book_id, self.books)
        self.books = list(books_without_id)

    def delete_all(self):
        self.books = []


class FakeUserRepository:
    def __init__(self, users=None):
        self.users = users or []

    def find_all(self):
        return self.users

    def find_by_username(self, username):
        matching_users = filter(
            lambda user: user.username == username,
            self.users
        )

        matching_users_list = list(matching_users)

        return matching_users_list[0] if len(matching_users_list) > 0 else None

    def create(self, user):
        self.users.append(user)

        return user

    def delete_all(self):
        self.users = []

class TestBookService(unittest.TestCase):
    def setUp(self):
        self.book_service = BookService(
            FakeBookRepository(),
            FakeUserRepository()
        )

        self.user_nalle = User('nallepuh', 'nallepuh111')

    def login(self, user):
        self.book_service.create_user(user.username, user.password)

    def test_login_with_valid_username_and_password(self):
        self.book_service.create_user(
            self.user_nalle.username,
            self.user_nalle.password
        )
        user = self.book_service.login(
            self.user_nalle.username,
            self.user_nalle.password
        )

        self.assertEqual(user.username, self.user_nalle.username)

    def test_login_with_invalid_username_and_password(self):
        self.assertRaises(
            InvalidCredentialsError,
            lambda: self.book_service.login('väärä', 'väärä')
        )

    def test_create_user_with_non_existing_username(self):
        username = self.user_nalle.username
        password = self.user_nalle.password

        self.book_service.create_user(username, password)
        users = self.book_service.get_users()

        self.assertEqual(len(users), 1)
        self.assertEqual(users[0].username, username)

    def test_create_user_with_already_existing_username(self):
        username = self.user_nalle.username
        self.book_service.create_user(username, 'salasana')

        self.assertRaises(
            UsernameExistsError,
            lambda: self.book_service.create_user(username, 'salasana')
        )

    def test_get_current_user(self):
        self.login(self.user_nalle)
        current_user = self.book_service.get_current_user()

        self.assertEqual(current_user.username, self.user_nalle.username)

    def test_create_new_book(self):
        self.login(self.user_nalle)

        self.book_service.create_book("paras kirja")
        books = self.book_service.get_books()

        self.assertEqual(len(books), 1)
        self.assertEqual(books[0].title, 'paras kirja')
        self.assertEqual(books[0].user.username, self.user_nalle.username)