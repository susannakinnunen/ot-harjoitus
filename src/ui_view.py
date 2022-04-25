from unicodedata import name
from services.stretching_services import StretchingService
from initialize_database import initialize_database

#commands
first_view = "Luo uusi käyttäjätunnus painamalla 'R', kirjaudu sisään painamalla 'K', lopeta painamalla 'X' \n"
R = "Rekisteröidy luomalla käyttäjätunnus ja salasana"
käyttäjätunnus = "käyttäjätunnus:"
salasana = "salasana:"
K = "Kirjaudu sisään"
second_view = "Tulosta kehonosat painamalla 'A', kirjaudu ulos ja poistu painamalla 'X' \n"
third_view = "Tulosta kehonosat painamalla 'A', hae venytys painamalla 'B', lisää venytys painamalla 'V', kirjaudu ulos ja poistu painamalla 'X' \n"
bodypart_query = "Kirjoita listassa annettu kehonosa:"
new_stretch = "Lisää venytyksen nimi:"
new_description = "Lisää venytysohjeet:"
bodypart_match = "Lisää kehonosa, johon venytys kohdentuu (syötä kaikki kirjaimet pienillä kirjaimilla) (Paina X poistuaksesi):"
registering_succesful = "Käyttäjätunnus luotu."
error = "Tapahtui virhe, kirjoita uudelleen."
error_username = "Tapahtui virhe, valitse uusi käyttäjänimi"
error_login = "Väärä käyttäjätunnus tai salasana"
stretchname = "venytyksen nimi"
instuctions = "ohjeet"


class UI:
    def __init__(self):
        initialize_database()
        self.io = InputOutput()
        self.bodypart_view = BodypartView()
        self.stretch_view = StretchView()
        self.user_view = UserView()
        self.bodypart_view.initialize_bodyparts()
        self.stretch_view.initialize_stretches()
        self.start_tekstikayttoliittyma()

    def start_tekstikayttoliittyma(self):
        
        while True:

            komento = self.io.user_input(first_view)

            if komento == "R":
                username = self.io.user_input(käyttäjätunnus)
                password = self.io.user_input(salasana)
                create = self.user_view.create_new_user(username,password)
                self.io.print_out(create)
                
            if komento == "K":
                self.io.print_out(K)
                username = self.io.user_input(käyttäjätunnus)
                password = self.io.user_input(salasana)
                login = self.user_view.login(username,password)
                
                if not login:
                   self.io.print_out(error_login) 
                
                else:
                    self.io.print_out(f"Olet kirjautunut sisään tunnuksella {username}")
                    while True:

                        komento = self.io.user_input(second_view)
                        
                        if komento == "V":
                            stretch = self.io.user_input(new_stretch)
                            description = self.io.user_input(new_description)
                            self.stretch_view.add_stretch(stretch, description)

                            while True:
                                matching_bodypart = self.io.user_input(bodypart_match)
                                if matching_bodypart == "X":
                                    break
                                self.bodypart_view.add_bodypart(matching_bodypart,stretch)

                        if komento == "A":

                            bodypart_list = self.bodypart_view.show_bodyparts()
                            for bodypart in bodypart_list:
                                self.io.print_out(bodypart)
                         

                            while True:
                                
                                komento = self.io.user_input(third_view)  

                                if komento == "A":
                                    bodypart_list = self.bodypart_view.show_bodyparts()
                                    for bodypart in bodypart_list:
                                        self.io.print_out(bodypart)

                                if komento == "B":
                                    bodypart_name = self.io.user_input(bodypart_query)
                                    stretch = self.stretch_view.show_stretch(bodypart_name)
                                    for s in stretch:
                                        self.io.print_out(f"{stretchname}:{s[0]}")
                                        self.io.print_out(f"{instuctions}:{s[1]}")

                                if komento == "V":
                                    stretch = self.io.user_input(new_stretch)
                                    description = self.io.user_input(new_description)
                                    self.stretch_view.add_stretch(stretch, description)

                                    while True:
                                        matching_bodypart = self.io.user_input(bodypart_match)
                                        if matching_bodypart == "X":
                                            break
                                        self.bodypart_view.add_bodypart(matching_bodypart,stretch)                                    
                                        
                                if komento == "X":
                                    break

                        if komento == "X":
                            break
            
            if komento == "X":
                break
        
class BodypartView:
    def __init__(self):
        self.stretching_service = StretchingService()

    def initialize_bodyparts(self):
        self.stretching_service.initialize_bodypart_table()

    def add_bodypart(self,name,stretch):
        self.stretching_service.add_bodypart(name,stretch)
        self.stretching_service.add_combination(name,stretch)

    def show_bodyparts(self):
        bodyparts = self.stretching_service.get_all_bodyparts()
        return bodyparts

class StretchView:
    def __init__(self):
        self.streching_service = StretchingService()

    def initialize_stretches(self):
        self.streching_service.initialize_stretch_table()
        self.streching_service.combine_stretches_and_bodyparts()


    def show_stretch(self,bodypart):
        stretch = self.streching_service.show_stretch(bodypart)
        if stretch == False:
            return error
        return stretch

    def add_stretch(self,stretch,description):
        self.streching_service.add_stretch(stretch,description)


class UserView:
    def __init__(self):
        self.stretching_service = StretchingService()

    def create_new_user(self,username,password):
        user = self.stretching_service.create_new_user(username,password)
        if not user:
            return error_username
        else:
            return registering_succesful

    def login(self,username,password):
        user = self.stretching_service.login(username,password)
        if not user:
            return False
        else:
            return True

class InputOutput:
    def __init__(self):
        self.test = 1

    def user_input(self,text):
        return input(text)

    def print_out(self, text):
        return print(text)      


if __name__ == "__main__":
    UI()
    