#import csv
import csv

# load the data from the csv file into the parallel arrays
#return the updated arrays
def load_data():
    #define the arrays
    game_titles = []
    genres = []
    age_ratings = []

    #open the file to read as file
    with open("game_data.csv", "r") as file:

        #define reader 
        reader = csv.reader(file)

        #skip header in csv file as there's no useful data in line 1
        header = next(reader)

        #loop over each row in reader to append to the arrays
        for row in reader:
            #append to arrays
            game_titles.append(row[0]) # game title
            genres.append(row[1]) # genre
            age_ratings.append(int(row[2])) # rating cast as int for later comparisons

    #return these lists to the main program
    return game_titles, genres, age_ratings 


#count function to count how many games of a specific genre are suitable for under 18s
# pass through previous arrays as well as the specific genre we want to check for
def count_suitable_games(genre_to_check, game_titles, genres, age_ratings):

    #set count initially to 0 - keeps track of occurences of valid games with ratings under 18
    count = 0

    #loop over each titles in game_titles with index

    for index in range(len(game_titles)):

        # condition, if rating less than 18 and current genre is the same as the one we are searching for, increment count by 1 and print that title
        if genres[index] == genre_to_check and age_ratings[index] < 18:
            
            #print the game title which meets these requirements
            print(game_titles[index])

            # increment count by 1
            count += 1
    
    # add the end of the sub-routine, now return value of total occurences
    print(f"Total occurences of {genre_to_check} games with ratings under 18 = {str(count)}")


#main function to run the program

def main():
    #define arrays which will store data from csv file - game_data.csv
    game_titles, genres, age_ratings = load_data()

    #count occurences of a specific genre, e.g Fantasy - because there are two games 
    count_suitable_games("Fantasy", game_titles, genres, age_ratings)

    #expected outcome
    #Castle Quest
    #Fantasy RPG
    #count = 2

#call main() to start/run the program
main()