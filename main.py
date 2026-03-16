import csv

# set up a class called Order to store the different attributes of each order

class Order:
    def __init__(self, order_num, date, email, option, cost, rating):
        self.order_num = order_num
        self.date = date
        self.email = email
        self.option = option
        self.cost = cost
        self.rating = rating


# A fucntion to read in the data from the text file and store it in an array of records called orders
def read_in_data():
    # create an array to hold all the orders
    orders = []
    # open up the file
    with open("orders.txt", "r") as file:
        reader = csv.reader(file)
        # iterate over each row
        for row in reader:
            # create a new order object using the information on each line
            new_order = Order(
                row[0], #orderNum 
                row[1], #date
                row[2], #email
                row[3], #option
                float(row[4]), #cost
                int(row[5])  #rating
            )
            # add new order to the list of orders
            orders.append(new_order)
    return orders


# identify which customer left the first 5-star rating for a given month - input orders
def identify_first_5_star_rating(orders):
    position = -1
    index = 0
    # 2.3 Ask user to enter month to search for
    chosen_month = input("Enter the first three letters of the month to serach: ")
    # until winning customer has been identified, iterate over each record
    while (position == -1) and (index < len(orders)):
        if (orders[index].date[3:6] == chosen_month) and (orders[index].rating == 5):
            position = index
        else:
            index += 1
    return position




# create a function to write the details of the winning customer to a text file called 'winningCustomer.txt' - input orders
def write_winner_to_file(orders, position):
    # 3.1 Open new file ‘winningCustomer.txt’
    with open("winningCustomer.txt", "w") as file:
        if position >= 0:
            # 3.3 Write winning order number, email and cost to ‘winningCustomer.txt’
            file.write(orders[position].order_num + ", ")
            file.write(orders[position].email + ", ")
            file.write(str(orders[position].cost))
        else:
            # 3.5 if no winner has been identified,
            file.write("No winner")


# a subroutine to count the number of orders delivered and collected 
def countOption(orders):
    # define variables to hold the number of each order category. They should both initially be set to 0
    number_of_delivered_orders = 0
    number_of_collected_orders = 0
    # interate over each record to count number of orders delivered and collected
    for order in orders:
        if order.option == "Delivery":
            number_of_delivered_orders += 1
        else:
            number_of_collected_orders +=1
    return number_of_delivered_orders, number_of_collected_orders


# a subroutine to display the total number of orders collected and delivered using the pre-defined sub-routine called countOption
def display_number_of_orders_delivered_and_collected(orders):
    # 4.1. 4.2 Call countOption function to return the number of orders delievered and collected
    number_of_delivered_orders, number_of_collected_orders = countOption(orders)
    # 4.3 Output results
    print(f"Total number of orders delivered to date: {str(number_of_delivered_orders)}")
    print(f"Total number of orders collected to date: {str(number_of_collected_orders)}")



# MAIN PROGRAM
orders = read_in_data()
position = identify_first_5_star_rating(orders)
write_winner_to_file(orders, position)
display_number_of_orders_delivered_and_collected(orders)
