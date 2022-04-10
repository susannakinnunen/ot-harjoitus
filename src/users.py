import database_connection
from initialize_database import initialize_database

def add_user(username, password):
    connection = database_connection.get_database_connection()
    cursor = connection.cursor()

    cursor.execute(
        "INSERT INTO Users (username,password) VALUES (:username, :password)", {"username": username, "password": password })

    connection.commit()

def login(username, password):
    user = find_by_username(username)
    
    if user == None or user[1] != password:
        print("Väärä käyttäjätunnus tai salasana")
    
    else:
        print(f"Olet kirjautunut sisään tunnuksella {username}")

def find_by_username(username):
    connection = database_connection.get_database_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM Users WHERE username=:username", {"username":username})

    row = cursor.fetchone()
    
    if row == None:
         return None

    return row['username'], row['password']

"""
if __name__ == "__main__":
    initialize_database()
    username = "ojokilo"
    password = "nana"
    add_user(username, password)
    login(username,password)
    login(username,"pooo")
    login("kii",password)
"""