import database_connection
from initialize_database import initialize_database
import bodyparts
import stretches
import bodypart_stretch
import users


def ui():

    komento = ("Luo uusi käyttäjätunnus painamalla 'R', kirjaudu sisään painamalla 'K'")
    
    if komento == "R":
        print("Rekisteröidy luomalla käyttäjätunnus ja salasana")
        username = input("käyttätunnus:")
        password = input("salasana:")
        users.add_user(username, password)

        print(username)
    
    if komento == "K":
        print("Kirjaudu sisään")
        username = ("käyttäjätunnus:")
        password = ("salasana:")

        users.check_user(username,password)

    while True:

        komento = input(
            "Tulosta kehonosat painamalla 'A', hae venytys painamalla 'B', lopeta painamalla 'X' \n")
        if komento == "A":

            bodypart_list = bodyparts.find_all()
            for bodypart in bodypart_list:
                print(bodypart)

        if komento == "B":
            bodypart_name = input("Kirjoita listassa annettu kehonosa:")
            stretch = stretches.find_stretch(bodypart_name)
            print(stretch)

        if komento == "X":
            break


if __name__ == "__main__":
    initialize_database()
    B = bodyparts.Bodypart(database_connection.get_database_connection())
    B.add_bodypart("takareisi")
    bodypart_name = "takareisi"

    S = stretches.Stretch(database_connection.get_database_connection())
    stretch_name = "Eteenpäintaivutus seisaaltaan"
    S.add_stretch(stretch_name, "Ota hieman lantiota leveämpi haaraasento. Pidä polvet rentoina.Hengita sisään ja ulos hengityksellä lähde viemään ylävartaloa alas kohti jalkoja. Anna pään roikkua rentona. Koukista polvia niin paljon, että voit olla venytyksessä mahdollisimman rennosti.")

    BS = bodypart_stretch.BodypartStretch(
        database_connection.get_database_connection())
    BS.add_combination(bodypart_name, stretch_name)

    ui()
