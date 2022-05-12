from repositories.bodypart_repository import BodypartRepository
from repositories.stretch_repository import StretchRepository
from repositories.bodypart_stretch_repository import BodypartStretchRepository
from repositories.user_repository import UserRepository


class StretchingService:
    """ Sovelluslogiikasta vastaava luokka
    """

    def __init__(self):
        self.bodypart_repository = BodypartRepository()
        self.stretch_repository = StretchRepository()
        self.bodypart_stretch_repository = BodypartStretchRepository()
        self.user_repository = UserRepository()

    def add_bodypart(self, name, stretch):
        return self.bodypart_repository.write_bodyparts_to_file_and_database(
            name, stretch)

    def add_stretch(self, bodypart_name, description):
        return self.stretch_repository.write_stretches_to_file_and_database(
            bodypart_name, description)

    def add_combination(self, name, stretch):
        return self.bodypart_stretch_repository.add_combination(name, stretch)

    def get_all_bodyparts(self):
        return self.bodypart_repository.find_all()

    def initialize_bodypart_table(self):
        bodypart_list = self.bodypart_repository.get_bodyparts_from_file()
        for bodypart in bodypart_list:
            self.bodypart_repository.add_bodypart(bodypart)

    def initialize_stretch_table(self):
        self.stretch_repository.get_stretches_from_file()

    def get_all_stretches(self):
        return self.stretch_repository.find_all()

    def show_stretch(self, bodypart):
        return self.stretch_repository.find_by_bodypart(bodypart)

    def combine_stretches_and_bodyparts(self):
        self.bodypart_stretch_repository.get_bodyparts_and_stretches_from_file()

    def create_new_user(self, username, password):
        admin = self.check_if_admin(username)
        user = self.user_repository.add_user(username, password, admin)
        if not user:
            return False
        return True

    def login(self, username, password):
        login = self.user_repository.login(username, password)
        return login

    def check_if_admin(self, username):
        if username == "admin":
            return True
        else:
            return False
