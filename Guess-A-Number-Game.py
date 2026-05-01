import random
welcome = print("Welcome to the Guess A Number Game!")

levelList = print("There are levels to choose from: Easy, Medium, Hard")
level = input("Please choose a level: ")
level = level.lower()

def easyLevel():
    number = random.randint(1,10)
    print("You have chosen the Easy level. You have 5 attempts and have to guess a number between 1 and 10.")
    guess = 0
    while guess != 5:
        userGuess = int(input(f"Please enter your guess: "))
        if userGuess > 10 or userGuess < 1:
            print("Invalid input. Please enter a number between 1 and 10.")
        elif userGuess >= 1 and userGuess <= 10:
            if userGuess == number:
                print("Congratulations! You guessed the number!")
                break
            elif userGuess != number:
                print("Sorry, that's not the correct number.")
            guess += 1
    return number

def mediumLevel():
    number = random.randint(1,50)
    print("You have chosen the Medium level. You have 5 attempts and have to guess a number between 1 and 50.")
    guess = 0
    while guess != 5:
        userGuess = int(input("Please enter your guess: "))
        if userGuess > 50 or userGuess < 1:
            print("Invalid input. Please enter a number between 1 and 50.")
        elif userGuess >= 1 and userGuess <= 50:
            if userGuess == number:
                print("Congratulations! You guessed the number!")
                break
            elif userGuess != number:
                print("Sorry, that's not the correct number.")
        guess += 1
    return number

def hardLevel():
    number = random.randint(1,100)
    print("You have chosen the Hard level. You have 5 attempts and have to guess a number between 1 and 100.")
    guess = 0
    while guess != 5:
        userGuess = int(input("Please enter your guess: "))
        if userGuess > 100 or userGuess < 1:
            print("Invalid input. Please enter a number between 1 and 100.")
        elif userGuess >= 1 and userGuess <= 100:
            if userGuess == number:
                print("Congratulations! You guessed the number!")
                break
            elif userGuess != number:
                print("Sorry, that's not the correct number.")
        guess += 1
    return number



if level == "easy":
    easyLevel()
elif level == "medium": 
    mediumLevel()
elif level == "hard":
    hardLevel()


# Error Handling for invalid level input
else:
    print("Invalid level input. Please choose from Easy, Medium, or Hard.")




