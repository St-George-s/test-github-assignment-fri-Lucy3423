import csv

class Member:
    def __init__(self, forename, surname, distance):
        self.forename = forename
        self.surname = surname
        self.distance = distance


def read_data():
    members = []
    with open("members.txt", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            members.append(
                Member(row[0], row[1], row[2])
            )
    return members


def find_furthest_distance_walked(members):
    furthest_distance = float(members[0].distance)

    for index in range(1, len(members)):
        if float(members[index].distance) > float(furthest_distance):
            furthest_distance = members[index].distance
    return furthest_distance





def display_furthest_distance_walked(furthest_distance):
    print(f"Furthest Distance Walked is {str(furthest_distance)}")

def write_club_prize_winners_to_file(members, furthest_distance):
    furthest_distance_requirement = float(furthest_distance) * 0.7

    with open("results.txt", "w") as file:
        file.write("The number of whole marathons walked by each member is: ")

        for member in members:
            if float(member.distance) > float(furthest_distance_requirement):
                file.write(member.forename + " ")
                file.write(member.surname + " ")
                number_of_marathons = round((float(member.distance) / 26.22))
                file.write(str(number_of_marathons) + ", ")



members = read_data()

furthest_distance = find_furthest_distance_walked(members)

display_furthest_distance_walked(furthest_distance)

write_club_prize_winners_to_file(members, furthest_distance)
