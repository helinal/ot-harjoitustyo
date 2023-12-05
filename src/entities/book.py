import uuid


class Book:
    def __init__(self, title, bookshelf, user=None, book_id=None):
        self.title = title
        self.bookshelf = bookshelf
        self.user = user
        self.id = book_id or str(uuid.uuid4())
