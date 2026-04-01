import random, time

#ask user for upper limit
print("THE NUMBER GUESSING GAME")
print("L    O   A   D   I   N   G")
time.sleep(2)
limit = input("Type a number: ")
if limit.isdigit():
    limit = int(limit)

    if limit <= 0:
        print("Please type a number larger than 0 next time")
        quit()
else:
    print("Please type a number larger than 0 next time")
    quit()

random_number = random.randint(0, limit)
tries = 3
guess1 = input("Guess the number: ")
if int(guess1) == random_number:
    print("Good job! You have guessed correctly")
    quit()
else: 
    tries = tries - 1
    print("You have guessed incorrectly! Please try again")
    print("Tries remaining: ", tries)
    if int(guess1) > random_number:
        print("The number is below your guess")
    else:
        print("The number is above your guess")
    guess2 = input("Guess the number: ")
    if int(guess2) == random_number:
        print("Good job! You have guessed correctly in ", (3 - tries), "tries")
        quit()
    else: 
        tries = tries - 1
        print("You have guessed incorrectly! Please try again")
        print("Tries remaining: ", tries)
        if int(guess2) > random_number:
            print("The number is below your guess")
        else:
            print("The number is above your guess")
        guess3 = input("Guess the number: ")
        if int(guess3) == random_number:
            print("Good job! You have guessed correctly in ", (4 - tries), "tries")
            quit()
        else:
            print("Try again next time")
            quit() 