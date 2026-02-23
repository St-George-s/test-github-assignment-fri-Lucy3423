from movie import Movie 

# FR1 user class to store details and manage the user's watched movies
class User:
    def __init__(self):
        # FR2 array of objects to store details about mulitples films watched by the user. 
        self.watched_movies:Movie = []
    

    # FR11 - a method to add a movie to the watched list
    def update_watched_movies_list(self, cur):
        name = self.input_movie_name()
        rating = self.input_movie_rating()

        # retrieve information on the film from the table
        found, director, genre = self.retrieve_movie_details(cur, name)


        not_recorded = self.check_presence_of_movie(name)

        if not_recorded:
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
            print(f"{name} has already been recorded in your watched movies list \n")    

    
    # method to input the movie name to be added and check for the prescence of text
    def input_movie_name(self):
        movieName = input("Movie name: ")
        # FR9 - keyboard validation to check that the user has entered a movie name
        while movieName == "":
            movieName = input("Movie name:")
        
        movieName.title()
        movieName.strip()
        return movieName


    # method to input the movie rating
    def input_movie_rating(self):
        rating = input("How would you rate the film (1-5): ")
        # FR14 - check the rating is within the correct range
        while len(rating)!=1 or int(rating) < 1 or int(rating) > 5:                           
            rating = int(input("How would you rate this film (1-5): "))
        return rating


    def retrieve_movie_details(self, cur, movieName):
        print(movieName)
        sql = """SELECT director, genre FROM movies WHERE movieName = %s;"""
        cur.execute(sql, (movieName,))
        rows = cur.fetchall()

        print("")
        if len(rows) > 0:
            found = True
            for director, genre in rows:
                return found, director, genre
        else:
            found = False
            return found, "", ""
    

    # a method to check whether movie to add has already been recorded in the user's watched movies list
    def check_presence_of_movie(self, movieName):
        not_recorded = True
        for movie in self.watched_movies:
            if movie.name == movieName:
                not_recorded = False 
        return not_recorded
    



    # FR3 - a method to apply a bubble sort to the user's watched movies list
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
                    # FR4 - if so, swap those elements. This will change the order of the movies in the user's watched movies so that they are ordered by highest rating rather than most recent addition
                    self.watched_movies[i], self.watched_movies[i+1] =  self.watched_movies[i+1], self.watched_movies[i]
                    # swap has happened, so additional swap may be required. reset swapped to true
                    swapped = True 
            # change the range of the list (ignore later elements as they have already been sorted)
            n -= 1
        return self
    
    # FR10 - a method to apply the bubble sort (FR3 and FR4) to the watched movies and then display all the movies from highest to lowest rating
    def view_watched_movies(self):
        # first check whether any movies have been recorded yet
        if self.watched_movies:
            print("Order movies by highest rating \n")
            # order the movies using FR3 for descending order
            self.bubble_sort()
            for movie in self.watched_movies:
                print(
    f"""Name: {movie.name}
    Director: {movie.director}
    Genre: {movie.genre}
    Rating: {int(movie.rating)}
    """)
        # if there are no movies recorded
        else:
            print("No movies have been recorded yet")


    # FR12 - a method to recommend the user more movies based on the most commonly occuring director and genre in their watched movies list
    def recommend_movies(self, cur):
        # check whether any movies have been recorded yet
        if len(self.watched_movies) == 0:
            print("You have not recorded any movies yet. At least one is required to request a recommendation")
            request_available = False 

        elif len(self.watched_movies) <= 5:
            # apply bubble sort
            self.bubble_sort()
            request_available = True 
            top_movies = self.watched_movies
        else:
            # assume that there are more than 5 movies recorded
            # apply the bubble sort
            self.bubble_sort()
            # limit the list to the top 5 results
            top_movies = self.watched_movies[:5]
            request_available = True
        
        # check whether the program is able to recommend the user movies
        if request_available:
            # 1 identify the most popular genre
            top_genre = self.identify_top_genre(top_movies)
            top_director = self.identify_top_director(top_movies)
            # 2 call the methods for the queries 
            self.display_genre_movies(top_genre, cur)
            self.display_director_movies(top_director, cur)
            print("") # this is just a line break

    # A method to loop through the user's watched movies and identify the most popular genre using dictionaries to count each genre occurence
    def identify_top_genre(self, top_movies):
        # define an empty dictionary: genre_name : genre_count
        genres = {}

        # iterate through the top_movies
        for movie in top_movies:
            # check whether the current genre has already been recorded in the dictionary
            if movie.genre not in genres:
                # add the genre as a new key, with value initially set to 1
                genres[movie.genre] = 1
            # if it has already been recorded, increment the count instead
            else:
                genres[movie.genre] += 1
        
        # now all the values are stored in the dictionary, identify genre with highest count
        top_genre_name = ""
        top_genre_count = 0

        # iterate through dictionary
        for key, value in genres.items():
            # if the current genre occurs more than the current top_genre, replace top_genre details 
            if value > top_genre_count:
                top_genre_name = key 
                top_genre_count = value 

        return top_genre_name

    # A method to loop through the user's watched movies and identify the most popular director using dictionaries to count each director occurence
    def identify_top_director(self, top_movies):
        # define an empty dictionary: name_of_director : director_count
        directors = {}

        # iterate through the top_movies
        for movie in top_movies:
            # check whether the current director has already been recorded in the dictionary
            if movie.director not in directors:
                # add the director as a new key, with value initially set to 1
                directors[movie.director] = 1
            # if it has already been recorded, increment the count instead
            else:
                directors[movie.director] += 1
        
        # now all the values are stored in the dictionary, identify the director with highest count
        top_director_name = ""
        top_director_count = 0

        # iterate through dictionary
        for key, value in directors.items():
            # if the current director occurs more than the current top director, replace top director details 
            if value > top_director_count:
                top_director_name = key 
                top_director_count = value 
        
        return top_director_name

    # FR16 - a method to perform a query to display movies from the database which have the same genre as the user's top genre
    def display_genre_movies(self, top_genre, cur):
        print("")
        print(f"Searching for movie with your top genre: {top_genre}")
        sql = """SELECT movieName, director, genre FROM movies WHERE genre LIKE %s LIMIT 5;"""
        cur.execute(sql, (top_genre,))
        rows = cur.fetchall()

        print("Why not try...")
        for movieName, director, genre in rows:
            print(f"Name: {movieName}, Director: {director}, Genre: {genre}")

    # FR17 - a method to perform a query to search for movies with the same director as the user's most popular director
    def display_director_movies(self, top_director, cur):
        print("")
        print(f"Searching for movies by your top director: {top_director}")
        sql = """SELECT movieName, director, genre FROM movies WHERE director LIKE %s LIMIT 5;"""
        cur.execute(sql, (top_director,))
        rows = cur.fetchall()

        print("Why not try...")
        for movieName, director, genre in rows:
            print(f"Name: {movieName}, Director: {director}, Genre: {genre}")

            


