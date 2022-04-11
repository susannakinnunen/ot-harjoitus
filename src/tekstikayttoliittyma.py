from initialize_database import initialize_database
import database_connection
import bodyparts
import stretches
import bodypart_stretch
import users


class Tekstikayttoliittyma:
    def __init__(self):
        self.io = InputOutput()

    def ui(self):

        while True:

            U = users.User(database_connection.get_database_connection())

            komento = self.io.user_input(
                "Luo uusi käyttäjätunnus painamalla 'R', kirjaudu sisään painamalla 'K', lopeta painamalla 'X' \n")

            if komento == "R":
                self.io.print_out(
                    "Rekisteröidy luomalla käyttäjätunnus ja salasana")
                username = self.io.user_input("käyttäjätunnus:")
                password = self.io.user_input("salasana:")
                U.add_user(username, password)

            if komento == "K":
                self.io.print_out("Kirjaudu sisään")
                username = self.io.user_input("käyttäjätunnus:")
                password = self.io.user_input("salasana:")

                login = U.login(username, password)

                if login:

                    while True:

                        komento = self.io.user_input(
                            "Tulosta kehonosat painamalla 'A', hae venytys painamalla 'B', kirjaudu ulos ja poistu painamalla 'X' \n")
                        if komento == "A":

                            bodypart_list = bodyparts.find_all()
                            for bodypart in bodypart_list:
                                self.io.print_out(bodypart)

                        if komento == "B":
                            bodypart_name = self.io.user_input(
                                "Kirjoita listassa annettu kehonosa:")
                            stretch = stretches.find_stretch(bodypart_name)
                            self.io.print_out(stretch)

                        if komento == "X":
                            break

            if komento == "X":
                break


class InputOutput:
    def __init__(self):
        self.test = 1

    def user_input(self, text):
        return input(text)

    def print_out(self, text):
        return print(text)


if __name__ == "__main__":
    initialize_database()

    B = bodyparts.Bodypart(database_connection.get_database_connection())
    B.add_bodypart("takareisi")
    bodypart_name = "takareisi"

    S = stretches.Stretch(database_connection.get_database_connection())
    stretch_name = "Eteenpäintaivutus seisaaltaan"
    S.add_stretch(stretch_name, "Ota hieman lantiota leveämpi haaraasento. Pidä polvet rentoina.Hengitä sisään ja ulos hengityksellä lähde viemään ylävartaloa alas kohti jalkoja. Anna pään roikkua rentona. Koukista polvia niin paljon, että voit olla venytyksessä mahdollisimman rennosti.")

    BS = bodypart_stretch.BodypartStretch(
        database_connection.get_database_connection())
    BS.add_combination(bodypart_name, stretch_name)

    T = Tekstikayttoliittyma()
    T.ui()
