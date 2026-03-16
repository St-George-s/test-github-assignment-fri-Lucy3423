import csv

class Sighting:
    def __init__(self, town, mammal, date, age):
        self.town = town
        self.mammal = mammal
        self.date = date
        self.age = age

#define the first function to read all the data from the text file and create instances of each sighting to save to a larger list

def load_data():
    #create a list to store all the sightings and thier info in
    sightings = []

    #open the file to read the data from it
    with open("mammals.txt", "r") as file:
        reader = csv.reader(file)

        #loop over each row in th file
        for row in reader:

            #create a sighting instance/object by passing through the corresponding variables of each sighting as actual parameters
            new_sighting = Sighting(
            row[0],
            row[1],
            row[2],
            int(row[3]))

            #add this new instance of a Sighting called new_sighting to the sightings list as defined previously
            sightings.append(new_sighting)

    #return the updated list of all sightings to the main program so they can be accessed elsewhere in the program
    return sightings


#function to find the oldest sighter from the list of sightings

def oldest_sighter(sightings):

    #start at the first index in the list and define this as the oldest sighter found so far
    oldestSighting = sightings[0]

    #loop thorugh each individual sighting in our list of sightings
    for sighting in sightings:

        #compare whether the age of the sighter from the currently interated sighting from the sightings list is greater that our assumed greatest age as defined on line 42 as oldestSighting
        if sighting.age > oldestSighting.age:

            #if this new sighting's sighter is older than the previously predicted one, we should update the variable, so later interated sightings are compared to this value instead.
            oldestSighting = sighting 
    
    #at the end of the loop, we should return the age of the oldest sighter
    
    print(f"Oldest age is: {str(oldestSighting.age)}")


def display_sighting_dates(sightings):

#     3.1 Ask user to enter town
    # 3.2 Call a function to return a string input that starts with an upper-case character

    town = input("Enter Town: ")
    town = town[0].upper() + town[1:]

    # 3.3 Ask user to enter mammal
    # 3.4 Call a function to return a string input that starts with an upper-case character
    mammal = input("Enter a mammal: ")
    mammal = mammal[0].upper() + mammal[1:]
    
    
    
    # 3.5 Display “The dates of sightings were:”

    print(f"The dates of the sightings for a {mammal} in {town} were: ")

    #iterate through each sighting in the list of sightings
    for sighting in sightings:

        #determine whether twon and mammal in that sighting matches up with input town and mammal by the user
        if sighting.town == town and sighting.mammal == mammal:

            #print valid date from the sighting to show that the input values by the user where recorded on this date
            print(sighting.date)



def count_sightings(sightings):
    # 4.1 Set dayToCount to first date in sightings array
    dayToCount = sightings[0].date

    # 4.2 Set count to 1
    count = 1

    # 4.3 Start loop from second record to end of sightings array
    for sighting in range(1, len(sightings)):

        # 4.4 If date in current record is the same as dayToCount then
        if sightings[sighting].date == dayToCount:

            # 4.5 Add 1 to count
            count += 1

        # 4.6 Else

        else:
            # 4.7 Display dayToCount and count
            print(f"{str(dayToCount)} occured {str(count)} times.")

            # 4.8 Set dayToCount to date in current record

            dayToCount = sightings[sighting].date

            # 4.9 Set count to 1
            count = 1
        
            #end the loop
        #display dayToCount and its corresponding count




    # 4.12 Display dayToCount and count
    print(f"{str(dayToCount)} occured {str(count)} times.")



sightings = load_data()
print(sightings[0].age)
oldest_sighter(sightings)
# display_sighting_dates(sightings)
count_sightings(sightings)
