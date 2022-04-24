from dnaio import FastaFormatError
from repositories.bodypart_repository import BodypartRepository
from repositories.stretch_repository import StretchRepository
from repositories.bodypart_stretch_repository import BodypartStretchRepository
from repositories.user_repository import UserRepository

class StretchingService:
    def __init__(self):
        self.bodypart_repository = BodypartRepository()
        self.stretch_repository = StretchRepository()
        self.bodypart_stretch_repository = BodypartStretchRepository()
        self.user_repository = UserRepository()

    def add_bodypart(self,name):
        return self.bodypart_repository.add_bodypart(name)

    def get_all_bodyparts(self):
        self.bodypart_repository.get_bodyparts_from_file()
        return self.bodypart_repository.find_all()

    def initialize_bodypart_table(self):
        self.bodypart_repository.get_bodyparts_from_file()
    
    def initialize_stretch_table(self):
        self.stretch_repository.get_stretches_from_file()
    
    def get_all_stretches(self):
        return self.stretch_repository.find_all()

    def show_stretch(self,bodypart):
        return self.stretch_repository.find_by_bodypart(bodypart)

    def combine_stretches_and_bodyparts(self):
        self.bodypart_stretch_repository.get_bodyparts_and_stretches_from_file()

    def create_new_user(self, username, password):
        user = self.user_repository.add_user(username,password)
        if not user:
            return False
        else:
            return True

    def login(self, username, password):
        login = self.user_repository.login(username,password)
        return login