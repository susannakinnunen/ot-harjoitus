from tkinter import Frame, ttk, StringVar, constants
from services.stretching_services import StretchingService

class BodypartView:
    def __init__(self,root, handle_bodypart_button):
        self._root = root
        self._handle_bodypart_button = handle_bodypart_button
        self._frame = None
        self._bodypart_list_frame = None
        self._bodypart_list_view = None

        self._stretching_service = StretchingService()
        self._bodyparts = self._stretching_service.get_all_bodyparts()

        self._initialize()

    def destroy(self):
        """"Tuhoaa näkymän."""
        print("nyt tuhotaan bodypart")
        self._frame.destroy()

    
    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        #self._bodypart_list_frame = ttk.Frame(master=self._frame)

        #self._initialize_bodypart_list()
        index = 0
        print(f"tässä on kehonosat{self._bodyparts}")
        for bodypart in self._bodyparts:
            bodypart_button = ttk.Button(master=self._frame, text=self._bodyparts, command=lambda: self._bodypart_handler(bodypart))

            bodypart_button.grid(row=index,column=0)
            index += 1



    def pack(self):
        self._frame.pack(fill=constants.X)

    def _bodypart_handler(self, bodypart):
        self._handle_bodypart_button(bodypart)
"""
    def initialize_bodypart_list(self):
        if self._bodypart_list_view:
            self._bodypart_list_view.destroy()

        bodyparts = self._stretching_service.get_all_bodyparts()

        self._bodypart_list_view = BodypartListView(
            self._bodypart_list_frame,
            bodyparts
        )

        self._bodypart_list_view.pack()
"""







"""
class BodypartListView:
    def __init__(self, root, bodyparts):
        self._root = root
        self._bodyparts = bodyparts
        self._frame = None

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
     
        self._frame.destroy()









    def initialize_bodyparts(self):
        self.stretching_service.initialize_bodypart_table()

    def add_bodypart(self, name, stretch):
        self.stretching_service.add_bodypart(name, stretch)
        self.stretching_service.add_combination(name, stretch)

    def show_bodyparts(self):
        bodyparts = self.stretching_service.get_all_bodyparts()
        return bodyparts



class BodypartView:
    def __init__(self, root):
        self._root = root
        self._stretching_service = StretchingService()
        self._bodypart_list_view = None
        self._bodypart_list_frame = None
        self._frame = None

        self._initialize()

    def pack(self):
        
        self._frame.pack(fill=constants.X)


    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        self._initialize_bodypart_list()


    def _initialize_bodypart_list(self):

        bodyparts = self._stretching_service.get_all_bodyparts()
        print(bodyparts)
        self._bodypart_list_view = BodypartListView(
            self._bodypart_list_frame,
            bodyparts
        )


        self._bodypart_list_view.pack()

"""