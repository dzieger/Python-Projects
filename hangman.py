'''
	This is the Hangman game.
	Day 6 of the course "100 Days of Python"
	David Zieger
	July 17, 2023
'''

import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = word_list[random.randint(0, len(word_list) -1)]
print(chosen_word)
#for i in range(len(chosen_word)):
#	print(chosen_word[i])

guess = input("Guess a letter: ")


for i in range(len(chosen_word)):
	if guess == chosen_word[i]:
		print("Right")
	else:
		print("Wrong")