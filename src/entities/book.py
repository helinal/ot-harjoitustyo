import uuid


class Book:
    """Luokka, joka kuvaa yhtä kirjaa.

    Attributes:
        title: Merkkijonoarvo, joka kuvaa kirjan otikkoa.
        bookshelf: Merkkijonoarvo, joka kuvastaa mihin kirjahyllyyn kirja kuuluu.
        user: User-olio, joka kuvaa kirjan omistajaa.
        book_id: Merkkijonoarvo, joku kuvaa kirjan id:tä.
    """

    def __init__(self, title, bookshelf, user=None, book_id=None):
        """Luokan konstruktori, joka luo uuden kirjan.

        Args:
            title: Merkkijonoarvo, joka kuvaa kirjan otsikkoa.
            bookshelf: Merkkijonoarvo, joka kuvastaa mihin kirjahyllyyn kirja kuuluu.
            user:
                Vapaaehtoinen, oletusarvoltaan None.
                User-olio, joka kuvaa kirjan omistajaa.
            book_id:
                Vapaaehtoinen, oletusarvoltaan generoitu uuid.
                Merkkijonoarvo, joku kuvaa kirjan id:tä.
        """

        self.title = title
        self.bookshelf = bookshelf
        self.user = user
        self.id = book_id or str(uuid.uuid4())
