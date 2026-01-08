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
          [1] Display all movie names
          [2] Display all genres
          [3] Exit program""")

def get_menu_choice():
    while True: 
        choice = input('Enter service (1-3): ')
        if int(choice) <= 3 and int(choice) > 0:
            break 
    return choice

def display_movie_names(cur):
    sql = """
    SELECT movieName FROM movies;    
    """
    cur.execute(sql)
    rows = cur.fetchall()

    print("")
    print('Fetching all movie names \n')
    for movieName in rows:
        print(f"Movie: {movieName}")

def display_movie_genres(cur):
    sql = """
    SELECT genre FROM movies;
"""
    cur.execute(sql)
    rows = cur.fetchall()

    print("")
    print("Fetching all genres")

    for genre in rows:
        print(f"Genre: {genre}")

def main():
    con,cur = open_db()
    # create a new instance of the User class to store details about the user's watched movies
    user = User()
    while True:
        display_menu()
        choice = get_menu_choice()
        if choice == '1':
            display_movie_names(cur)
        elif choice == '2':
            display_movie_genres(cur)
        else:
            print("Bye")
            break
        


if __name__ == '__main__':
    main()

