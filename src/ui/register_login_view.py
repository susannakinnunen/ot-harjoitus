from tkinter import ttk, StringVar, constants


class RegisterLoginView:
    def __init__(self, root, handle_create_new_user_button, handle_login_button):
        self._root = root
        self._handle_create_new_user_button = handle_create_new_user_button
        self._handle_login_button = handle_login_button
        self._frame = None

        self._initialize()

    def pack(self):
        """"Näyttää näkymän."""
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        heading_label = ttk.Label(
            master=self._frame, text="Kirjautumalla sisään pääset käyttämään sovellusta.")

        register_button = ttk.Button(
            master=self._frame,
            text="Luo uusi käyttäjätunnus",
            command=self._handle_create_new_user_button
        )
        login_button = ttk.Button(
            master=self._frame,
            text="Kirjaudu sisään",
            command=self._handle_login_button
        )

        heading_label.grid(row=0, column=0)
        register_button.grid(row=1, column=0)
        login_button.grid(row=2, column=0)
