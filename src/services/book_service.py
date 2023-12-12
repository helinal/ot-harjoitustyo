from entities.book import Book
from entities.user import User

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
    """Sovelluslogiikasta vastaava luokka.
    """

    def __init__(
        self,
        book_repository=default_book_repository,
        user_repository=default_user_repository
    ):
        """Luokan konstruktori.
           Luo uuden sovelluslogiikasta vastaavan palvelun.

        Args:
            book_repository:
                Vapaaehtoinen, oletuksena BookRepository-olio.
                Olio, jolla on BookRepository-luokkaa vastaavat metodit.
            user_repository:
                Vapaaehtoinen, oletuksena UserRepository-olio.
                Olio, jolla on UserRepository-luokkaa vastaavat metodit.
        """

        self._user = None
        self._book_repository = book_repository
        self._user_repository = user_repository

    def create_book(self, title, bookshelf):
        """Luo uuden kirjan.

        Args:
            Title: Merkkijonoarvo, joka kuvaa kirjan otsikkoa.
            bookshelf: Kirjahylly-olio, johon kirja sijoitetaan.
        Returns:
            Luotu kirja Book-oliona.
            Jos kirja on jo olemassa, palauttaa kyseisen jo olemassa olevan kirjan.
        """

        if not bookshelf:
            raise InvalidCredentialsError("Please choose a shelf for the book")

        existing_books = self._book_repository.find_all()
        existing_book = next(
            (b for b in existing_books if b.title == title and b.bookshelf == bookshelf), None)

        if existing_book:
            return existing_book

        book = Book(title=title, user=self._user, bookshelf=bookshelf)
        return self._book_repository.create(book)

    def get_books(self):
        """Palauttaa kirjautuneen käyttäjän kirjat.

        Returns:
            Palauttaa kirjautuneen käyttäjän kirjat Book-olioiden listana.
            Jos käyttäjä ei ole kirjautunut, palauttaa tyhjän listan.
        """
        if not self._user:
            return []

        books = self._book_repository.find_by_username(self._user.username)

        return list(books)

    def delete_book(self, book_id):
        """Poistaa tietyn, yksittäisen kirjan.

        Args:
            book_id: Poistetttavan kirjan id.
        """

        self._book_repository.delete(book_id)

    def login(self, username, password):
        """Kirjaa käyttäjän sisään.

        Args:
            username: Merkkijonoarvo, joka kuvaa kirjautuvan käyttäjän käyttäjätunnusta.
            password: Merkkijonoarvo, joka kuvaa kirjautuvan käyttäjän salasanaa.
        Returns:
            Kirjautunut käyttäjä User-oliona.
        Raises:
            InvalidCredentialsError:
                Virhe, joka tapahtuu, jos käyttäjätunnus ja salasana eivät täsmää.
        """

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise InvalidCredentialsError("Invalid username or password")

        self._user = user

        return user

    def logout(self):
        """Kirjaa tämänhetkisen käyttäjän ulos.
        """

        self._user = None

    def get_current_user(self):
            """Paluttaa kirjautuneen käyttäjän.

        Returns:
            Kirjautunut käyttäjä User-oliona.
        """

        return self._user

    def get_users(self):
        """Palauttaa kaikki käyttäjät.

        Returns:
            User-olioita sisältävä lista kaikista käyttäjistä.
        """

        return self._user_repository.find_all()

    def create_user(self, username, password, login=True):
        """Luo uuden käyttäjän ja tarvittaessa kirjaa luodun käyttäjän sisään.

        Args:
            username: Merkkijonoarvo, joka kuvaa käyttäjän käyttäjätunnusta.
            password: Merkkijonoarvo, joka kuvaa käyttäjän salasanaa.
            login:
                Vapaahtoinen, oletusarvo True.
                Boolean-arvo, joka kertoo kirjataanko käyttäjä sisään onnistuneen luonnin jälkeen.

        Raises:
            UsernameExistsError: Virhe, joka tapahtuu, kun käyttäjätunnus on jo käytössä.

        Returns:
            Luotu käyttäjä User-oliona.
        """

        existing_user = self._user_repository.find_by_username(username)

        if existing_user:
            raise UsernameExistsError(f"Username {username} already exists")

        user = self._user_repository.create(User(username, password))

        if login:
            self._user = user

        return user


book_service = BookService()
