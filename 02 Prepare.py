import time
import random
import subprocess

Agent_Number = random.randint(8,99)

First_Name = input('Please Enter Your First Name: ')
print('Processing ...')
print(' ')
time.sleep (1)
Last_Name = input('Please Enter Your Last Name: ')
print('Processing ...')
print(' ')
time.sleep (3)

Acceptence = input("""You have been selected to become an Agent 
If you choose to accept you will be given your own 00 status. 
Do you accept this opportunity? (1 = Yes, 2 = No): """)
print('Processing ...')
print(' ')
time.sleep (3)

if Acceptence == "1":
    print (f'Congratulations Agent {Last_Name}, {First_Name} {Last_Name}!')
    print (f'You are now 00{Agent_Number}!')
    
else:
    print (f'That is too bad {Last_Name}, {First_Name} {Last_Name}.')
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
