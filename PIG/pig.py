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

max_score = 15
players_scores = [0 for i in range(players)] # To store the each player's score

while max(players_scores) < max_score: 
    for player_idx in range(players):
        print(f"\nNow player {player_idx+1} turn!")
        print(f"Your total score is: {players_scores[player_idx]}\n")
        while True:
            isRoll = input("Would you like to roll (y/n)? ")
            if isRoll.lower() != "y":
                break
            value = roll()
            if value == 1:
                players_scores[player_idx] = 0
                print("You rolled a 1! Your turn is done!")
                break
            else:
                players_scores[player_idx] += value
                print(f"You rolled a: {value}")
            print(f"Your score is {players_scores[player_idx]}")
        
        print(f"Your total score is {players_scores[player_idx]}")

print("\nThe Game is Done!")
print("\nThe Final Score:")
for i in range(players):
    print(f"Player {i+1}: {players_scores[i]}")

max_player_score = max(players_scores)
winner_idx = players_scores.index(max_player_score)

print(f"\nThe winner is player {winner_idx+1} with a score of {max_player_score}!")