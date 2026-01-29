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
[2] Request recommendations
[3] View watched movies list
[4] End program""")

def get_menu_choice():
    while True: 
        choice = input('Enter service (1-4): ')
        if int(choice) <= 4 and int(choice) > 0:
            break
        else:
            choice = input("Enter service (1-4): ")
    return choice

# End User 1: add movie to watched movies list
def update_watched_movies(user:User, cur):
    new_movie_name, rating = user.update_watched_movies_list()
    new_movie_name = new_movie_name.title()

    # check the movie is not already recorded before progressing
    director, genre = retrieve_movie_details(cur, new_movie_name, rating)
    user.watched_movies.append(Movie(new_movie_name, genre, director, rating))
    return user

def retrieve_movie_details(cur, movieName, rating):
    print(movieName)
    sql = """SELECT director, genre FROM movies WHERE movieName = %s;"""
    cur.execute(sql, (movieName,))
    rows = cur.fetchall()

    print("")
    print('Fetching movie data \n')
    for director, genre in rows:
        return director, genre


def main():
    con,cur = open_db()
    # create a new instance of the User class to store details about the user's watched movies
    user = User()
    while True:
        display_menu()
        choice = get_menu_choice()
        if choice == "1":
            update_watched_movies(user, cur)
            print("New movie added \n")
            
            for movie in user.watched_movies:
                print(f"name: {movie.name}")
                print(f"genre: {movie.genre}")
                print(f"director: {movie.director}")
                print(f"rating: {str(movie.rating)}")
        else:
            break
        


if __name__ == '__main__':
    main()
user = User()
con,cur = open_db()
update_watched_movies(user, cur)