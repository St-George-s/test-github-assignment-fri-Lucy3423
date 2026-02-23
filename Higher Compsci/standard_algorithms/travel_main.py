#for x in range(1000000):
    #print(str(x) + " x " + str(13.5) + " = " + str(x * 13.5))


def get_destination():
    travel_destination = input("Enter your travel destination (type 'END' to stop): ")
    return travel_destination


# destination = get_destination()

def get_number_people():
    number_people = int(input("Enter how many poeple are coming: "))
    return number_people


# number_people = get_number_people()

def get_travel_method():
    travel_method = input("Enter your mode of transport: ")
    return travel_method


# travel_method = get_travel_method()

def print_all_trips(destinations, poeple_counts, travel_methods):
    for destination in range(len(destinations)):
        print(f"""
Destination: {destinations[destination]}
Number of Poeple: {poeple_counts[destination]}
Mode of Transport: {travel_methods[destination]}
""")
    

def check_if_local_destination(destination):
    is_local = False
    local_destinations = ["Edinburgh", "Glasgow", "Dundee", "Aberdeen"]

    for local_destination in local_destinations:
        if local_destination == destination:
            is_local = True
    
    if is_local == False:
        travel_method = get_travel_method()
    else:
        travel_method = "Local Transport"
    
    return travel_method


def summerise_trips(destinations, people_counts):
    num_trips = len(destinations)

    total_ppl = 0
    for count in range(len(people_counts)):
        total_ppl += count

    index = 0
    item_to_look_for = destinations[index]
    
    number_found = 0
    for destination in destinations:
        if destination in destinations[count:]:
            pass

def find_trip_by_destination(destination_to_find, destinations, people_counts, travel_methods):
    for destination in range(len(destinations)):
        if destination == destination_to_find:
            num_ppl = "Number people: " + str(people_counts[destination])
            mode = "Mode of transport: " + travel_methods[destination]
            return num_ppl, mode
                                    
    



def plan_a_trip():
    destination = get_destination()

    #define lists
    destinations = []
    people_counts = []
    travel_methods = []
    while destination != "END":
        number_people = get_number_people()

        #check if local destination
        travel_method = check_if_local_destination(destination)

        #add values to lists
        destinations.append(destination)
        people_counts.append(number_people)
        travel_methods.append(travel_method)
        print("")

        #input whether user wants to append another trip
        destination = get_destination()
        



        #print overall travel details/info
    travel_details = print_all_trips(destinations, people_counts, travel_methods)

    trip_to_look_for = input("Enter a destination to look for: ")
    print(trip_to_look_for)
    find_trip_by_destination(trip_to_look_for, destinations, people_counts, travel_methods)
    


start_trip = plan_a_trip()

# trip_info = print_travel_details(destination, number_people, travel_method)