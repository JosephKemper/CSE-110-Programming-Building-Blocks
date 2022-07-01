#Write a program that asks the user for their favorite letter. 
# Then, loop through all the words in the provided list, 
# and for each word, loop through all of it's letters. 
# If the letter is the user's favorite, print it out as a capital letter, 
# if not, print it out as a lower case letter.

main_word = "Commitment"

favorite_letter = input ("What is your favorite letter? ")

for letter in main_word:
    if letter.lower () == favorite_letter.lower ():
        print (letter.upper (), end = "")
    else:
        print (letter.lower (), end = "")
    