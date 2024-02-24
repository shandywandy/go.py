import random

# Get user's name
myName = input("Enter your name: ")

# Dictionary to store game messages
messages = {
    'welcome': f"Hi {myName}! Welcome back to the guessing game.",
    'select_number': "Please select a number.",
    'too_high': "Too high! Go lower.",
    'too_low': "Too low! Go higher.",
    'winner': "Yes!!! You are the winner"
}

# Generate a random number between 1 and 100 as the correctNumber
correctNumber = random.randint(1, 100)

# Boolean to track if the game is still running
gameRunning = True

# Main game loop
while gameRunning:
    # Display welcome message and prompt for guess
    print(messages['welcome'])
    print(messages['select_number'])

    # Get user's guess
    userGuess = int(input("Your guess: "))

    # Check if the guess is correct
    if userGuess == correctNumber:
        print(messages['winner'])
        gameRunning = False
    elif userGuess > correctNumber:
        print(messages['too_high'])
    else:
        print(messages['too_low'])
