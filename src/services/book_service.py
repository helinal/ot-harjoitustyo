from entities.user import User

class BookService:
    
    def __init__(self):
        self._user = None

    def login(self, username, password):
        user = User(username, password)
        self._user = user
        return user
    

book_service = BookService()