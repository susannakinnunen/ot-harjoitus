from re import S
from turtle import back
from services.stretching_services import StretchingService
from tkinter import ttk, StringVar, constants

error = "Tapahtui virhe, kirjoita uudelleen."

class StretchViewAdmin:
    def __init__(self, root, bodypart, handle_back_to_bodyparts_admin):
        self._root = root
        self.bodypart = bodypart
        self._handle_back_to_bodyparts_admin = handle_back_to_bodyparts_admin
        self._frame = None
        self._streching_service = StretchingService()
    
        self._initialize()

    def destroy(self):
        """"Tuhoaa näkymän."""
        self._frame.destroy()
    
    def pack(self):
        """"Näyttää näkymän."""
        self._frame.pack(fill=constants.X)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        stretches = self._streching_service.show_stretch(self.bodypart)

        index = 0
        for stretch in stretches:
            stretch_name = ttk.Label(master=self._frame, text=f"venyttelyn nimi: {stretch[0]}")
            stretch_instructions = ttk.Label(master=self._frame, text=f"ohjeet: {stretch[1]}")

            stretch_name.grid(padx=5, pady=5)
            index += 1
            stretch_instructions.grid(padx=5, pady=5)
            index += 1

        back_to_bodyparts = ttk.Button(master=self._frame, text="Takaisin kehonosiin", command=self._handle_back_to_bodyparts_admin)
        back_to_bodyparts.grid(padx=5, pady=5)







"""

    def initialize_stretches(self):
        self.streching_service.combine_stretches_and_bodyparts()

    def show_stretch(self, bodypart):
        stretch = self.streching_service.show_stretch(bodypart)
        if stretch == False:
            return error
        return stretch

    def add_stretch(self, stretch, description):
        self.streching_service.add_stretch(stretch, description)

"""