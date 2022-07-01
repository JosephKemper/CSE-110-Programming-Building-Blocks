#06 Prepare: Checkpoint
#The Problem: Qualifying for a loan
#Initially would run into an error with generating failed results. Found that I was not properly counting for all scenarios.
#Had to add a few else statements to get them accounted for. 
#Used print statements to figure out which points of the if statements were being used and when. 

import time

print ("Thank you for choosing Kemper Loans! We look forward to helping you get your loan.")
time.sleep (3)

print ("Before we get started, let's give you a quick introduction to how our services work.")
time.sleep (3)

print ("For each question we ask, you will respond with a whole number between 1 and 10, 10 being the highest.")
time.sleep (3)

print ("For example, when we ask what is your loan size, if you responded with a 1, then it would be telling us that the loan size was the smallest available.")
time.sleep (3)

print ()
print ()
print ()

loan_size = int (input ("On the 1 to 10 score, what is the loan size? "))
time.sleep (1)
print("Loan Size entered successfully.")
print ()

credit_History = int (input ("On the 1 to 10 score, how good is your credit history? "))
time.sleep (1)
print ("Credit History entered successfully.")
print ()

income_rating = int (input ("On the 1 to 10 score, how high is your income? "))
time.sleep (1)
print("Credit History entered successfully.")
print ()

down_payment_size = int (input ("On the 1 to 10 score, how large is your down payment? "))
time.sleep (1)
print("Down Payment size entered successfully.")
print ()

print ("Processing Loan request...")
time.sleep (1)
print ()
time.sleep (1)
print ()

if loan_size >= 5:
    if credit_History >= 7 and income_rating >= 7:
        loan_status = True
        print("Processing loan status ... 1 step remaining")
    elif (credit_History >= 7 or income_rating >= 7) and down_payment_size >= 5:
        loan_status = True
        print("Processing loan status ... 2 steps remaining")
    else:
        loan_status = False
        print("Processing loan status ... 3 steps remaining")

elif loan_size < 5:
    if credit_History >= 4:
        if down_payment_size >= 7 or income_rating >= 7:
            loan_status = True
            print("Processing loan status ... 4 steps remaining")
        else:
            loan_status = False
            print("Processing loan status ... 5 steps remaining")

    elif income_rating >= 4 and down_payment_size >= 4:
        loan_status = True
        print("Processing loan status ... 6 steps remaining")
    
    else:
        loan_status = False
        print("Processing loan status ... 7 steps remaining")    
    

time.sleep (1)
print ()
print ("Loan application processing complete generating results...")
time.sleep (1)
print ()

if loan_status:
    print ("Congratulations! Your Loan has been approved!")
else:
    print ("We're sorry. We were unable to approve your loan.")