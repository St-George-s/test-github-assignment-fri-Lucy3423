# import random
import random

battle_grid = [["-", "-", "-", "-", "-"], ["-", "-", "-", "-", "-"], ["-", "-", "-", "-", "-"], ["-", "-", "-", "-", "-"], ["-", "-", "-", "-", "-"]]

# function to clearly display the player's grid
def display_player_grid(player_grid):
    for index in range(5):
        print(player_grid[index])


def play_game(battle_grid):
    # set position of the boat

    boat_position_column = random.randint(1, len(battle_grid) -1)
    boat_position_row = random.randint(1, len(battle_grid) -1)
    battle_grid[boat_position_column][boat_position_row] = "Boat"

    # battle_grid[boat_position] = "Hit"
    win = False
    player_grid = [["-", "-", "-", "-", "-"], ["-", "-", "-", "-", "-"], ["-", "-", "-", "-", "-"], ["-", "-", "-", "-", "-"], ["-", "-", "-", "-", "-"]]
    number_guesses = 0


    while (number_guesses < 25):
        if win == False:
            # display the player grid to the screen
            display_player_grid(player_grid)

            # input the row and column to guess the position at
            guess_row = int(input("Enter a row to guess the location of a boat: "))
            guess_column = int(input("Enter a collumn to guess the location of a boat: "))

            # make the input indexes suitable for checking the location in the battle_grid
            guess_row -= 1
            guess_column -= 1

            # see if there is a boat at the guessed coords 
            if battle_grid[guess_row][guess_column] == "Boat":
                player_grid[guess_row][guess_column] = "Boat"
                print("You have hit all the boat! You win")
                display_player_grid(player_grid)
                win = True
                break
            else:
                player_grid[guess_row][guess_column] = "Miss"
                print("That's a miss!")

            number_guesses += 1
            

play_game(battle_grid)