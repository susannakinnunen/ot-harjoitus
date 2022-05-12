"""
from ui.input_output import InputOutput
from ui.bodypart_view import BodypartView
from ui.stretch_view import StretchView
from ui.login_view import LoginView
"""
from ui.register_login_view import RegisterLoginView
from ui.register_view import RegisterView
from ui.bodypart_view import BodypartView
from ui.stretch_view import StretchView
from ui.bodypart_view_admin import BodypartViewAdmin
from ui.admin_view import AdminView
#from tkinter import Tk, ttk

# commands


class UI:
    def __init__(self,root):
        #self.io = InputOutput()
        #self.register_view = RegisterView()

       
        self._root = root
        self._current_view = None

    def start(self):
        """Käynnistää käyttöliittymän."""
        self._show_register_login_view()


    def _hide_current_view(self):
        if self._current_view != None:
            self._current_view.destroy()

        self._current_view = None


    def _show_register_login_view(self):
        self._hide_current_view()

        self._current_view = RegisterLoginView(
            self._root, self._show_register_view)

        self._current_view.pack()

    def _show_register_view(self):
        self._hide_current_view()

        self._current_view = RegisterView(self._root, self._show_bodypart_view, self._show_bodypart_view_admin)
       
        self._current_view.pack()

    def _show_bodypart_view(self):
        self._hide_current_view()
        self._current_view = BodypartView(self._root, self._show_stretch_view)
        self._current_view.pack()

    def _show_bodypart_view_admin(self):
        self._hide_current_view()
        self._current_view = BodypartViewAdmin(self._root,self._show_stretch_view,self._show_admin_view) #lisää show_stretch_view_admin
        self._current_view.pack()

    def _show_stretch_view(self,bodypart):
        self._hide_current_view()
        self._current_view = StretchView(self._root, bodypart) #lisää "edellinen"napikka

        self._current_view.pack()
   
    def _show_admin_view(self):
        self._hide_current_view()
        self._current_view = AdminView(self._root, self._show_bodypart_view_admin)
        self._current_view.pack()
   
   
    """
    def _handle_create_new_user_button(self):
        self._show_register_view()

    def _handle_register_button(self):
        self._show_bodypart_view()

    def _handle_bodypart_button(self,bodypart):
        self._show_stretch_view(bodypart)
    """