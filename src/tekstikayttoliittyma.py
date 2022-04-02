import bodyparts

def ui():

    while True:

        komento = input("Tulosta kehonosat painamalla 'A', lopeta painamalla 'X' \n")
        if komento == "A":
           bodypart_list()
        if komento == "X":
            break


def bodypart_list():
    bodypart_list = bodyparts.get_all()
    print(bodypart_list)


if __name__ == "__main__":
    ui()