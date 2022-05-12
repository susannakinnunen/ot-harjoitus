from tkinter import Frame, ttk, StringVar, constants
from services.stretching_services import StretchingService

class AdminView:
    def __init__(self, root, handle_add_stretch):
        self._root = root
        self._frame = None
        self._frame_admin = None
        self._handle_add_stretch = handle_add_stretch
        self._stretching_service = StretchingService()

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """"Tuhoaa näkymän."""
        self._frame.destroy()


    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        heading_label = ttk.Label(master=self._frame, text="Lisää venytys")

        bodypart_label = ttk.Label(master=self._frame, text="Kehonosa")
        self._bodypart_entry = ttk.Entry(master=self._frame)

        stretch_name_label = ttk.Label(master=self._frame, text="Venyttelyn nimi")
        self._stretch_name_entry = ttk.Entry(master=self._frame)

        stretch_instructions_label = ttk.Label(master=self._frame, text="Venyttelyohjeet")
        self._stretch_instructions_entry = ttk.Entry(master=self._frame)

        add_button = ttk.Button(master=self._frame, text="Lisää", command=self.add_stretch_handler)

        heading_label.grid(row=0,column=0)
        
        bodypart_label.grid(row=1,column=0)
        self._bodypart_entry.grid(row=1,column=1)

        stretch_name_label.grid(row=2,column=0)
        self._stretch_name_entry.grid(row=2,column=1)

        stretch_instructions_label.grid(row=3,column=0)
        self._stretch_instructions_entry.grid(row=3,column=1)
        
        add_button.grid(row=4,column=0)


    def add_stretch_handler(self):
        bodypart = self._bodypart_entry.get()
        stretch_name = self._stretch_name_entry.get()
        stretch_instructions = self._stretch_instructions_entry.get()
        self._stretching_service.add_stretch(stretch_name,stretch_instructions)

        self._stretching_service.add_bodypart(bodypart, stretch_name)
        self._stretching_service.add_combination(bodypart, stretch_name)

        self._handle_add_stretch()
