from tkinter import ttk, StringVar, constants
from services.book_service import book_service, UsernameExistsError


class CreateUserView:
    """Rekisteröitymisestä vastaava näkymä.
    """

    def __init__(self, root, handle_create_user, handle_show_login_view):
        """Luokan konstruktori, joka luo uuden rekisteröitymisnäkymän.

        Args:
            root :
                Tkinter-elementti, jonka sisään näkymä alustetaan.
            handle_create_user:
                Arvo, jota kutsutaan, kun käyttäjä luodaan.
                Argumentteina käyttäjätunnus ja salasana.
            handle_show_login_view: 
                Arvo, jota kutsutaan, kun siirrytään takaisin kirjautumisnäkymään.
        """
        self._root = root
        self._handle_create_user = handle_create_user
        self._handle_show_login_view = handle_show_login_view
        self._frame = None
        self._username_entry = None
        self._password_entry = None
        self._error_variable = None
        self._error_label = None

        self._initialize()

    def pack(self):
        """Näyttää näkymän."""
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Tuhoaa näkymän."""
        self._frame.destroy()

    def _create_user_handler(self):
        username = self._username_entry.get()
        password = self._password_entry.get()

        if len(username) == 0 or len(password) == 0:
            self._show_error("Username and password is required")
            return

        if len(username) < 3:
            self._show_error("Username must be at least 3 characters long")
            return

        try:
            book_service.create_user(username, password)
            self._handle_create_user()
        except UsernameExistsError:
            self._show_error(f"Username {username} already exists")

    def _show_error(self, message):
        self._error_variable.set(message)
        self._error_label.grid()

    def _hide_error(self):
        self._error_label.grid_remove()

    def _initialize_username_field(self):
        username_label = ttk.Label(master=self._frame, text="Username")

        self._username_entry = ttk.Entry(master=self._frame)

        username_label.grid(padx=5, pady=5, sticky=constants.W)
        self._username_entry.grid(padx=5, pady=5, sticky=constants.EW)

    def _initialize_password_field(self):
        password_label = ttk.Label(master=self._frame, text="Password")

        self._password_entry = ttk.Entry(master=self._frame, show="*")

        password_label.grid(padx=5, pady=5, sticky=constants.W)
        self._password_entry.grid(padx=5, pady=5, sticky=constants.EW)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        self._login_label = ttk.Label(
            master=self._frame, text="Create a new user",
            font=("Arial", 17))
        self._login_label.grid(padx=5, pady=5)

        self._error_variable = StringVar(self._frame)

        self._error_label = ttk.Label(
            master=self._frame,
            textvariable=self._error_variable,
            foreground="red"
        )

        self._error_label.grid(padx=5, pady=5)

        self._initialize_username_field()
        self._initialize_password_field()

        create_user_button = ttk.Button(
            master=self._frame,
            text="Create a new user",
            command=self._create_user_handler
        )

        login_button = ttk.Button(
            master=self._frame,
            text="Back to login",
            command=self._handle_show_login_view
        )

        self._frame.grid_columnconfigure(0, weight=1, minsize=400)
        self._frame.configure(padding=(20, 10))

        create_user_button.grid(padx=5, pady=5, sticky=constants.EW)
        login_button.grid(padx=5, pady=5, sticky=constants.EW)

        self._hide_error()
