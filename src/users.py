import database_connection
from initialize_database import initialize_database

class User:
    def __init__(self,connection):
        self._connection = connection

    def add_user(self, username, password):
        cursor = self._connection.cursor()

        cursor.execute(
            "INSERT INTO Users (username,password) VALUES (:username, :password)", {"username": username, "password": password })

        self._connection.commit()

        return f"Lisätty käyttäjätunnus {username} ja salasana {password}"

    def login(self, username, password):
        user = self.find_by_username(username)
        
        if user == None or user[1] != password:
            print("Väärä käyttäjätunnus tai salasana")
            return False
        
        else:
            print(f"Olet kirjautunut sisään tunnuksella {username}")
            return True

    def find_by_username(self,username):
        cursor = self._connection.cursor()

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