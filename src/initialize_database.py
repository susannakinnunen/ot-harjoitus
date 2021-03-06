from database_connection import get_database_connection


def drop_tables(connection):
    """Poistaa tietokantataulut."""
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
    """Luo tietokantataulut."""
    cursor = connection.cursor()
    sql_bodyparts = "CREATE TABLE Bodyparts (id INTEGER PRIMARY KEY, name TEXT UNIQUE);"
    cursor.execute(sql_bodyparts)
    connection.commit()

    sql_stretches = "CREATE TABLE Stretches (id INTEGER PRIMARY KEY," \
                    "name TEXT UNIQUE, description TEXT UNIQUE);"
    cursor.execute(sql_stretches)
    connection.commit()

    sql_bodypart_stretch = "CREATE TABLE BodypartStretches" \
        "(id INTEGER PRIMARY KEY, bodypart_id INTEGER REFERENCES Bodyparts," \
        "stretch_id INTEGER REFERENCES Stretches);"
    cursor.execute(sql_bodypart_stretch)
    connection.commit()

    sql_users = "CREATE TABLE Users (id INTEGER PRIMARY KEY, " \
        "username TEXT UNIQUE, password TEXT, is_admin BOOLEAN)"
    cursor.execute(sql_users)
    connection.commit()


def initialize_database():
    """Alustaa tietokantataulut"""
    connection = get_database_connection()
    drop_tables(connection)
    create_tables(connection)
