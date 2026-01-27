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
    return choice

# End User 1: add movie to watched movies list
def update_watched_movies(user:User, cur):
    user.update_watched_movies_list()
       
    retrieve_movie_details(cur)


    return user

def retrieve_movie_details(cur):
    sql = """
    SELECT director, genre FROM movies WHERE movieName = %s;    
    """
    cur.execute(sql, ("Frozen",))
    rows = cur.fetchall()

    print("")
    print('Fetching all movie names \n')
    for movieName, director in rows:
        print(f"Movie: {movieName}")
        print(f"Director: {director}")


# def main():
#     con,cur = open_db()
#     # create a new instance of the User class to store details about the user's watched movies
#     user = User()
#     while True:
#         display_menu()
#         choice = get_menu_choice()
#         if choice == "1":
#             update_watched_movies(user, cur)
            
            
#             for movie in user.watched_movies:
#                 print(f"""
#                 name: {movie.name}
#                 genre: {movie.genre}
#                 director: {movie.director}
#                 rating: {str(movie.rating)}
#                 """)
#         elif choice == "2":
#             test_query(cur)
#         else:
#             break
        


# if __name__ == '__main__':
#     main()
user = User()
con,cur = open_db()
update_watched_movies(user, cur)