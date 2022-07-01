import time
grade = float (input ("Please enter the final numerical grade for your class: "))

print()
time.sleep (1)
print()
time.sleep (1)

if grade >= 94:
    print (f"A score of {grade} is an A.")

elif grade >= 90:
    print (f"A score of {grade} is an A-.")

elif grade >= 87:
    print (f"A score of {grade} is a B+.")

elif grade >= 84:
    print (f"A score of {grade} is a B.")

elif grade >= 80:
    print (f"A score of {grade} is a B-.")

elif grade >= 77:
    print (f"A score of {grade} is a C+.")

elif grade >= 74:
    print (f"A score of {grade} is a C.")

elif grade >= 70:
    print (f"A score of {grade} is a C-.")

elif grade >= 67:
    print (f"A score of {grade} is a D+.")

elif grade >= 64:
    print (f"A score of {grade} is a D.")

elif grade >= 60:
    print (f"A score of {grade} is a D-.")

else:
    print (f"A score of {grade} is an F.")

print()
time.sleep (1)
print()
time.sleep (1)

if grade >= 70:
    print ("Congratulations! You passed the class!")

else:
    print ("We're so sorry. You did not pass the class.")

print()
time.sleep (2)
