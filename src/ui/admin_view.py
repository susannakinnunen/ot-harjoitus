from tkinter import Frame, ttk, StringVar, constants
from services.stretching_services import StretchingService

class AdminView:
    def __init__(self, root, handle_add_stretch):
        self._root = root
        self._frame = None
        self._frame_admin = None
        self._handle_add_stretch = handle_add_stretch
        self._stretching_service = StretchingService()

        self._error_variable = None
        self._error_label = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

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

        heading_label = ttk.Label(master=self._frame, text="Lisää venytys")

        bodypart_label = ttk.Label(master=self._frame, text="Kehonosa")
        self._bodypart_entry = ttk.Entry(master=self._frame)

        stretch_name_label = ttk.Label(master=self._frame, text="Venyttelyn nimi")
        self._stretch_name_entry = ttk.Entry(master=self._frame)

        stretch_instructions_label = ttk.Label(master=self._frame, text="Venyttelyohjeet")
        self._stretch_instructions_entry = ttk.Entry(master=self._frame)

        add_button = ttk.Button(master=self._frame, text="Lisää", command=self.add_stretch_handler)

        heading_label.grid(padx=5, pady=5)
        
        bodypart_label.grid(padx=5, pady=5)
        self._bodypart_entry.grid(padx=5, pady=5)

        stretch_name_label.grid(padx=5, pady=5)
        self._stretch_name_entry.grid(padx=5, pady=5)

        stretch_instructions_label.grid(padx=5, pady=5)
        self._stretch_instructions_entry.grid(padx=5, pady=5)
        
        add_button.grid(padx=5, pady=5)

        self._hide_error()

    def add_stretch_handler(self):
        bodypart = self._bodypart_entry.get()
        stretch_name = self._stretch_name_entry.get()
        stretch_instructions = self._stretch_instructions_entry.get()

        if len(bodypart) == 0 or len(stretch_name) == 0 or len(stretch_instructions) == 0:
            self._show_error("Mikään kentistä ei saa olla tyhjä")
            return
        
        self._stretching_service.add_bodypart(bodypart, stretch_name)
        self._stretching_service.add_stretch(stretch_name,stretch_instructions)
        self._stretching_service.add_combination(bodypart, stretch_name)

        self._handle_add_stretch()
