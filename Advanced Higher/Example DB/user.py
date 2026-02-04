from movie import Movie 

# FR1 user class to store details bout hte user's watched movies

class User:
    def __init__(self):
        # FR2 array of objects to store details about mulitples films watched by the user. 
        self.watched_movies:Movie = []
    

    # FR11 - a method to add a movie to the watched list
    def update_watched_movies_list(self, cur):
        # input the name of the movie to be added
        name = self.input_movie_name()
        # capatalise the name of the movie
        name = name.title()
        # input the rating for that movie
        rating = self.input_movie_rating()

        # retrieve information on the film from the table
        found, director, genre = self.retrieve_movie_details(cur, name)

        # check whether the movie has been found
        if found:
            print("Movie has been found! \n")
            # add new movie to the watched movies list
            self.watched_movies.append(Movie(name, genre, director, rating))
            print("Updating watched movies list... \n")
            print(f"""Name {name}
Director: {director}
Genre: {genre}
Rating: {str(rating)}""")
        else:
            print("Unable to find movie")
        

        
        

        

    # method to input the movie name to be added and check for the prescence of text
    def input_movie_name(self):
        movieName = input("Movie name: ")
        # FR9 - keyboard validation to check that the user has entered a movie name
        while movieName == "":
            movieName = input("Movie name:")
        
        return movieName

    # method to input the movie rating
    def input_movie_rating(self):
        rating = input("How would you rate the film (1-5): ")
        # FR14 - check the rating is within the correct range
        while len(rating)!=1 or int(rating) < 1 or int(rating) > 5:                           
            rating = int(input("How would you rate this film (1-5): "))
            # error here when checking for the presence of data
        return rating

    def retrieve_movie_details(self, cur, movieName):
        print(movieName)
        sql = """SELECT director, genre FROM movies WHERE movieName = %s;"""
        cur.execute(sql, (movieName,))
        rows = cur.fetchall()

        print("")
        print('Fetching movie data \n')
        # ERROR
        # for director, genre in rows:
        #     if director == "" or genre == "":
        #         found = False
        #     else:
        #         found = True 
        # print()
        if len(rows) > 0:
            found = True
            for director, genre in rows:
                return found, director, genre
        else:
            found = False
            return found, "", ""

        
            


