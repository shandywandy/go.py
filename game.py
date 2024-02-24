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
gamerunning = True
correctnumber = random.randint(0, 1000)


    # Display welcome message and prompt for guess
print(messages['welcome'])
print(messages['select_number'])

userGuess = int(input("Your guess: "))
# Get user's guess and convert to integer
userGuess = int(input("Your guess: "))

        # Check if the guess is correct
if userGuess == correctNumber:
    print(messages['winner'])
    gameRunning = False
elif userGuess > correctNumber:
    print(messages['too_high'])
else:
print(messages['too_low'])
print(messages['wrong'])
