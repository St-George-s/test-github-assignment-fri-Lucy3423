import mysql.connector
from dataclasses import dataclass
from typing import List, Optional

from user import User 
from movie import Movie
# ^^^^ importations 

DB_CONFIG = {
    "host": "127.0.0.1",
    "user": "student",
    "password": "studentpw",
    "database": "project1",
    "port": 3306
}

# a function to open up the database, and return variables enabling us to open the database at other parts of the program
def open_db():
    conn = mysql.connector.connect(**DB_CONFIG)
    cur = conn.cursor()
    return conn, cur


# a function to display the menu and the available choices/activities the user can do while using the program
def display_menu():
    print("""Movie recommendation service
[1] Add movie to watched movies list
[2] View watched movies list
[3] Request recommendations
[4] End program""")

# a function to input the user's option choice
def get_menu_choice():
    choice = input("Enter service (1-4): ")
    # validate whether the chosen menu choice within the correct range
    while len(choice) != 1 or int(choice) < 1 or int(choice) > 4:
        print("Invalid input") 
        print("Choice must be between (1-4)")
        choice = input("Enter service (1-4): ")
    return choice

# a function to operate the whole movie recommendation service. all methods and function from other parts of the program are called within this function
def main():
    con,cur = open_db()
    # create a new instance of the User class to store details about the user's watched movies
    user = User()
    # keep the service live until the user selects option 4 to end the program
    while True:
        display_menu()
        choice = get_menu_choice()
        if choice == "1": # Add movie to watched movies list
            user.update_watched_movies_list(cur)
        elif choice == "2": # View watched movies list
            print("Sorting list")
            user.view_watched_movies() 
        elif choice == "3": # Request recommendations
            user.recommend_movies(cur)
        else: # End program
            print("Byeee")
            break
        

# call the function main() to run the program
if __name__ == '__main__':
    main()
