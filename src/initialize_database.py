from database_connection import get_database_connection


def drop_tables(connection):
    cursor = connection.cursor()

    sql_bodyparts = "DROP TABLE IF EXISTS Bodyparts;"
    cursor.execute(sql_bodyparts)
    connection.commit()

    sql_stretches = "DROP TABLE IF EXISTS Stretches;"
    cursor.execute(sql_stretches)
    connection.commit()

    sql_bodypart_stretches = "DROP TABLE IF EXISTS BodypartStretches;"
    cursor.execute(sql_bodypart_stretches)
    connection.commit()

    sql_users = "DROP TABLE IF EXISTS Users;"
    cursor.execute(sql_users)
    connection.commit()

def create_tables(connection):
    cursor = connection.cursor()
    sql_bodyparts = "CREATE TABLE Bodyparts (id INTEGER PRIMARY KEY, name TEXT);"
    cursor.execute(sql_bodyparts)
    connection.commit()

    sql_stretches = "CREATE TABLE Stretches (id INTEGER PRIMARY KEY, name TEXT, description TEXT);"
    cursor.execute(sql_stretches)
    connection.commit()

    sql_bodypart_stretch = "CREATE TABLE BodypartStretches" \
        "(id INTEGER PRIMARY KEY, bodypart_id INTEGER REFERENCES Bodyparts," \
        "stretch_id INTEGER REFERENCES Stretches);"
    cursor.execute(sql_bodypart_stretch)
    connection.commit()


    sql_users = "CREATE TABLE Users (id INTEGER PRIMARY KEY, username TEXT UNIQUE, password TEXT)"
    cursor.execute(sql_users)
    connection.commit()


def initialize_database_tests():
    connection = get_database_connection()
    drop_tables(connection)
    create_tables(connection)


def initialize_database():
    connection = get_database_connection()
    drop_tables(connection)
    create_tables(connection)