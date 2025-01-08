#Step 1 ---------------------------------------------------->

#from random import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

lives = len(stages)

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

import random
chosen_word = random.choice(word_list) #todo - 1
#Testing code
#print(f'the solution is {chosen_word}.')

# for letters in chosen_word:
#     if letters == guess:
#         print("Present")
#     else:
#         print("Not present")

# step 2 ------------------------------------------------>



#TODO-1: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.

#TODO-2: - Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].

#TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
#Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.

display = []
for letters in chosen_word:
    display += "_"
print(display)

#for i in range(len(chosen_word)):
# guess = input("\nGuess a letter: ")
# guess = guess.lower()
# if guess == chosen_word[i]:
#     display[i] = guess
# if 



# for i in range(len(chosen_word)):
    # if guess == chosen_word[i]:
    #     display[i] = guess
#print(display,"\n")

# Step 3 ---------------------------------------------------->

#TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.

blank = "_"
while blank in display:
    guess = input("Guess a letter: ").lower()
    for letters in chosen_word:
        if guess == letters:
            display = guess
            print(display)
        if guess not in letters:
            print(stages[lives - 1])
            lives -= 1
print(display)

if lives == 0:
    print("You lose")
else:
    print("You won")

