from tkinter import ttk, constants, StringVar, messagebox
from services.book_service import book_service


class BookListView:
    """Sovelluksen 'main pagesta' ja kirjojen lisauksesta vastaava näkymä."""

    def __init__(self, root, books):
        """Luokan konstruktori, joka luo uuden päänäkymän.

        Args:
            root: 
                Tkinter-elementti, jonka sisään näkymä alustetaan
            books:
                Lista Book-olioita, jotka näytetään näkymässä.
        """

        self._root = root
        self._books = books
        self._frame = None

        self._initialize()

    def pack(self):
        """Näyttää näkymän."""
        self._frame.pack()

    def destroy(self):
        """Tuhoaa näkymän."""
        self._frame.destroy()

    def _initialize_book(self, book):
        item_frame = ttk.Frame(master=self._frame)

        label = ttk.Label(master=item_frame, text=book.title)
        label.grid(row=0, column=0, padx=3, pady=3, sticky=constants.W)

        button_style = ttk.Style()
        button_style.configure("Delete.TButton", font=(
            "Helvetica", 8), padding=(0, 0))

        delete_button = ttk.Button(
            master=item_frame,
            text="Delete",
            command=lambda: self._delete_book(book),
            style="Delete.TButton"
        )

        delete_button.grid(row=0, column=1, padx=3, pady=3, sticky=constants.W)

        item_frame.pack(fill=constants.X)

    def _delete_book(self, book):
        book_service.delete_book(book.id)
        self._books.remove(book)
        self._update_books(self._books)

    # ChatGPT:n avulla generoitu koodi alkaa:
    def _update_books(self, new_books):
        for widget in self._frame.winfo_children():
            widget.destroy()

        for book in new_books:
            self._initialize_book(book)
    # Generoitu koodi päättyy

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        for book in self._books:
            self._initialize_book(book)


class BooksView:
    """Kirjojejn listauksesta ja kirjahyllyihin lisäämisestä vastaava näkymä."""

    def __init__(self, root, handle_logout):
        """Luokan konstruktori, joka luo uuden kirjanäkymän.

        Args:
            root:
                Tkinter-elementti, jonka sisään näkymä alustetaan.
            handle_logout:
                Arvo, jota kutsutaan, kun kirjaudutaan ulos.
        """
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

    def pack(self):
        """Näyttää näkymän."""
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Tuhoaa näkymän."""
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._want_list_frame = ttk.Frame(master=self._frame)
        self._reading_list_frame = ttk.Frame(master=self._frame)
        self._read_list_frame = ttk.Frame(master=self._frame)

        self._initialize_loggedin()
        self._initialize_bookshelves()
        self._initialize_book_list()
        self._initialize_headers()

        self._want_list_frame.grid(row=2, column=0, sticky=constants.EW)
        self._reading_list_frame.grid(row=2, column=1, sticky=constants.EW)
        self._read_list_frame.grid(row=2, column=2, sticky=constants.EW)

        self._frame.grid_columnconfigure(0, weight=1)
        self._frame.grid_columnconfigure(1, weight=0)
        self._frame.grid_columnconfigure(2, weight=0)

    def _logout_handler(self):
        book_service.logout()
        self._handle_logout()

    def _initialize_book_list(self):
        books = book_service.get_books()

        want_books = [book for book in books if int(book.bookshelf) == 1]
        reading_books = [book for book in books if int(book.bookshelf) == 2]
        read_books = [book for book in books if int(book.bookshelf) == 3]

        # Generoitu koodi alkaa:
        for widget in self._want_list_frame.winfo_children():
            widget.destroy()

        for widget in self._reading_list_frame.winfo_children():
            widget.destroy()

        for widget in self._read_list_frame.winfo_children():
            widget.destroy()
        # Generoitu koodi päättyy

        self._want_book_list = BookListView(self._want_list_frame, want_books)
        self._reading_book_list = BookListView(
            self._reading_list_frame, reading_books)
        self._read_book_list = BookListView(self._read_list_frame, read_books)

        self._want_book_list.pack()
        self._reading_book_list.pack()
        self._read_book_list.pack()

        if not want_books:
            self._display_empty_message(self._want_list_frame, " No books yet")

        if not reading_books:
            self._display_empty_message(self._reading_list_frame, " No books yet")

        if not read_books:
            self._display_empty_message(self._read_list_frame, " No books yet")

        # Generoitu koodi alkaa:
        self._frame.update_idletasks()
        # Generoitu koodi päättyy

    def _display_empty_message(self, frame, message):
        empty_label = ttk.Label(master=frame, text=message)
        empty_label.pack(fill=constants.X)

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
        user_label.grid(row=4, column=3, padx=3, pady=3, sticky=constants.EW)

        logout_button.grid(
            row=3,
            column=3,
            padx=10,
            pady=10,
            sticky=constants.E
        )

    def _initialize_headers(self):
        want_to_read_label = ttk.Label(
            master=self._frame,
            text="Want to read",
            font='Helvetica 13 bold'
        )
        reading_label = ttk.Label(
            master=self._frame,
            text="Reading now",
            font='Helvetica 13 bold'
        )
        read_label = ttk.Label(
            master=self._frame,
            text="Have already read",
            font='Helvetica 13 bold'
        )

        want_to_read_label.grid(row=1, column=0, padx=3,
                                pady=3, sticky=constants.W)
        reading_label.grid(row=1, column=1, padx=3, pady=3, sticky=constants.W)
        read_label.grid(row=1, column=2, padx=3, pady=3, sticky=constants.W)

    def _initialize_bookshelves(self):
        self._create_book_entry = ttk.Entry(master=self._frame)

        create_book_button = ttk.Button(
            master=self._frame,
            text="Add a new book",
            command=self._handle_create_book,
            style='AddBook.TButton'
        )

        self._create_book_entry.grid(
            row=3,
            column=0,
            columnspan=2,
            padx=10,
            pady=10,
            sticky=constants.EW,
        )

        create_book_button.grid(
            row=3,
            column=2,
            padx=10,
            pady=10,
            sticky=constants.EW
        )

        var = StringVar()

        create_wantto = ttk.Radiobutton(
            master=self._frame,
            text="Want to Read",
            variable=var,
            value="1",
            command=lambda: self._set_selected_shelf(var.get())
        )

        create_reading = ttk.Radiobutton(
            master=self._frame,
            text="Currently Reading",
            variable=var,
            value="2",
            command=lambda: self._set_selected_shelf(var.get())
        )

        create_read = ttk.Radiobutton(
            master=self._frame,
            text="Already Read",
            variable=var,
            value="3",
            command=lambda: self._set_selected_shelf(var.get())
        )

        create_wantto.grid(row=4, column=0, padx=1,
                           pady=1, sticky=constants.EW)
        create_reading.grid(row=4, column=1, padx=1,
                            pady=1, sticky=constants.EW)
        create_read.grid(row=4, column=2, padx=1, pady=1, sticky=constants.EW)

    def _set_selected_shelf(self, value):
        self._selected_shelf = value

    max_title_length = 35

    def _handle_create_book(self):
        book_title = self._create_book_entry.get()
        bookshelf = self._selected_shelf

        try:
            self._validate_book_title(book_title)
        except ValueError as e:
            messagebox.showerror("Error", str(e))
            return

        if book_title and bookshelf:
            book_service.create_book(book_title, bookshelf)
            self._initialize_book_list()
            self._create_book_entry.delete(0, constants.END)
    
    def _validate_book_title(self, title):
        if len(title) == 0:
            raise ValueError(f"The title cannot be empty, please try again") 
        elif len(title) > self.max_title_length:
            raise ValueError(f"Book title cannot exceed {self.max_title_length} characters")
