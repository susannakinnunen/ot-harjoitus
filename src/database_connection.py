from os import getenv
import sqlite3
import os


database_filename = getenv("database_filename")

dirname = os.path.dirname(__file__)
connection = sqlite3.connect(os.path.join(dirname, str(database_filename)))
connection.isolation_level = None
connection.row_factory = sqlite3.Row


def get_database_connection():
    return connection
