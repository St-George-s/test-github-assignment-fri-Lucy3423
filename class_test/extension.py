#import csv
import csv

# load the data from the csv file into the parallel arrays
#return the updated arrays
def load_data():
    #define the arrays
    game_titles = []
    genres = []
    age_ratings = []
    platforms = []

    #open the file to read as file
    with open("game_platform_data.csv", "r") as file:

        reader = csv.reader(file)

        #skip header in csv file as there's no useful data in line 1
        header = next(reader)

        #loop over each row in reader to append to the arrays
        for row in reader:
            #append to arrays
            game_titles.append(row[0]) 
            genres.append(row[1])
            age_ratings.append(int(row[2])) # rating cast as int for later comparisons
            platforms.append(row[3]) 

    #return these lists to the main program
    return game_titles, genres, age_ratings, platforms 


#count function to count how many games of a specific genre are suitable for under 18s
# pass through previous arrays as well as the specific genre we want to check for
def count_suitable_games(genre_to_check, game_titles, genres, age_ratings):

    #keeps track of occurences of valid games with ratings under 18
    count = 0

    #loop over each titles in game_titles with index
    for index in range(len(game_titles)):

        # condition, if rating less than 18 and current genre is the same as the one we are searching for, increment count by 1 and print that title
        if genres[index] == genre_to_check and age_ratings[index] < 18:
            print(game_titles[index])
            count += 1
    
    # add the end of the sub-routine, now return value of total occurences
    print(f"Total occurences of {genre_to_check} games with ratings under 18 = {str(count)}")
    

#new function to count occurences of particular game genre with rating less than 18 and for specific platform
# take in all predfined lists, and genre and platform to check for
def platform_genre_count(genre_to_check, platform_to_check, game_titles, genres, age_ratings, platforms):
    
    with open("games.txt", "w") as file:
        #same as before
        count = 0
        
        #loop over each titles in game_titles with index
        for index in range(len(game_titles)):

        # condition, if rating less than 18 and current genre is the same as the one we are searching for, increment count by 1 and print that title
        # now additional parameter to check for platform too
            if genres[index] == genre_to_check and age_ratings[index] < 18 and platforms[index] == platform_to_check:
                #title, platform
                file.write(game_titles[index] + "-")
                file.write(platforms[index])
                count += 1






#main function to run the program
def main():
    #define arrays which will store data from csv file - game_data.csv
    game_titles, genres, age_ratings, platforms = load_data()

    #count occurences of a specific genre, e.g Fantasy - because there are two games 
    count = count_suitable_games("Fantasy", game_titles, genres, age_ratings)

    #expected outcome
    #Castle Quest
    #Fantasy RPG
    #count = 2

    x = platform_genre_count("Fantasy", "PC", game_titles, genres, age_ratings, platforms)

#call main() to start/run the program
main()