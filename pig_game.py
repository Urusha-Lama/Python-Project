import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)
    return roll

while True:
    players = input("Enter the number of players (2-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Number of players must be between 2 and 4.")
    else:
        print("Invalid input. Please enter a number.")

max_score = 50
players_score = [0 for _ in range(players)]

while max(players_score) < max_score:
    for player_index in range(players):
        print(f"\nPlayer number {player_index + 1}'s turn has just started!\n")
        current_score = 0

        while True:
            should_roll = input("Would you like to roll? (y/n): ")
            if should_roll.lower() == "n":
                break
            elif should_roll.lower() == "y":
                value = roll()
                if value == 1:
                    print("You rolled a 1! Turn done!")
                    current_score = 0
                    break
                else:
                    current_score += value
                    print(f"You rolled a {value}. Your current score this turn is: {current_score}")
            else:
                print("Invalid input. Please enter 'y' or 'n'.")

        players_score[player_index] += current_score
        print(f"Your total score is now: {players_score[player_index]}")

    print("\nCurrent Scores:")
    for i in range(players):
        print(f"Player {i + 1}: {players_score[i]}")
        
winner = players_score.index(max(players_score)) + 1
print(f"\nPlayer {winner} wins with a score of {players_score[winner - 1]}!")
