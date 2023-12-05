from tkinter import ttk, constants
from tkinter import IntVar
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

        label.grid(row=0, padx=3, pady=3)

        item_frame.pack(fill=constants.X)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        # self._frame.grid(row=0, column=0, padx=10, pady=10)

        for book in self._books:
            self._initialize_book(book)


class BooksView:
    def __init__(self, root, handle_logout):
        self._root = root
        self._frame = None
        self._handle_logout = handle_logout
        self._user = book_service.get_current_user()
        self._create_book_entry = None
        self._selected_shelf = None
        self._want_list_frame = None
        self._reading_list_frame = None
        self._read_list_frame = None
        self._want_book_list = None
        self._reading_book_list = None
        self._read_book_list = None

        self._initialize()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._want_list_frame = ttk.Frame(master=self._frame)
        self._reading_list_frame = ttk.Frame(master=self._frame)
        self._read_list_frame = ttk.Frame(master=self._frame)

        self._initialize_loggedin()
        self._initialize_bookshelves()
        self._initialize_book_list()
        self._initialize_headers()

        self._want_list_frame.grid(
            row=1,
            column=0,
            columnspan=2,
            sticky=constants.EW
        )
        self._reading_list_frame.grid(
            row=1,
            column=1,
            columnspan=2,
            sticky=constants.EW
        )
        self._read_list_frame.grid(
            row=1,
            column=2,
            columnspan=2,
            sticky=constants.EW
        )

        self._frame.grid_columnconfigure(0, weight=1, minsize=100)
        self._frame.grid_columnconfigure(1, weight=0, minsize=100)
        self._frame.grid_columnconfigure(2, weight=0, minsize=100)

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _logout_handler(self):
        book_service.logout()
        self._handle_logout()

    def _initialize_book_list(self):
        if self._want_book_list:
            self._want_book_list.destroy()
        elif self._reading_book_list:
            self._reading_book_list.destroy()
        elif self._read_book_list:
            self._read_book_list.destroy()

        books = book_service.get_books()
        want_books = []
        reading_books = []
        read_books = []

        for book in books:
            shelf = int(book.bookshelf)

            if shelf == 1:
                want_books.append(book)
            elif shelf == 2:
                reading_books.append(book)
            else:
                read_books.append(book)

        self._want_book_list = BookListView(
            self._want_list_frame,
            want_books
        )
        self._reading_book_list = BookListView(
            self._reading_list_frame,
            reading_books
        )
        self._read_book_list = BookListView(
            self._read_list_frame,
            read_books
        )

        self._want_book_list.pack()
        self._reading_book_list.pack()
        self._read_book_list.pack()

    def _initialize_loggedin(self):
        user_label = ttk.Label(
            master=self._frame,
            text=f"Logged in as {self._user.username}"
        )

        logout_button = ttk.Button(
            master=self._frame,
            text="Logout",
            command=self._logout_handler
        )
        user_label.grid_columnconfigure(0, weight=1, minsize=100)
        user_label.grid(row=4, column=2, padx=3, pady=3, sticky=constants.EW)

        logout_button.grid(
            row=3,
            column=2,
            padx=5,
            pady=5,
            sticky=constants.EW
        )

    def _initialize_headers(self):
        want_to_read_label = ttk.Label(
            master=self._frame,
            text="want to read",
            font='Helvetica 15 bold'
        )
        reading_label = ttk.Label(
            master=self._frame,
            text="reading now",
            font='Helvetica 15 bold'
        )
        read_label = ttk.Label(
            master=self._frame,
            text="have already read",
            font='Helvetica 15 bold'
        )
        want_to_read_label.grid(row=0, column=0, padx=3,
                                pady=3, sticky=constants.W)
        reading_label.grid(row=0, column=1, padx=3, pady=3, sticky=constants.W)
        read_label.grid(row=0, column=2, padx=3, pady=3, sticky=constants.W)

    def _initialize_bookshelves(self):
        self._create_book_entry = ttk.Entry(master=self._frame)

        create_book_button = ttk.Button(
            master=self._frame,
            text="Add a new book",
            command=self._handle_create_book
        )

        self._create_book_entry.grid(
            row=3,
            column=0,
            padx=5,
            pady=5,
            sticky=constants.EW,
        )

        self._create_book_entry.grid_columnconfigure(0, weight=1, minsize=100)

        create_book_button.grid(
            row=3,
            column=1,
            padx=5,
            pady=5,
            sticky=constants.EW
        )

        def selected_shelf():
            self._selected_shelf = var.get()

        var = IntVar()

        create_wantto = ttk.Radiobutton(
            master=self._frame,
            text="want to read",
            variable=var,
            value=1,
            command=selected_shelf
        )

        create_reading = ttk.Radiobutton(
            master=self._frame,
            text="reading now",
            variable=var,
            value=2,
            command=selected_shelf
        )

        create_read = ttk.Radiobutton(
            master=self._frame,
            text="have read",
            variable=var,
            value=3,
            command=selected_shelf
        )

        create_wantto.grid(
            row=4,
            column=0,
            padx=1,
            pady=1,
            sticky=constants.EW
        )

        create_reading.grid(
            row=5,
            column=0,
            padx=1,
            pady=1,
            sticky=constants.EW
        )

        create_read.grid(
            row=6,
            column=0,
            padx=1,
            pady=1,
            sticky=constants.EW
        )

    def _handle_create_book(self):
        book_title = self._create_book_entry.get()
        bookshelf = self._selected_shelf

        if book_title:
            book_service.create_book(book_title, bookshelf)
            self._initialize_book_list()
            self._create_book_entry.delete(0, constants.END)
