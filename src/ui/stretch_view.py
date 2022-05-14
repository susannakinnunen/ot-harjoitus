from services.stretching_services import StretchingService
from tkinter import ttk, constants

error = "Tapahtui virhe, kirjoita uudelleen."


class StretchView:
    def __init__(self, root, bodypart, handle_back_to_bodyparts):
        self._root = root
        self.bodypart = bodypart
        self._handle_back_to_bodyparts = handle_back_to_bodyparts
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
            stretch_name = ttk.Label(
                master=self._frame, text=f"venyttelyn nimi: {stretch[0]}")
            stretch_instructions = ttk.Label(
                master=self._frame, text=f"ohjeet: {stretch[1]}")

            stretch_name.grid(padx=5, pady=5)
            index += 1
            stretch_instructions.grid(padx=5, pady=5)
            index += 1

        back_to_bodyparts = ttk.Button(
            master=self._frame, text="Takaisin kehonosiin", command=self._handle_back_to_bodyparts)
        back_to_bodyparts.grid(padx=5, pady=5)
