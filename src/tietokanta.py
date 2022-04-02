# Ei vielä oikeaa yhteyttä tietokantaan, harjoitustietokanta

class Tietokanta:
    def __init__(self):
        self.list_bodyparts = ["takareisi", "etureisi", "pohje"]

    def __str__(self):
        return f"Kehonosat: {self.list_bodyparts}"