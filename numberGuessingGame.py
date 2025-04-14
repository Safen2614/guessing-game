

'''
It is a CLI-based game, so you need to use the command line to interact with the game. The game should work as follows:

When the game starts, it should display a welcome message along with the rules of the game.
The computer should randomly select a number between 1 and 100.
User should select the difficulty level (easy, medium, hard) which will determine the number of chances they get to guess the number.
The user should be able to enter their guess.
If the user’s guess is correct, the game should display a congratulatory message along with the number of attempts it took to guess the number.
If the user’s guess is incorrect, the game should display a message indicating whether the number is greater or less than the user’s guess.
The game should end when the user guesses the correct number or runs out of chances.
'''

'''
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
You have 5 chances to guess the correct number.

Please select the difficulty level:
1. Easy (10 chances)
2. Medium (5 chances)
3. Hard (3 chances)

Enter your choice: 2

Great! You have selected the Medium difficulty level.
Let's start the game!

Enter your guess: 50
Incorrect! The number is less than 50.

Enter your guess: 25
Incorrect! The number is greater than 25.

Enter your guess: 35
Incorrect! The number is less than 35.

Enter your guess: 30
Congratulations! You guessed the correct number in 4 attempts.
'''
import random

print("Welcome to the Number Guessing Game! \nI'm thinking of a number between 1 and 100. \n\n Please select the difficulty level: \n1. Easy (10 chances)\n2. Medium (5 chances)\n3. Hard (3 chances)")


while True:
    difficulty = input('Enter your choice: ')
    if difficulty == '1':
        difficulty = 'Easy'
        print('Great! You have selected the ' + difficulty + ' difficulty level.')
        chances= 10
        break
    elif difficulty == '2':
        difficulty = 'Medium'
        print('Great! You have selected the ' + difficulty + ' difficulty level.')
        chances= 5
        break
    elif difficulty == '3':
        difficulty = 'Hard'
        print('Great! You have selected the ' + difficulty + ' difficulty level.')
        chances= 3
        break

    else:
        print('dawg pls just choose one of the three')

print("Let's start the game!")
           
ranNumber=(random.randint(1, 101))
attempts=0
for x in range(0,chances):
    guess=input("Enter your guess: ")
    if ranNumber>int(guess):
        print("Incorrect! The number is greater than "+guess+".")
        attempts+=1
    elif ranNumber<int(guess):
        print("Incorrect! The number is less than "+guess+".")
        attempts+=1
    else:
        attempts+=1
        print("Congratulations! You guessed the correct number in " + str(attempts) + " attempts.")
        break




