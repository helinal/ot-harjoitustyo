from tkinter import ttk, constants

class BooksView:
    
    def __init__(self, root, books):
        self._root = root
        self._books = books
        self._frame = None

        self._initialize()

    def _initialize(self):
        label = ttk.Label(master=self._root, text="This is going to be the main page of the application :D")
        label.pack()

    def pack(self):
        """"Näyttää näkymän."""
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """"Tuhoaa näkymän."""
        self._frame.destroy()