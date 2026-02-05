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

        # check if movie has already been recorded
        valid = self.check_presence_of_movie(name)

        if valid:
            # check whether the movie has been found
            if found:
                print("Movie has been found! \n")
                # add new movie to the watched movies list
                self.watched_movies.append(Movie(name, genre, director, rating))
                print("Updating watched movies list... \n")
                print(f"""
Name {name}
Director: {director}
Genre: {genre}
Rating: {str(rating)}""")
            else:
                print("Unable to find movie")
        else:
            print(f"{name} has already been recorded in your watched movies list")    

    
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
    

    # method to check whether movie to add has already been recorded
    def check_presence_of_movie(self, movieName):
        valid = True
        for movie in self.watched_movies:
            if movie.name == movieName:
                valid = False 
        return valid
    


    # EU3 - view watched movies list in descending order by rating

    # a method to apply a bubble sort to the user's watched movies list
    # FR3
    # LOGIC - I'm not sure if this is the right algorithm to use for descending order, but it does work
    def bubble_sort(self):
        # find len of list
        n = len(self.watched_movies)
        # set swapped initially True
        swapped = True 

        # while swapps are still happening
        while swapped:
            # addition swap won't necessarily be needed, so reset
            swapped = False
            # iterate through the list from first to second to last index (top of list already sorted)
            for i in range(n-1):
                # check whether current element is less than next one
                if self.watched_movies[i].rating < self.watched_movies[i+1].rating:
                    # swap those elements
                    self.watched_movies[i], self.watched_movies[i+1] =  self.watched_movies[i+1], self.watched_movies[i]
                    # swap has happened, so additional swap may be required. reset swapped to true
                    swapped = True 
            # change the range of the list (ignore later elements as they have already been sorted)
            n -= 1
        return self
    
    # FR10 
    def view_watched_movies(self):
        # first order the movies using FR3
        self.bubble_sort
        for movie in self.watched_movies:
            print(f"""
Name: {movie.name}
Director: {movie.director}
Genre: {movie.genre}
Rating: {int(movie.rating)}""")

    

                

        
            


