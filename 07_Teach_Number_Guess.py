import random
import time
import subprocess

Agent_Number = random.randint(8,99)

print("Welcome to the Ultimate Number Guessing game!")
time.sleep(1)

#get user name. 
First_Name = input('Please Enter Your First Name: ')
print('Processing ...')
print(' ')
time.sleep (1)
Last_Name = input('Please Enter Your Last Name: ')
print('Processing ...')
print(' ')
time.sleep (1)

#Reply back with user name.
print(f'Thank you for playing the number guessing game {First_Name} {Last_Name}!')

#Set proper expectations for user.
print("I am going to pick a number between 1 and 1,000!")

#give deliberate pauses to create the illusion of thinking. 
time.sleep(3)

#Get first guess from user. 
guess = int(input("What is your guess? "))

#Randomly choose number. 
correct_number = random.randint(1, 1000)

#Create system for tracking guesses. 
guess_count = 1

#Increase guess count if they do not guess the correct number. 
while guess != correct_number:
  time.sleep(1)
  guess_count += 1

  #Let the user the user know they need to go higher if their guess is too low and ask for their next guess using the name they provided. 
  if guess < correct_number:
    guess = int(input(f"""Nice try, but you need to go higher. 
  What is your next guess {First_Name}? """))

      #Let the user the user know they need to go higher if their guess is too high and ask for their next guess using the name they provided.
  else:
    guess = int(input(f"""Nice try, but you need to go lower. 
  What is your next guess {First_Name}? """))

#Let the user know when they get the right number and use their name in the reply, along with telling them how many guesses they took to get the right number. 
print(f"""That's Right {First_Name}! 
The answer was {correct_number} it took you {guess_count} guesses.""") 
if guess_count <= 15:
    print('To get that good of a score you must have a lot of skill and luck on your side.')
    time.sleep (3)
    print('')
    print('That is just what we are looking for in an agent.') 
    time.sleep (3)
    print('')
    print("That's right, this was not a simple game.")
    time.sleep (3)
    print('')
    print('It is a recruiting tool that we use to find people just like you.')
    time.sleep (3)
    print('')
    print('If you choose to accept you will be given your own 00 status.') 
    Acceptence = input('Do you accept this opportunity? (1 = Yes, 2 = No): ')
    print('Processing ...')
    print(' ')
    time.sleep (3)

    if Acceptence == "1":
        print (f'Congratulations Agent {Last_Name}, {First_Name} {Last_Name}!')
        print (f'You are now 00{Agent_Number}!')
        time.sleep (3)
        print('')
        print('You will be contacted shortly with your first mission.')
        time.sleep (3)
    
    else:
        print (f'That is too bad, {First_Name} {Last_Name}.')
        print ("We'll be watching you...")
    

    time.sleep (5)
    print (' ')
    print ('This message will self destruct in: \n10')
    time.sleep (1)
    print('9')
    time.sleep (1)
    print('8')
    time.sleep (1)
    print('7')
    time.sleep (1)
    print('6')
    time.sleep (1)
    print('5')
    time.sleep (1)
    print('4')
    time.sleep (1)
    print('3')
    time.sleep (1)
    print('2')
    time.sleep (1)
    print('1')
    time.sleep (1)

    def clrscr():
        cls = subprocess.call('cls',shell=True)
    clrscr()
else:
    print(f'Can you do better next time {First_Name}?')
    time.sleep (3)
    print("We bet you can't get 15 or less!")
    time.sleep (3)
    print("Prove us wrong. We dare you!")