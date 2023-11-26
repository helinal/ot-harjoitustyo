from entities.user import User


class BookService:

    def __init__(self):
        self._users = {}

    def login(self, username, password):
        return password == self._users.get(username)

    def create_user(self, username, password):
        self._users.update({username: password})


book_service = BookService()
