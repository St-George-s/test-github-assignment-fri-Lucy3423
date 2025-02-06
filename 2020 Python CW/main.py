import csv

# parallel arrays

forenames = []
surnames = []
categories = []
passwords = []

def check_for_valid_password():
# initailly valid password has not yet been entered
    valid = False

    # continue to input passwrod until it meet the requirements
    while valid == False:
        password = input("Password: ")

        # check against the conditions 

        # first character is capital and last character is a symbol
        if (ord(password[0]) >= 65 and ord(password[0]) <= 90) and (ord(password[-1]) >= 35 and ord(password[-1]) <= 37):

            # if both of these requirement are met, the password is valid
            print("Valid Password Entered")
            valid = True
        
        else:
            print("Invalid Password, Please Try Again")

        
        # return valid password at the end of the function
    return password

        




def get_new_member():

    # input new data: first name, last name and category they belong to
    forename = input("First Name: ")
    surname = input("Surname: ")
    category = input("Category (Junior, Adult, Senior): ")

    # call check_for_valid_password() function to input a new password
    password = check_for_valid_password()

    return forename, surname, category, password

def read_in_data(forename, surname, category, password):

    # read in data from file members.txt and store information in parallel arrays
    with open("members.txt", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            forenames.append(row[0])
            surnames.append(row[1])
            categories.append(row[2])
            passwords.append(row[3])
        
        # add details of new member to parallel arrays
        forenames.append(forename)
        surnames.append(surname)
        categories.append(category)
        passwords.append(password)

        # display the information for each memeber
        print("Our Member Are:")
        for index in range(len(forenames)):
            print(f"{forenames[index]} {surnames[index]} {categories[index]}")
    
    return forenames, surnames, categories, passwords

def count_number_members_for_each_category(categories):
    number_of_juniors = 0 
    number_of_adults = 0
    number_of_seniors = 0
    total_number_members = 0
    for category in categories:
        total_number_members += 1
        if category == "Junior":
            number_of_juniors += 1
        elif category == "Adult":
            number_of_adults += 1
        else:
            number_of_seniors += 1
    
    # print the results 
    print(f"Total current membership is {str(total_number_members)}")
    print(f"There are currently {str(number_of_adults)} Adults members")
    print(f"There are currently {str(number_of_juniors)} Junior members")
    print(f"There are currently {str(number_of_seniors)} Senior members")



# main program
forename, surname, category, password = get_new_member()

forenames, surnames, categories, passwords = read_in_data(forename, surname, category, password)

count_number_members_for_each_category(categories)