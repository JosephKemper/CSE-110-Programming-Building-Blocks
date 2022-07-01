import random
import time

print("Welcome to the number guessing game!")
time.sleep(1)

#get user name. 
name = input('What is your name? ') 

#Reply back with user name.
print(f'Thank you for playing the number guessing game {name}!')

#Set proper expectations for user.
print("I am going to pick a number between 1 and 100!")

#give deliberate pauses to create the illusion of thinking. 
time.sleep(3)

#Get first guess from user. 
guess = int(input("What is your guess? "))

#Randomly choose number. 
correct_number = random.randint(1, 100)

#Create system for tracking guesses. 
guess_count = 1

#Increase guess count if they do not guess the correct number. 
while guess != correct_number:
  time.sleep(1)
  guess_count += 1

  #Let the user the user know they need to go higher if their guess is too low and ask for their next guess using the name they provided. 
  if guess < correct_number:
    guess = int(input(f"""Nice try, but you need to go higher. 
  What is your next guess {name}? """))

      #Let the user the user know they need to go higher if their guess is too high and ask for their next guess using the name they provided.
  else:
    guess = int(input(f"""Nice try, but you need to go lower. 
  What is your next guess {name}? """))

#Let the user know when they get the right number and use their name in the reply, along with telling them how many guesses they took to get the right number. 
print(f"""That's Right {name}! 
The answer was {correct_number} it took you {guess_count} guesses. 
Can you do better next time {name}?""")