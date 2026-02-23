times_spent = [5, 3, 4, 6, 5]

def find_max(list):
    max_value = list[0]

    for x in range(1, len(list)):
        if list[x] > max_value:
            max_value = list[x]
    
    print("Max number: " + str(max_value))


def find_min(list):
    min_value = list[0]
    
    for x in range(1, len(list)):
        if list[x] < min_value:
            min_value = list[x]
    
    print("Min number:" + str(min_value))

def find_value(list):
    pass

find_max(times_spent)
find_min(times_spent)