class Bookshelf:
    """Luokka, joka kuvaa yhtä kirjahyllyä.

    Attributes:
        name: Merkkijonoarvo, joka kuvaa kirjahyllyn nimeä.
        books: Lista, joka sisältää kaikki kirjahyllyn kirja-oliot.
    """

    def __init__(self, name, books):
        """Luokan konstruktori, joka luo uuden kirjahyllyn.

        Args:
            name: Merkkijonoarvo, joka kuvaa kirjahyllyn nimeä.
            books: Lista, joka sisältää kaikki kirjahyllyn kirja-oliot.
        """

        self.name = name
        self.books = books
