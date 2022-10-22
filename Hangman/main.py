import random
from requirment import *
blank = []
flag = 0
game_finished = False
Chosen_word = random.choice(words)
Chosen_word_len = len(Chosen_word)
lives = len(hangman) - 1

print(logo)

for i in range(Chosen_word_len):
    blank.append("_")
print(blank)

while not game_finished:
    guess_alpha = input("Guess the alphabet ").lower()
    for i in range(Chosen_word_len):
        if Chosen_word[i] == guess_alpha:
            blank[i] = guess_alpha
            flag = 1
            print(blank)
            print("Your guess was correct")
    if guess_alpha not in Chosen_word:
        print("Your guess was wrong")
        print(hangman[lives])
        if lives == 0:
            game_finished = True
            print("You lose")
            print("You are hanged")
        lives -= 1
    if "_" not in blank:
        game_finished = True
        print("You Won")
