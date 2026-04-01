import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type rock, paper , scissors or Q to quit: ").lower()

    if user_input == "q":
        break
    
    if user_input not in options:
        continue

    random_number = random.randint(0,2)
    # rock = 0, paper = 1, scissors = 2
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors":
        user_wins = user_wins + 1
        print("You won!")
        continue
    elif user_input == "rock" and computer_pick == "scissors":
        user_wins = user_wins + 1
        print("You won!")
    elif user_input == "rock" and computer_pick == "scissors":
        user_wins = user_wins + 1
        print("You won!")
    else:
        print("You lost!")
        computer_wins = computer_wins + 1

print("STATS")
print("Your wins: ", user_wins)
print("Computer wins: ", computer_wins)
print("Goodbye!")


