from tkinter import ttk, StringVar, constants
from services.stretching_services import StretchingService

error_username = "Tapahtui virhe, valitse uusi käyttäjänimi"
error_too_short = "Käyttäjätunnuksen ja salasanan minimipituus 3 merkkiä"


class RegisterView:
    """Luokka vastaa rekisteröitymisnäkymästä."""
    def __init__(self, root, handle_register_button, handle_register_button_admin):
        self._root = root
        self._handle_register_button = handle_register_button
        self._handle_register_button_admin = handle_register_button_admin
        self._frame = None

        self._error_variable = None
        self._error_label = None

        self.stretching_service = StretchingService()

        self._initialize()

    def destroy(self):
        """Tuhoaa näkymän"""
        self._frame.destroy()

    def pack(self):
        """"Näyttää näkymän."""
        self._frame.pack(fill=constants.X)

    def _show_error(self, message):
        self._error_variable.set(message)
        self._error_label.grid()

    def _hide_error(self):
        self._error_label.grid_remove()

    def _register_handler(self):
        username = self._username_entry.get()
        password = self._password_entry.get()
        if len(username) < 3 or len(password) < 3:
            self._show_error(error_too_short)
            return
        user = self.stretching_service.create_new_user(username, password)
        if user is True:
            admin = self.stretching_service.check_if_admin(username)
            if admin:
                self._handle_register_button_admin()
            else:
                self._handle_register_button()
        else:
            self._show_error(error_username)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        self._error_variable = StringVar(self._frame)

        self._error_label = ttk.Label(
            master=self._frame,
            textvariable=self._error_variable,
            foreground="red"
        )

        self._error_label.grid(padx=5, pady=5)

        heading_label = ttk.Label(
            master=self._frame, text="Luo uusi käyttäjätunnus ja salasana.")

        username_label = ttk.Label(master=self._frame, text="Käyttäjätunnus")
        self._username_entry = ttk.Entry(master=self._frame)

        password_label = ttk.Label(master=self._frame, text="Salasana")
        self._password_entry = ttk.Entry(master=self._frame)

        register_button = ttk.Button(
            master=self._frame, text="Rekisteröidy", command=self._register_handler)

        heading_label.grid(padx=5, pady=5)

        username_label.grid(padx=5, pady=5)
        self._username_entry.grid(padx=5, pady=5)

        password_label.grid(padx=5, pady=5)
        self._password_entry.grid(padx=5, pady=5)

        register_button.grid(padx=5, pady=5)

        self._hide_error()
