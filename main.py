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
    for destination in destinations:
        for number_people in poeple_counts:
            for travel_method in travel_methods:
                print(f"""Destination: {destination}
Number of Poeple: {number_people}
Mode of Transport: {travel_method}""")
    

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

        #input whether user wants to append another trip
        destination = get_destination()


        #print overall travel details/info
        travel_details = print_all_trips(destinations, people_counts, travel_methods)


start_trip = plan_a_trip()

# trip_info = print_travel_details(destination, number_people, travel_method)