"""
Guessing Number Game
"""
import random
#generate random number between 0-50
number = random.randrange(0, 51, 1)
#ask user to guess number
guess = input('Please guess a intiger between 0 - 50: ')
#convert int to string
intGuess = int(guess)
#Feedback to high, to low, you got it!
if intGuess == number:
	print('You got it!')
elif intGuess > number:
	print('You guessed to high!')
elif intGuess < number:
	print('You guessed to low!')