#Write a program that asks the user for their favorite letter. 
# Then, loop through all the words in the provided list, 
# and for each word, loop through all of it's letters. 
# If the letter is the user's favorite, print it out as a capital letter, 
# if not, print it out as a lower case letter.

from cProfile import run


quote = """In coming days, it will not be possible to survive spiritually without the guiding, directing, comforting, and constant influence of the Holy Ghost."""

run_again = "yes"

while run_again == "yes":
    user_number = int (input ("Please enter a number: "))
    for i, letter in enumerate (quote):
        if i % user_number == 0:
            print (letter.upper (), end = "")
        else:
            print (letter.lower (), end = "")
    print ()
    run_again = input ("Would you like to enter another number? ")

print ("Goodbye")