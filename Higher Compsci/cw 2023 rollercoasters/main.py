# import csv
import csv


# a sub-routine to read in the data from the attraction text file into paralle array
def read_data():
    # define parallel arrays
    attractions = []
    categories = []
    visitors = []
    days_open = []
    heights = []
    # open file to read in data
    with open("attractions.csv", "r") as file:
        reader = csv.reader(file)
        # iterate over each line in file and append to parallel arrays
        for row in reader:
            attractions.append(row[0])
            categories.append(row[1])
            visitors.append(int(row[2]))
            days_open.append(int(row[3]))
            heights.append(row[4])
    # return parallel arrays to main program
    return attractions, categories, visitors, days_open, heights



# function to identify which rides have the most and least number of visitors
def identify_most_and_least_popular_rides(attractions, visitors):
    # identify most popular rides as first items in visitors list initially
    most_popular_ride = visitors[0]
    least_popular_ride = visitors[0]
    # iterate over each attraction to compare number of visitors to the most and least popular rides previously identified
    for index in range(1, len(attractions)):
        if visitors[index] > most_popular_ride:
            most_popular_ride = visitors[index]
        if visitors[index] < least_popular_ride:
            least_popular_ride = visitors[index]
    
    # return the results
    for x in range(len(visitors)):
        if visitors[x] == most_popular_ride:
            print(f"The most popular ride is {attractions[x]}")
        if visitors[x] == least_popular_ride:
            print(f"The least popular ride is {attractions[x]}")


# a subroutine to write roller coasters in need of service within 7 days to a file
def write_rides_in_need_of_service(attractions, categories, days_open):
    # 3.1 Create ‘service.csv’ file by opening file
    with open("service.csv", "w") as file:    
        # 3.2 Loop for each attraction
        for index in range(len(attractions)):
            # 3.3 If current category is ‘Roller Coaster’ then
                if categories[index] == "Roller Coaster":
                    # 3.4 Set days to current daysOpen modulus 90
                        days = days_open[index] % 90
                     # 3.5 If (90 – days) is less than or equal to 7 then
                        if (90 - days) >= 7:
                            # 3.6 Write current attraction to file
                             file.write(attractions[index])

                           


# main program
# define parallel arrays
attractions, categories, visitors, days_open, heights = read_data()
identify_most_and_least_popular_rides(attractions, visitors)
write_rides_in_need_of_service(attractions, categories, days_open)
