import csv

class Sighting:
    def __init__(self, town, mammal, date, age):
        self.town = town
        self.mammal = mammal
        self.date = date
        self.age = age

def load_data():
    sightings = []
    with open("mammals.txt", "r") as file:
        reader = csv.reader(file)
        for row in reader:

            new_sighting = Sighting(
            row[0],
            row[1],
            row[2],
            int(row[3]))

            sightings.append(new_sighting)

    return sightings


def oldest_sighter(sightings):
    oldestSighting = sightings[0]
    for sighting in sightings:
        if sighting.age > oldestSighting.age:
            oldestSighting = sighting 
    
    print("Oldest age is: " + str(oldestSighting.age))


def display_sighting_dates(sightings):

#     3.1 Ask user to enter town
    # 3.2 Call a function to return a string input that starts with an upper-case character

    town = input("Enter Town: ").title()

    # 3.3 Ask user to enter mammal
    # 3.4 Call a function to return a string input that starts with an upper-case character
    mammal = input("Enter a mammal: ").title()
    
    
    
    # 3.5 Display “The dates of sightings were:”

    print(f"The dates of the sightings for a {mammal} in {town} were: ")

    for sighting in sightings:
        if sighting.town == town and sighting.mammal == mammal:
            print(sighting.date)

        
    
    # 3.6 Start loop for each sighting in array of records
    # 3.7 If sighting matches entered town and mammal then
    # 3.8 Display date
    # 3.9 End if
    # 3.10 End loop

def count_sightings(sightings):
    # 4.1 Set dayToCount to first date in sightings array
    day_to_count = sightings[0]

    # 4.2 Set count to 1
    count = 1

    # 4.3 Start loop from second record to end of sightings array
    for sighting in 


    # 4.4 If date in current record is the same as dayToCount then
    # 4.5 Add 1 to count
    # 4.6 Else
    # 4.7 Display dayToCount and count
    # 4.8 Set dayToCount to date in current record
    # 4.9 Set count to 1
    # 4.10 End if
    # 4.11 End loop
    # 4.12 Display dayToCount and count




sightings = load_data()
oldest_sighter(sightings)
display_sighting_dates(sightings)
