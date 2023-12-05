from entities.book import Book
from entities.user import User
from entities.bookshelf import Bookshelf

from repositories.book_repository import (
    book_repository as default_book_repository
)

from repositories.user_repository import (
    user_repository as default_user_repository
)


class InvalidCredentialsError(Exception):
    pass


class UsernameExistsError(Exception):
    pass


class BookService:
    def __init__(
        self,
        book_repository=default_book_repository,
        user_repository=default_user_repository
    ):
        self._user = None
        self._book_repository = book_repository
        self._user_repository = user_repository

    def create_book(self, title, bookshelf):
        if not bookshelf:
            raise InvalidCredentialsError("Please choose a shelf for the book")
        
        book = Book(title=title, user=self._user, bookshelf=bookshelf)

        return self._book_repository.create(book)

    def get_books(self):
        if not self._user:
            return []

        books = self._book_repository.find_by_username(self._user.username)

        return list(books)

    def login(self, username, password):
        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise InvalidCredentialsError("Invalid username or password")

        self._user = user

        return user

    def logout(self):
        self._user = None

    def get_current_user(self):
        return self._user

    def get_users(self):
        return self._user_repository.find_all()

    def create_user(self, username, password, login=True):
        existing_user = self._user_repository.find_by_username(username)

        if existing_user:
            raise UsernameExistsError(f"Username {username} already exists")

        user = self._user_repository.create(User(username, password))

        if login:
            self._user = user

        return user


book_service = BookService()
