#06 Teach: Team Activity
#Amusement Park Rides

#Thoughts
#I want to figure out how to force the use to enter a numeric age. 
#I imagine that it could be accomplished with a while statement. 
#I am just not sure how to tell if they entered a number or not. 
#One possibility is that I could simply check if the value they entered is greater than 0. 


#Confirm rider quantity.
while True:
    try:
        rider_count = input ("How many riders will there be today? ")
        if rider_count.lower () == "one" or rider_count.lower () == "1":
            print ("1 Rider Confirmed.")
            rider_count = 1
            break
        elif rider_count.lower () == "two" or rider_count.lower () == "2":
            print ("2 Riders confirmed")
            rider_count = 2
            break
        else:
            print ("We're sorry, this ride allows for up to 2 riders at a time. \nPlease choose either 1 or 2 riders.")
    except:
        continue

#Approval check for single rider begins. 

#Single rider info collection begins
#Collect age and height for rider
if rider_count == 1:
    single_rider_age = int (input ("What is the rider's age? "))
    print (f"Age confirmed as {single_rider_age}.\n")
    single_rider_height = int (input ("What is the rider's height in inches? "))
    print (f"Height confirmed as {single_rider_height}.\n")
   
#Check for minimum height with hard stop if not met.  
    if single_rider_height < 36:
        print ("We're sorry, but you need to be taller than 36 inches to ride this ride.")
        exit ()

#if minimum height met, check for Golden Ticket    
    elif single_rider_height >= 36:
        while True:
            try:
                golden_ticket = str (input ("Do you have a Golden Ticket? "))
                if golden_ticket.lower () == "yes" or golden_ticket.lower () == "y":
                    golden_ticket = True
                    print ("Golden Ticket Confirmed.\n")
                    break
                elif golden_ticket.lower () == "no" or golden_ticket.lower ()== "n":
                    golden_ticket = False
                    print ("Patron does not possess a Golden Ticket.\n")
                    break
                else:
                    print ("Please answer YES or NO.\n")
            except:
                continue

#If Golden ticket, check to see if they are between 12 and 17 (inclusive) and adjust age to 18. 
        if golden_ticket:
            if single_rider_age >= 12:
                single_rider_age = 18
                print ("Patron will be given the Golden Ticket benefits\n")
            else:
                print ("Patron is too young to receive the Golden Ticket benefits.\n")
#Single rider info collection ends

#Approval check for single rider
        if single_rider_age >= 18 and single_rider_height >= 62:
            print ("Congratulations! You meet the requirements to ride alone. \nWe hope you enjoy your ride!")
        else:
            print ("We're sorry, you must be 18 or older and at least 62 inches tall to ride this ride alone.")
#Approval check for single rider ends.


#Two Rider Approval process begins

#Two rider info collection process begins
#Collect first rider age and height
elif rider_count == 2:
    first_rider_age = int (input ("What is the first rider's age? "))
    print (f"First Rider age confirmed as {first_rider_age}.\n")
    first_rider_height = int (input("What is the first rider's height in inches? "))
    print (f"First rider height confirmed as {first_rider_height}.\n")
    
    print()
    
    second_rider_age = int (input("What is the age of the second rider? "))
    print (f"Second Rider age confirmed as {second_rider_age}.\n")
    second_rider_height = int (input("What is the height of the second rider in inches? "))
    print (f"Second rider height confirmed as {second_rider_height}.\n")
    
    print ()
#Check for minimum height requirements with hard stop. 
    if first_rider_height < 36 or second_rider_height <36:
        print ("We're sorry, everyone needs to be 36 inches tall to ride this ride.\n")
        exit ()
    else:
        print ("Confirmed: No one is under minimum height requirements.\n")

#Check for golden ticket on first rider if they meet the minimum height requirements.    
    if first_rider_height >= 36 and second_rider_height >= 36:
        while True:
            try:
                first_rider_golden_ticket = str(input ("Does the first rider have a golden ticket? "))
                if first_rider_golden_ticket.lower () == "yes" or first_rider_golden_ticket.lower ()== "y":
                    first_rider_golden_ticket = True
                    print ("Confirmed: First Rider has a Golden Ticket.\n")
                    break
                elif first_rider_golden_ticket.lower () == "no" or first_rider_golden_ticket.lower () == "n":
                    first_rider_golden_ticket = False
                    print ("Confirmed: First rider does not possess a Golden Ticket\n")
                    break
                else:
                    print ("Please answer YES or NO.\n")
            except:
                continue
        
        if first_rider_golden_ticket:
            if first_rider_age >= 12:
                first_rider_age = 18
                print ("The first rider will be given the Golden Ticket benefits.\n")
            else:
                print ("The first rider is too young to receive the Golden Ticket Benefits.\n")
        
        while True:
            try:
                second_rider_golden_ticket = (input ("Does the second rider have a golden ticket? "))
                if second_rider_golden_ticket.lower () == "yes" or second_rider_golden_ticket.lower ()== "y":
                    second_rider_golden_ticket = True
                    print ("Confirmed: Second Rider has a Golden Ticket.\n")
                    break
                elif second_rider_golden_ticket.lower () == "no" or second_rider_golden_ticket.lower () == "n":
                    second_rider_golden_ticket = False
                    print ("Confirmed: Second rider does not possess a Golden Ticket.\n")
                    break
                else:
                    print ("Please answer YES or NO.\n")
            except:
                continue
#With Golden Ticket, check if first player between 12 and 17 (inclusive) and set age to 18. 
        
        
        if second_rider_golden_ticket:
            if second_rider_age >= 12:
                second_rider_age = 18
                print ("The second rider will be given the Golden Ticket benefits.\n")
            else:
                print ("The second rider too young to receive the Golden Ticket benefits.\n")

#Age and height check for 2 riders
    if first_rider_age >= 18 or second_rider_age >= 18:
        print ("Enjoy your ride!")
    
    elif (first_rider_age >= 16 and second_rider_age >= 14) or (first_rider_age >= 14 and second_rider_age >= 16):
        print ("We hope you enjoy your ride!")
    
    elif (first_rider_age >= 12 and first_rider_height >= 52) and (second_rider_age >= 12 and second_rider_height >= 52):
        print ("We hope both of you enjoy your ride!")
        
    else:
        print ("We're sorry but the two of you are too young to ride this ride. \nYou will need to get an adult to accompany you.")
    







