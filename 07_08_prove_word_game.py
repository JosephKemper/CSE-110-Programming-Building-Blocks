# Word list taken from https://www.bestwordlist.com/5letterwords.htm 
# I simply converted the list to a usable format. 
# After spending several hours trying to figure out how to build this and failing to get anywhere, 
# I turned to the internet for tutorials
# Used this video https://www.youtube.com/watch?v=J6h7D2iQmBU to get core of how to compare strings. 
# When I first tried implimenting his code, my program would not run. 
# I quickly found out that the script would not initiate as he built it
# but that was quickly fixed by simply calling the function. 
# From there, I wanted to have a dynamic hint that would have the actual letters of the word the user guessed
# My initial try created errors and would not even load the program. 
# Eventually, I got the hints to display dynamically and accurately, but it would not recognize when the user got the right word. 
# To fix that, I had to take it from comparing the hint to the answer, to comparing the user guess to the answer. 
# After I did that, for some reason the dynamically generated hint stopped working. 
# Utlimately, what I had to do was to rebuild the function from scratch to get it working again. 
# From there, I implimented a play again feature 
# I had to force the user to enter only a 5 letter word to prevent the game from crashing if they entered a word of the wrong length. 

import random




def main_loop():
    word_list = []
    word_file = open ("07_08_prove_word_list.txt")

    for word in word_file:
        word_list.append (word.strip())

    answer = random.choice (word_list)
# Remove # on next line to see answer for testing purposes. 
    print (answer)
    
    number_of_guesses = 0
    correct_guess = False
    while number_of_guesses < 6 and not correct_guess:
        guess = input ("\33[1;37;40m \nPlease guess a five letter word: ")
        while len (guess) != 5:
            print ("\nThe word is 5 letters long. Please guess a 5 letter word")
            guess = input ("\33[1;37;40m \nWhat is your guess: ")

        for count in range(len(guess.lower())):
            if guess[count].lower() == answer[count]:
                print (f"\33[1;32;40m {guess[count].upper()}", end= " ")
            elif guess[count] in answer:
                print (f"\33[1;33;40m {guess[count].upper()}", end= " ")
            else:
                print (f"\33[1;31;40m {guess[count].upper()}", end= " ")

        number_of_guesses += 1
    
        correct_guess = answer == guess.lower()

    if correct_guess:
        print (f"\33[1;37;40m \nIt took you {number_of_guesses} tries to get the word right")
    else:
        print (f"\33[1;37;40m \nSorry, you used up all of your tries. The correct word was {answer}.")


print ("\33[1;37;40m \nWelcome to Joseph D. Kemper's Wordle clone! Here are a few things to get you started.")
print ("""When a letter in the hint is printed in\33[1;32;40m green like this\33[1;37;40m
it means that the letter is in the word and in the right place.\n""")
reading_time_pause = input ("Press enter to continue.\n")
print ("""When a letter prints in\33[1;33;40m yellow like this\33[1;37;40m
it means that the letter is in the word but not in the right place.\n""")
reading_time_pause = input ("Press enter to continue.\n")
print ("""And when a letter appears in\33[1;31;40m red like this\33[1;37;40m
then it is not in the word at all.\n""")

reading_time_pause = input ("Press Enter to begin the game.\n")

main_loop ()

play_again = input ("\nDo you want to play again? ")

while play_again.lower () == "y" or play_again.lower () == "yes":
    main_loop ()

    play_again = input ("\nDo you want to play again? ")

print ("Thank you for playing! Have a wonderful day!")
