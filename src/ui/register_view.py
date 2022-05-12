from tkinter import ttk, StringVar, constants
from services.stretching_services import StretchingService

class RegisterView:
    def __init__(self, root, handle_register_button, handle_register_button_admin):
        self._root = root
        self._handle_register_button = handle_register_button
        self._handle_register_button_admin = handle_register_button_admin
        self._frame = None

        self.stretching_service = StretchingService()
        
        self._initialize()

    def destroy(self):
        print("nyt tuhotaan rekisteri")
        self._frame.destroy()

    
    def _register_handler(self):
        username = self._username_entry.get()
        password = self._password_entry.get()
        error_too_short = "käyttäjätunnuksen minimipituus 3 merkkiä"
        if len(username) < 3:
            print(error_too_short)

        self.stretching_service.create_new_user(username,password)
        admin = self.stretching_service.check_if_admin(username)
        if admin:
            self._handle_register_button_admin()
        else:
            self._handle_register_button()
        
        
    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        heading_label = ttk.Label(master=self._frame, text="Luo uusi käyttäjätunnus ja salasana.")
        
        username_label = ttk.Label(master=self._frame, text="Käyttäjätunnus")
        self._username_entry = ttk.Entry(master=self._frame)

        password_label = ttk.Label(master=self._frame, text="Salasana")
        self._password_entry = ttk.Entry(master=self._frame)

        register_button = ttk.Button(master=self._frame, text="Rekisteröidy",command=self._register_handler)

        heading_label.grid(row=0,column=0,columnspan=2)
        
        username_label.grid(row=1,column=0)
        self._username_entry.grid(row=1,column=1)

        password_label.grid(row=2,column=0)
        self._password_entry.grid(row=2,column=1)

        register_button.grid(row=3,column=0)

    
    def pack(self):
        """"Näyttää näkymän."""
        self._frame.pack(fill=constants.X)