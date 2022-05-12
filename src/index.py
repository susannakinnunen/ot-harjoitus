from tkinter import Tk
from ui.ui_uusi import UI
from initialize_database import initialize_database
from initialize_csv import InitializeCSV

initial_bodypart = "takareisi"
initial_stretch = "eteenpäintaivutus"
initial_stretch_intstructions = "Ota hieman lantiota leveämpi haaraasento. Pidä polvet rentoina.Hengitä sisään ja ulos hengityksellä lähde viemään ylävartaloa alas kohti jalkoja. Anna pään roikkua rentona. Koukista polvia niin paljon, että voit olla venytyksessä mahdollisimman rennosti."


def main():
    initialize_database()
    InitializeCSV(initial_bodypart, initial_stretch,initial_stretch_intstructions)
    window = Tk()
    window.title("Stretching application")


    ui_view = UI(window)
    ui_view.start()

    window.mainloop()


if __name__ == "__main__":
    main()