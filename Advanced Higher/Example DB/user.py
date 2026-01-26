from movie import Movie 

# FR1 user class to store details bout hte user's watched movies

class User:
    def __init__(self):
        # FR2 array of objects to store details about mulitples films watched by the user. 
        self.watched_movies:Movie = []
    

    # FR11 - a method to add a movie to the watched list
    def update_watched_movies_list(self):
        # input the name of the movie to be added
        name = self.input_movie_name()
        rating = self.input_movie_rating()

        # !!!!!
        # no current implementation of db - not final implementation
        self.watched_movies.append(Movie(name, 'fantasy', "Tim Burton", rating))
        return self
        

        

    # method to input the movie name to be added and check for the prescence of text
    def input_movie_name(self):
        movieName = input("Movie name: ")
        # FR9 - keyboard validation to check that the user has entered a movie name
        while movieName == "":
            movieName = input("Movie name:")
        
        return movieName

    # method to input the movie rating
    def input_movie_rating(self):
        rating = int(input("How would you rate the film (1-5): "))
        # FR14 - check the rating is within the correct range
        while rating < 1 or rating > 5 or str(rating) == "":
            rating = int(input("How would you rate this film (1-5): "))
        
        return rating

