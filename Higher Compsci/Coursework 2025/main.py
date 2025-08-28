# set up a class called Order to store the different attributes of each order

class Order:
    def __init__(self, order_num, date, email, option, cost, rating):
        self.order_num = order_num
        self.date = date
        self.email = email
        self.option = option
        self.cost = cost
        self.rating = rating


def read_in_data():
    orders = []
    with open("orders.txt", "r") as file:
        reader = file.read()
        for row in reader:
            new_order = Order(
                row[0],
                row[1],
                row[2],
                row[3],
                row[4],
                row[5]
            )
            orders.append(new_order)
    return orders

            



















# A fucntion to read in the data from the text file and store it in an array of records called orders
def read_in_datax():
    # create an array to hold all the orders
    orders = []
    # open up the file
    with open("orders.txt", "r") as file:

        # iterate over the content of the file, row by row
        for row in file:
            # create a new order using the information on each line
            new_order = Order(
                row[0],
                row[1],
                row[2],
                row[3],
                row[4],
                row[5]
            )
            # add new order to the list of orders
            orders.append(new_order)
    
    # return the list of orders to the main program
    return orders



# identify which customer left the first 5-star rating for a given month - input orders
# Identify first 5-star rating

    # return the index at which this customer's details can be found at



# create a function to write the details of the winning customer to a text file - input orders
# NO returns




# a function to display total stats for orders delivered and collected
# NO returns 


# MAIN PROGRAM
orders = read_in_data()
