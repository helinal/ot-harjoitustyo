import uuid


class Book:
    def __init__(self, title, user=None, book_id=None):
        self.title = title
        self.user = user
        self.id = book_id or str(uuid.uuid4())

# TODO: writer, genre, pages, year of publication...
