from tkinter import ttk, StringVar, constants
from services.stretching_services import StretchingService


class BodypartViewAdmin:
    """Näyttää kehonosanäkymän ylläpitäjän toiminnoilla"""
    def __init__(self, root, handle_bodypart_button, handle_admin_button, handle_logout):
        self._root = root
        self._handle_bodypart_button = handle_bodypart_button
        self._handle_admin_button = handle_admin_button
        self._handle_logout = handle_logout
        self._frame = None
        self._bodypart_list_view = None
        self._bodypart_list_frame = None

        self._error_variable = None
        self._error_label = None

        self._stretching_service = StretchingService()

        self._initialize()

    def destroy(self):
        """"Tuhoaa näkymän."""
        self._frame.destroy()

    def _show_error(self, message):
        self._error_variable.set(message)
        self._error_label.grid()

    def _hide_error(self):
        self._error_label.grid_remove()

    def _initialize(self):

        self._frame = ttk.Frame(master=self._root)

        self._error_variable = StringVar(self._frame)

        self._error_label = ttk.Label(
            master=self._frame,
            textvariable=self._error_variable,
            foreground="red"
        )

        self._error_label.grid(padx=5, pady=5)

        self._bodyparts = self._stretching_service.get_all_bodyparts()

        for bodypart in self._bodyparts:
            bodypart_button = ttk.Label(master=self._frame, text=bodypart)
            bodypart_button.grid(padx=5, pady=5)

        search_stretch_by_bodypart_label = ttk.Label(
            master=self._frame, text="Etsi venyttely kirjoittamalla listassa annettu kehonosa")
        self._search_stretch_by_bodypart_entry = ttk.Entry(master=self._frame)
        search_stretch_by_bodypart_button = ttk.Button(
            master=self._frame, text="Etsi", command=self._bodypart_handler)

        admin_button = ttk.Button(
            master=self._frame, text="Ylläpitäjän toiminnot", command=self._handle_admin_button)

        logout_button = ttk.Button(
            master=self._frame, text="Kirjaudu ulos", command=self._handle_logout)

        search_stretch_by_bodypart_label.grid(padx=5, pady=5)
        self._search_stretch_by_bodypart_entry.grid(padx=5, pady=5)
        search_stretch_by_bodypart_button.grid(padx=5, pady=5)
        admin_button.grid(padx=5, pady=5)
        logout_button.grid(padx=5, pady=5)

        self._hide_error()

    def pack(self):
        """Näyttää näkymän"""
        self._frame.pack(fill=constants.X)

    def _bodypart_handler(self):
        bodypart = self._search_stretch_by_bodypart_entry.get()
        stretches = self._stretching_service.show_stretch(bodypart)
        if stretches is False:
            self._show_error("Tapahtui virhe, kirjoita kehonosa uudestaan.")
            return
        self._handle_bodypart_button(bodypart)
