import random

def roll(): # For generate random rolling dice
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)
    return roll

while True: # For the input of how many players would play this game
    players = input("Enter the number of players (2 - 4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Players must be between 2 - 4!")
    else:
        print("Invalid, try again!")

max_score = 50
players_scores = 0