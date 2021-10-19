#Step 1 

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a
# variable called chosen_word.

#TODO-2 - Ask the user to guess a letter and assign their answer to a 
# variable called guess. Make guess lowercase
#TODO-3 - Check if the letter the user guessed (guess) is one of the letters
# in the chosen_word.

#randomly choosing the list word.
import random
chosen_word = random.choice(word_list)

#asking the user for input and assigning it
guess = input("Guess a letter: ").lower()

#check if the letter guessed is one from the list
for letter in chosen_word: 
    if letter == guess:
        print("Right")
    else:
        print("Wrong")
        