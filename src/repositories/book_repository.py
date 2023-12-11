from pathlib import Path
from entities.book import Book
from repositories.user_repository import user_repository
from config import BOOKS_FILE_PATH


class BookRepository:
    def __init__(self, file_path):
        self._file_path = file_path

    def create(self, book):
        books = self.find_all()

        existing_book = next((b for b in books if b.title ==
                             book.title and b.bookshelf == book.bookshelf), None)

        if existing_book:
            return existing_book

        books.append(book)
        self._write(books)

        return book

    def find_all(self):
        return self._read()

    def find_by_username(self, username):
        books = self.find_all()

        user_books = filter(
            lambda book: book.user and book.user.username == username, books)

        return list(user_books)

    def delete(self, book_id):
        books = self.find_all()

        updated_books = [book for book in books if book.id != book_id]

        self._write(updated_books)

    def delete_all(self):
        self._write([])

    def _ensure_file_exists(self):
        Path(self._file_path).touch()

    def _read(self):
        books = []

        self._ensure_file_exists()

        with open(self._file_path, encoding="utf-8") as file:
            for row in file:
                row = row.replace("\n", "")
                parts = row.split(";")

                book_id = parts[0]
                title = parts[1]
                shelf = parts[2]
                username = parts[3]

                user = user_repository.find_by_username(
                    username) if username else None

                books.append(
                    Book(title, shelf, user, book_id)
                )

        return books

    def _write(self, books):
        self._ensure_file_exists()

        with open(self._file_path, "w", encoding="utf-8") as file:
            for book in books:
                username = book.user.username if book.user else ""

                row = f"{book.id};{book.title};{book.bookshelf};{username}"

                file.write(row+"\n")


book_repository = BookRepository(BOOKS_FILE_PATH)
