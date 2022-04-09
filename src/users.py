import database_connection



def add_user(username, password):
    connection = database_connection.get_database_connection()
    cursor = connection.cursor()

    cursor.execute(
        "INSERT INTO Users (username,password) VALUES (:username, :password)", {"username": username, "password": password })

    connection.commit()