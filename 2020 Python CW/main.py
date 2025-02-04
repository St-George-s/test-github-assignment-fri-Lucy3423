import csv

# parallel arrays

forenames = []
surnames = []
categories = []
passwords = []



def read_in_data():
    with open("members.txt", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            forenames.append(row[0])
            surnames.append(row[1])
            categories.append(row[2])
            passwords.append(row[3])
    
    return forenames, surnames, categories, passwords



# main program
forenames, surnames, categories, passwords = read_in_data()
print(forenames)