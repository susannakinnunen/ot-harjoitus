from tkinter import Tk
from ui.ui import UI
from initialize_database import initialize_database
from initialize_csv import InitializeCSV


INITIAL_BODYPART = "takareisi"
INITIAL_STRETCH = "eteenpäintaivutus"
INITIAL_STRETCH_INSTRUCTIONS = """Ota hieman lantiota leveämpi haaraasento. \
Pidä polvet rentoina.Hengitä sisään ja ulos hengityksellä \
lähde viemään ylävartaloa alas kohti jalkoja. \
Anna pään roikkua rentona. Koukista polvia niin \
paljon, että voit olla venytyksessä mahdollisimman rennosti."""


def main():
    initialize_database()
    InitializeCSV(INITIAL_BODYPART, INITIAL_STRETCH,
                  INITIAL_STRETCH_INSTRUCTIONS)
    window = Tk()
    window.title("Stretching application")

    ui_view = UI(window)
    ui_view.start()

    window.mainloop()


if __name__ == "__main__":
    main()
