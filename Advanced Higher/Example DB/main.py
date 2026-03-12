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


# to test FR3+FR4 and FR10
# create new instance of User class

# TEST 1 - When no movies have been recorded
# call FR3+FR4 to sort the list by the highest rating
# print("TEST 1")
# user.bubble_sort()

# call FR10 to display the newly sorted list
# user.view_watched_movies()

# TEST 2 - When 1 movies has been recorded
# print("TEST 2")
# user.watched_movies.append(Movie("Finding Nemo", "Andrew Stanton", "comedy", 3))

# call FR3+FR4 to sort the list by the highest rating
# user.bubble_sort()

# call FR10 to display the newly sorted list
# user.view_watched_movies()


# TEST 3 - When movie than one movie has been recorded
# print("TEST 3")
# # add two predefined movies to their watched movies list
# user.watched_movies.append(Movie("Finding Nemo", "comedy", "Andrew Stanton",  3))
# user.watched_movies.append(Movie("Frozen", "comedy", "Jennifer Lee", 5))
# user.watched_movies.append(Movie("Love Actually", "romance", "Richard Curtis", 4))

# call FR3+FR4 to sort the list by the highest rating
# user.bubble_sort()
# 
# call FR10 to display the newly sorted list
# user.view_watched_movies()




# FR6 - a query to retreive informatio non a movie input by the user

# FR1 User class to store details about the user's watches movies
# 1 - create an empty instance
# user = User()

# 2 - to check that the attribute has been loaded, print the length. Should be 0 as watched_movies is inially []
# print(len(user.watched_movies))



# FR7 - validation to check that input movie name exits in the movie table
# 1 -  open the table
# conn, cur = open_db()

# 2 - create instance of User class
# user = User()

# call method to retrieve details of the movie, by entering a pre-defined movie name 
# (usually this will be input earlier in the program)
# found, director, genre = user.retrieve_movie_details(cur, "Turning Red")
# print(found) # False when not found and vise versa

# when movie name input is in the the movie table
# found, director, genre = user.retrieve_movie_details(cur, "Love Actually")
# print(found)


# FR6 - a query to display the director and genre for an input movie

# user = User()
# conn, cur = open_db()

# FR9 - validation to check for presence of text when user inputs a movie name
# user.input_movie_name()

# FR10 - a method to display the user's watched movies list by order of highest rated

# test 1 - no movies recorded yet
# print("TEST 1")
# user.view_watched_movies()


# test 2 - one movie recorded
# print("TEST 2")
# user.watched_movies.append(Movie('Frozen', "Jennifer Lee", "comedy", 5))
# user.view_watched_movies()

# test 3 - more than one movie recorded
# print("TEST 3")
# user.watched_movies.append(Movie('Frozen', "Jennifer Lee", "comedy", 5))
# user.watched_movies.append(Movie('Frozen 2', "Jennifer Lee", "comedy", 3))

# user.view_watched_movies()


# user = User()
# conn, cur = open_db()


# # FR11 - a method to add movies to the user's watched movies list
# user.update_watched_movies_list(cur)
