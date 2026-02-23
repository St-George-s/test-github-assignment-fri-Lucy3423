import random

def generate_username(first_name, last_name):
    first_name3 = first_name[:3]
    last_name3 = last_name[:3]
    joined_name = first_name3 + last_name3
    random_number = random.randint(100,999)
    username = joined_name + str(random_number)
    return username

level = input("Input level (Bronze, Silver, Gold): ")
age = input("Input age: ")
username = generate_username("Lucy", "Fowler")
print(username)

name = "lucy"
name = name[0].upper() + name[1:]
print(name)
