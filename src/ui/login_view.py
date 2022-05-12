from services.stretching_services import StretchingService

error_username = "Tapahtui virhe, valitse uusi käyttäjänimi"
error_too_short = "käyttäjätunnuksen minimipituus 3 merkkiä"
registering_succesful = "Käyttäjätunnus luotu."


class LoginView:
    def __init__(self):
        self.stretching_service = StretchingService()



    """
    def create_new_user(self, username, password, admin):
        user = self.stretching_service.create_new_user(
            username, password, admin)
        if user == error_too_short:
            return error_too_short
        if not user:
            return error_username
        else:
            return registering_succesful

    """