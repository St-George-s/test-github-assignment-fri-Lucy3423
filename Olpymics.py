import csv


#data loading routine
#extract medal and country info
#print total countries processed

class Country:
    def __init__(self, rank, country, code, gold, silver, bronze, total):
        self.rank = rank
        self.country = country
        self.code = code
        self.gold = gold
        self.silver = silver
        self.bronze = bronze
        self.total = total

# ranks = []
# countries = []
# codes = []
# golds = []
# silvers = []
# bronzes = []
# totals = []


def load_data():
    #create acountries list which will store all the info for each country
    countries = []

    with open("olympics2024.csv", "w") as file:
        reader = csv.reader(file) 

        for row in reader:

            #create a Country instance with all the properties from each row
            new_record = Country(
            int(row[0]),
            row[1],
            row[2],
            int(row[3]),
            int(row[4]),
            int(row[5]),
            int(row[6])
            )        

            countries.append(new_record)

            # ranks.append(int(row[0]))
            # countries.append(row[1])
            # codes.append(row[2])
            # golds.append(int(row[3]))
            # silvers.append(int(row[4]))
            # bronzes.append(int(row[5]))
            # totals.append(int(row[6]))
    return countries


    # return athletes


#total medal calculation routine
def calculate_medal_count(athletes):
    pass


#top country indentification routine
def identify_top_country(athletes):
    pass


#gold medal report routine
def report_top_gold_medals(athletes):
    pass

# Main
