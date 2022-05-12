from tkinter import ttk, StringVar, constants
from services.stretching_services import StretchingService

class BodypartViewAdmin:
    def __init__(self,root, handle_bodypart_button, handle_admin_button):
        self._root = root
        self._handle_bodypart_button = handle_bodypart_button
        self._handle_admin_button = handle_admin_button
        self._frame = None
        #self._bodypart_var = StringVar()
        self._bodypart_list_view = None
        self._bodypart_list_frame = None
    
        
        self._stretching_service = StretchingService()

        self._initialize()

    def destroy(self):
        """"Tuhoaa näkymän."""
        print("nyt tuhotaan bodypart admin")
        self._frame.destroy()
    
    def _initialize(self):

        self._frame = ttk.Frame(master=self._root)
        self._bodyparts = self._stretching_service.get_all_bodyparts()

        index = 0
        print(f"tässä on kehonosat{self._bodyparts} admin")
        for bodypart in self._bodyparts:
            #self._bodypart_var.set(bodypart)
            bodypart_button = ttk.Label(master=self._frame, text=bodypart)
            bodypart_button.grid(row=index,column=0)
            index += 1

        search_stretch_by_bodypart_label = ttk.Label(master=self._frame, text="Etsi venyttely kirjoittamalla listassa annettu kehonosa")
        self._search_stretch_by_bodypart_entry = ttk.Entry(master=self._frame)
        search_stretch_by_bodypart_button = ttk.Button(master=self._frame, text="Etsi",command=self._bodypart_handler)

        admin_button = ttk.Button(master=self._frame, text="ylläpitäjän toiminnot", command=self._handle_admin_button)
        
        search_stretch_by_bodypart_label.grid(row=index, column=0)
        self._search_stretch_by_bodypart_entry.grid(row=index, column=1)
        search_stretch_by_bodypart_button.grid(row=index+1, column=0)
        admin_button.grid(row=index+2,column=0)        

    def pack(self):
        self._frame.pack(fill=constants.X)

    def _bodypart_handler(self):
        bodypart = self._search_stretch_by_bodypart_entry.get()
        self._handle_bodypart_button(bodypart)







"""
class BodypartListView:
    def __init__(self, root, bodyparts, handle_bodyparts):
        self._root = root
        self._bodyparts = bodyparts
        self._handle_bodyparts = handle_bodyparts
        self._frame = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy() 

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        for bodypart in self._bodyparts:
            self._initialize_bodypart_item(bodypart)

    def _initialize_bodypart_item(self,bodypart):
        item_frame = ttk.Frame(master=self._frame)
        
        bodypart_button = ttk.Button(master=item_frame, text=bodypart, command=lambda: self._handle_bodyparts(bodypart))

        bodypart_button.grid(row=0, column=0)
        item_frame.grid_columnconfigure(0, weight=1)
        item_frame.pack(fill=constants.X)

"""