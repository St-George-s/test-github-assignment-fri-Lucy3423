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
        # iterate over the content of the file, row by row
        for row in reader:
            # create a new order using the information on each line
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
    # close the file
    
    # return the list of orders to the main program
    return orders



# identify which customer left the first 5-star rating for a given month - input orders
# Identify first 5-star rating
def identify_first_5_star_rating(orders):
    # 2.1 set position to -1
    position = -1
    # 2.2 Set index to 0
    index = 0

    # 2.3 Ask user to enter month to search for
    chosen_month = input("Enter the first three letter sof the month to serach:  ")

    # 2.4 While position is -1 and index is less than the length of the array
    while (position == -1) and (index < len(orders)):
        # 2.5 If current month is equal to searched month and current rating is 5 then
        if (orders[index].date[3:6] == chosen_month) and (orders[index].rating == 5):

            # 2.6 Set position to index
            position = index

        # 2.7 End if
        else:
            # 2.8 Add 1 to index
            index += 1
    
    # 2.10 return position
    return position




# create a function to write the details of the winning customer to a text file - input orders
def write_winner_to_file(orders, position):
    # 3.1 Open new file ‘winningCustomer.txt’
    with open("winningCustomer.txt", "w") as file:
        # 3.2 If position is 0 or above then
        if position >= 0:
            # 3.3 Write winning order number, email and cost to ‘winningCustomer.txt’
            file.write(orders[position].order_num + ", ")
            file.write(orders[position].email + ", ")
            file.write(str(orders[position].cost))

        # 3.4 Else
        else:
            # 3.5 Write ‘No winner’ to ‘winningCustomer.txt
            file.write("No winner")
    
    # 3.6 close the file


# a subroutine to count the number of orders delivered and collected 
def countOption(orders):
    # define variables to hold the number of each order category. they should both initially be set to 0
    number_of_delivered_orders = 0
    number_of_collected_orders = 0

    # loop over each record (order) in the orders list. Look at the position to allow extraction of information in each record.
    for order in orders:
        # check whether the current option is 'Delivered'
        if order.option == "Delivery":
            # increment the count varaible for number of orders delivered by 1
            number_of_delivered_orders += 1
        # if the order has not be deliverd, it will have been collected, therefore,
        else:
            # increment the count varaible for the number of orders collected by 1 instead
            number_of_collected_orders +=1
    
    # At the end of the subroutine, the total count for each of the options should be returned to the main program
    return number_of_delivered_orders, number_of_collected_orders






# a subroutine to display the total number of orders collected and delivered using pre-defined sub-routines which count the stats. 
def display_number_of_orders_delivered_and_collected(orders):
    # 4.1 Call countOption function to return the number of orders delievered 
    # 4.2 Call countOption function to reutrn the number of orders collected
    number_of_delivered_orders, number_of_collected_orders = countOption(orders)

    # 4.3 Output the total number of orders delievered 
    # 4.4 Output the total number of orderes collected 
    # print the results
    print(f"Total number of orders delivered to date: {str(number_of_delivered_orders)}")
    print(f"Total number of orders collected to date: {str(number_of_collected_orders)}")

    # since the results have been displayed within the function, there is nothing to return to the main program.





# MAIN PROGRAM
orders = read_in_data()
position = identify_first_5_star_rating(orders)
write_winner_to_file(orders, position)
display_number_of_orders_delivered_and_collected(orders)
