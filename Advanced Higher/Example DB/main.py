import mysql.connector
from dataclasses import dataclass
from typing import List, Optional

from user import User 
from movie import Movie

DB_CONFIG = {
    "host": "127.0.0.1",
    "user": "student",
    "password": "studentpw",
    "database": "project1",
    "port": 3306
}

def open_db():
    conn = mysql.connector.connect(**DB_CONFIG)
    cur = conn.cursor()
    return conn, cur

def display_menu():
    print("""Movie recommendation service
[1] Add movie to watched movies list
[2] View watched movies list
[3] Request recommendations
[4] End program""")

def get_menu_choice():
    choice = input("Enter service (1-4): ")
    while len(choice) != 1 or int(choice) < 1 or int(choice) > 4:
        print("Invalid input") 
        print("Choice must be between (1-4)")
        choice = input("Enter service (1-4): ")
    return choice


def main():
    con,cur = open_db()
    # create a new instance of the User class to store details about the user's watched movies
    user = User()
    while True:
        display_menu()
        choice = get_menu_choice()
        # EU1 - add movie to watched movies list
        if choice == "1":
            user.update_watched_movies_list(cur)
        elif choice == "2":
            print("Sorting list")
            user.view_watched_movies()    
        elif choice == "3":
            user.recommend_movies(cur)
        else:
            print("Byeee")
            break
        


if __name__ == '__main__':
    main()
user = User()
con,cur = open_db()
