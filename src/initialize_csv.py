from repositories.bodypart_repository import BodypartRepository
from repositories.stretch_repository import StretchRepository


class InitializeCSV():
    def __init__(self, bodypart_name, stretch_name, stretch_instructions):
        self.bodypart_name = bodypart_name
        self.strech_name = stretch_name
        self.strech_instructions = stretch_instructions
        self.bodypart_repository = BodypartRepository()
        self.stretch_repository = StretchRepository()
        self.initialize_bodyparts_csv()
        self.initialize_stretches_csv()

    def initialize_bodyparts_csv(self):
        self.bodypart_repository.delete_all()
        self.bodypart_repository.write_bodyparts_to_file_and_database(
            self.bodypart_name, self.strech_name)

    def initialize_stretches_csv(self):
        self.stretch_repository.delete_all()
        self.stretch_repository.write_stretches_to_file_and_database(
            self.strech_name, self.strech_instructions)
