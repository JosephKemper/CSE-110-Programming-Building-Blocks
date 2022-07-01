# Make two while loops
# One that repeatedly asks for a number until it is positive. 
# And one that keeps asking for a peice of candy until you say yes. 

number = 0
candy = ""

number = int (input ("Please type a positive number: "))

while number < 0:
    print ("Sorry, that is a negative number. Please try again.")
    print ()
    number = int (input ("Please type a positive number: "))

print (f"Thank you. The number is {number}.")

print ()


while candy != "yes":
    candy = input ("May I have a piece of candy? ")

print ("Thank you!")



