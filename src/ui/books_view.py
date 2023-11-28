from tkinter import ttk, constants
from services.book_service import book_service


class BookListView:
    def __init__(self, root, books):
        self._root = root
        self._books = books
        self._frame = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize_book(self, book):
        item_frame = ttk.Frame(master=self._frame)
        label = ttk.Label(master=item_frame, text=book.title)

        label.grid(row=0, column=0, padx=5, pady=5, sticky=constants.W)

        item_frame.grid_columnconfigure(0, weight=1)
        item_frame.pack(fill=constants.X)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        for book in self._books:
            self._initialize_book(book)


class BooksView:
    def __init__(self, root, handle_logout):
        self._root = root
        self._frame = None
        self._handle_logout = handle_logout
        self._user = book_service.get_current_user()
        self._create_book_entry = None
        self._book_list_frame = None
        self._book_list_view = None

        self._initialize()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._book_list_frame = ttk.Frame(master=self._frame)

        self._initialize_header()
        self._initialize_book_list()
        self._initialize_footer()

        self._book_list_frame.grid(
            row=1,
            column=0,
            columnspan=2,
            sticky=constants.EW
        )

        self._frame.grid_columnconfigure(0, weight=1, minsize=400)
        self._frame.grid_columnconfigure(1, weight=0)

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _logout_handler(self):
        book_service.logout()
        self._handle_logout()

    def _initialize_book_list(self):
        if self._book_list_view:
            self._book_list_view.destroy()

        books = book_service.get_books()

        self._book_list_view = BookListView(
            self._book_list_frame,
            books
        )

        self._book_list_view.pack()

    def _initialize_header(self):
        user_label = ttk.Label(
            master=self._frame,
            text=f"Logged in as {self._user.username}"
        )

        logout_button = ttk.Button(
            master=self._frame,
            text="Logout",
            command=self._logout_handler
        )

        user_label.grid(row=0, column=0, padx=5, pady=5, sticky=constants.W)

        logout_button.grid(
            row=0,
            column=1,
            padx=5,
            pady=5,
            sticky=constants.EW
        )

    def _initialize_footer(self):
        self._create_book_entry = ttk.Entry(master=self._frame)

        create_book_button = ttk.Button(
            master=self._frame,
            text="Add a new book",
            command=self._handle_create_book
        )

        self._create_book_entry.grid(
            row=2,
            column=0,
            padx=5,
            pady=5,
            sticky=constants.EW
        )

        create_book_button.grid(
            row=2,
            column=1,
            padx=5,
            pady=5,
            sticky=constants.EW
        )

    def _handle_create_book(self):
        book_title = self._create_book_entry.get()

        if book_title:
            book_service.create_book(book_title)
            self._initialize_book_list()
            self._create_book_entry.delete(0, constants.END)
