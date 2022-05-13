from ui.register_login_view import RegisterLoginView
from ui.register_view import RegisterView
from ui.bodypart_view import BodypartView
from ui.stretch_view import StretchView
from ui.stretch_view_admin import StretchViewAdmin
from ui.bodypart_view_admin import BodypartViewAdmin
from ui.admin_view import AdminView
from ui.login_view import LoginView
from services.stretching_services import StretchingService

class UI:
    def __init__(self,root):     
        self._root = root
        self._current_view = None
        self.stretching_service = StretchingService()
        self.stretching_service.combine_stretches_and_bodyparts()

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
            self._root, self._show_register_view, self._show_login_view)

        self._current_view.pack()

    def _show_register_view(self):
        self._hide_current_view()

        self._current_view = RegisterView(self._root, self._show_bodypart_view, self._show_bodypart_view_admin)
       
        self._current_view.pack()
    
    def _show_login_view(self):
        self._hide_current_view()

        self._current_view = LoginView(self._root, self._show_bodypart_view, self._show_bodypart_view_admin)

        self._current_view.pack()

    def _show_bodypart_view(self):
        self._hide_current_view()
        self._current_view = BodypartView(self._root, self._show_stretch_view,self._show_register_login_view)
        self._current_view.pack()

    def _show_bodypart_view_admin(self):
        self._hide_current_view()
        self._current_view = BodypartViewAdmin(self._root,self._show_stretch_view_admin,self._show_admin_view, self._show_register_login_view) #lisää show_stretch_view_admin
        self._current_view.pack()

    def _show_stretch_view_admin(self,bodypart):
        self._hide_current_view()
        self._current_view = StretchViewAdmin(self._root, bodypart,self._show_bodypart_view_admin)

        self._current_view.pack()

    def _show_stretch_view(self,bodypart):
        self._hide_current_view()
        self._current_view = StretchViewAdmin(self._root, bodypart,self._show_bodypart_view)

        self._current_view.pack()

   
    def _show_admin_view(self):
        self._hide_current_view()
        self._current_view = AdminView(self._root, self._show_bodypart_view_admin)
        self._current_view.pack()
   
