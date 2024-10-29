#import csv to read from the csv files
import csv

#define a class for the orders
class Orders:
    def __init__(self, customer_id, customer_name, product_purchased, amount_spent, category):
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.product_purchased = product_purchased
        self.amount_spent = amount_spent
        self.category = category

#read form the file to put the data from the csv file into the array of records - Orders using a function

def load_data():
    #define empty list called orders which will be used to store all the data from the csv file
    orders = []

    #define the csv file as file to iterate through it

    with open("ordersExtended.csv", "r") as file:

        #begin reading all the date from the file and store in variable called reader
        reader = csv.reader(file )

        #skip over the header (first line) in the file as this line does not contain any data
        header = next(reader)

        #iterate through the list reader and append each individual item from each row as a parameter/property of the Orders class 
        for row in reader:
            new_order = Orders(
            int(row[0]), # customer id
            row[1], # customer name
            row[2], # product purchased
            row[3], # amount spent
            row[4] # category
            )

            # amount spent

            #add new order to the list of all orders
            orders.append(new_order)
    
    # now return updated list of orders
    return orders


#define a function to identify the customer which spent the most on a tv
#it will need to take thorugh the list orders as a parameter to access the data from the csv

def find_max_order_with_tv(orders):
    #begin looking at the first line in the csv file to compare other orders (rows) to later
    max_order = orders[0]

    #loop over the reamining orders from the list
    for order in range(1, len(orders)):

        #check current order against these requirements
        #for chekcing if the product was a tv, since the product names are quite long and also containg other words like the make, simply only check that the string "TV" is present in the longer product name
        if "TV" in orders[order].product_purchased and orders[order].amount_spent > max_order.amount_spent:

            #if they meet the requirments update the max_order from line 46 with the current order
            max_order = orders[order]
    
    #display max price after iterating over the whole list
    print(f"Max amount spent on a TV was £{max_order.amount_spent}")


#new function to determine whether purchase is legitimate for a discount
def determine_discount(orders):

    #open file to write new info to it
    with open("Discounts.txt", "w") as file:
        for order in orders:
            file.write(str(order.customer_id) + "-")
            file.write(order.product_purchased[:3] + "-")

            if order.customer_id % 5 == 0:
                file.write("DISCOUNT CODE ASSIGNED \n")
            else:
                file.write("NO DISCOUNT \n")
            







#define a function call main to run the program
def main():
    # call load_data to export all data from orders.csv to make it available to use in the main program
    orders = load_data()

    #call the find max order with tv function to identify the maximum amount spent on a tv from the orders list
    find_max_order_with_tv(orders)

    determine_discount(orders)

#call the function main to start the program
main()
    
