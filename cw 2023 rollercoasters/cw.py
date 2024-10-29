import csv

name_list = []
category_list = []
vistors_list = []
daysOpen_list = []
height_list = []

def get_data(): 
    with open("./attractions.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            name_list.append(row[0]) 
            category_list.append(row[1]) 
            vistors_list.append(int(row[2])) 
            daysOpen_list.append(int(row[3])) 

            height_to_add = row[4]
            height_to_add = height_to_add[:-1]
            height_list.append(float(height_to_add))

    return name_list, category_list, vistors_list, daysOpen_list, height_list


#find the least popular destiantion
def least_popular(name_list, visitor_list):
    #start at the first indexes
    min_name = name_list[0]
    min_visitors = visitor_list[0]
    #loop through each number of visorts
    for index in range(len(visitor_list)):
        #if number currently at is less than currently focused one, replace to compare future numbers to
        if visitor_list[index] < min_visitors:
            min_visitors = visitor_list[index]
            min_name = name_list[index]
    
    return min_name

def most_popular(name_list, visitor_list):
    #start at the first indexes
    max_name = name_list[0]
    max_visitors = int(visitor_list[0])

    #loop through each number of visorts
    for index in range(len(visitor_list)):
        #if number currently at is less than currently focused one, replace to compare future numbers to
        if visitor_list[index] > max_visitors:
            max_visitors = visitor_list[index]
            max_name = name_list[index]
    
    return max_name

def record_service_needed(name_list, category_list, daysOpen_list):
    with open("service.csv", "w") as file:
        for index in range(len(name_list)):
            if category_list[index] == "Roller Coaster":
                days = daysOpen_list[index] % 90
                if (90 - days) <= 7:
                    writer = csv.writer(file)
                    writer.writerow([name_list[index]])
                

def changed_height_coasters(name_list, height_list):
    #define a list for rides with heights > 1m
    out_of_data_rides = []

    #firstly, sort through the attractions and identify which ones have a height of less than 1.0m
    for index in range(len(height_list)):
        if height_list[index] < 1.0:
            #add these rides to a list called out_of_date_rides = []
            out_of_data_rides.append(name_list[index])
    print(out_of_data_rides)

    current_number = 1
    for ride in out_of_data_rides:
        print(str(current_number) + ". " + ride)
        current_number += 1
    # lastly, loop through each ride in the list above, then print them with 1, 2, 3, etc








def main():
    name_list,category_list, visitor_list, daysOpen_list, height_list = get_data()
    unpopular = least_popular(name_list, visitor_list)
    popular = most_popular(name_list, visitor_list)
    content_rides_service_needed = record_service_needed(name_list, category_list, daysOpen_list)

    print("Most popular ride: " + popular)
    print("Least unpopular ride: " + unpopular)

    print(content_rides_service_needed)

    changed_height_coasters(name_list, height_list)

main()