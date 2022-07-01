from decimal import Rounded
from queue import PriorityQueue
import time

#Introduction to customer
print ("Welcome to the Your Choice Buffet!")
time.sleep (2)
print ("And if you're from out of state, then welcome to Utah as well.")
time.sleep (2)
print ("We are trying to prove that set prices are not needed in a restaurant.")
time.sleep (2)
print("And yes, we are an all you can eat buffet.")
time.sleep (2)
print("Accordingly, we are going to let you choose your meal prices.")
time.sleep (2)
print("You will find that our food quality and selection are similar to that of Golden Corral")
time.sleep (2)

#Input from user
child_meal_price = input ("""The normal price charged at similar restaurants for children to eat is $8.
What do you feel is a fair price for a child's meal (10 and under)? $""")
time.sleep (1)
adult_meal_price = input ("""The normal price charged at similar restaurants for adults to eat is $12.
What do you feel is a fair price for an adult's meal (11 and older)? $""")
time.sleep (1)
child_count = input ("How many children will be eating? ")
time.sleep (1)
adult_count = input ("How many adults will be eating? ")
time.sleep (1)
sales_tax = input ("The normal sales tax is 4.85 percent. What amount do you feel is a fair sales tax rate (do not enter the percent sign? ")
time.sleep (1)

#Calculations
child_meal_total = float(child_meal_price) * float(child_count)
adult_meal_total = float(adult_meal_price) * float(adult_count)
subtotal = child_meal_total + adult_meal_total
sales_tax_percent = float(sales_tax)/100
sales_tax_amount = subtotal * sales_tax_percent
total = sales_tax_amount + subtotal

#Processing time for experience
time.sleep (1)
print()
time.sleep (1)
print()
time.sleep (1)
print()

#Billing dialog begins
print("After a wonderful and filling meal you approach the host and hostess who greet you kindly.")
time.sleep (1)
print ("Thank you again for choosing the Your Choice Buffett!")
time.sleep (1)
print ("Let me calculate your bill based on your chosen meal prices.")
time.sleep (1)
print()
time.sleep ()
print()

print ("Here is your bill today.")
print ("Subtotal: $" + str( format (subtotal, '.2f')))
print ("Sales Tax: $" + str( format (sales_tax_amount, '.2f')))
print ("Total: $" + str( format (total, '.2f')))

time.sleep(1)
print ()
time.sleep(1)
print ()

five_percent_tip = subtotal * 0.05
ten_percent_tip = subtotal * 0.10
fifteen_percent_tip = subtotal * 0.15

#Option to tip given
is_customer_tipping = input ("Do you want to tip our staff today? (1 = Yes 2 = No) ")
if is_customer_tipping == "1":
    print ("""Thank you for being willing to tip our staff. 
    To help you out here are some common tip calculations for you.""")
    print ("A 5 percent tip would be $" + str( format ( five_percent_tip, '.2f')))
    print ("A 10 percent tip would be $" + str( format ( ten_percent_tip, '.2f')))
    print ("A 15 percent tip would be $" + str( format ( fifteen_percent_tip, '.2f')))
    tip_amount = input ("How much would you like to tip? $")

    total_with_tip = float(total) + float(tip_amount)

    print ()

    print ("Your total with tip is: $" + str( format (total_with_tip, '.2f')))

    print ()

    customer_payment = input ("What is the payment amount? $")

    print ()
    
    customer_change = float(customer_payment) - float(total_with_tip)
    
    print ("Change: $" + str(format(customer_change, '.2f')))

else:
    customer_payment = input ("What is the payment amount? $")
    customer_change = float (customer_payment) - float(total)
        
    print ("Change: $" + str (format (customer_change, '.2f')))

print ()
time.sleep (1)
print ()
time.sleep (1)
print ()
time.sleep (1)

#Humor thrown in at the end if the customer did not choose high enough price for their meals. 
meal_price_actual_total = float(child_meal_price) + float(adult_meal_price)

if meal_price_actual_total <= 18:
    print ("""As you walk out you hear one employee say to the other,
    "OUCH!!! I hope that doesn't happen too much, or we will go out of business." """)
else:
    print ("""As you walk out you hear one employee say to the other,
    "See! I told you we could let customers set their own prices!
    Just wait until the word gets out" """)
