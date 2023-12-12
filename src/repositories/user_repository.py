from entities.user import User
from database_connection import get_database_connection


def get_user_by_row(row):
    return User(row["username"], row["password"]) if row else None


class UserRepository:
    """Käyttäjien tietokantaoperaatioista vastaava luokka.
    """

    def __init__(self, connection):
        """Luokan konstruktori.

        Args:
            connection: Tietokantayhteyden Connection-olio.
        """
        self._connection = connection

    def create(self, user):
        """Lisää uuden käyttäjän tietokantaan.

        Args:
            user: Tallennettava käyttäjä User-oliona.

        Returns:
            Tallennettu käyttäjä User-oliona.
        """

        cursor = self._connection.cursor()

        cursor.execute(
            "insert into users (username, password) values (?, ?)",
            (user.username, user.password)
        )

        self._connection.commit()

        return user

    def find_all(self):
        """Etsii kaikki tietokannan käyttäjät.

        Returns:
            Palauttaa listan User-olioita.
        """

        cursor = self._connection.cursor()

        cursor.execute("select * from users")

        rows = cursor.fetchall()

        return list(map(get_user_by_row, rows))

    def find_by_username(self, username):
        """Palauttaa käyttäjän käyttäjätunnuksen perusteella.

        Args:
            username: Käyttäjätunnus, jonka käyttäjä palautetaan.

        Returns:
            Palauttaa User-olion, jos käyttäjätunnuksen omaava käyttäjä löytyy tietokannasta.
            Muussa tapauksessa palauttaa None.
        """

        cursor = self._connection.cursor()

        cursor.execute(
            "select * from users where username = ?",
            (username,)
        )

        row = cursor.fetchone()

        return get_user_by_row(row)

    def delete_all(self):
        """Poistaa kaikki käyttäjät.
        """
        
        cursor = self._connection.cursor()

        cursor.execute("delete from users")

        self._connection.commit()


user_repository = UserRepository(get_database_connection())
