class Bodypart:
    """ Kehonosaolion luova luokka.
    """

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return str(self.name)
