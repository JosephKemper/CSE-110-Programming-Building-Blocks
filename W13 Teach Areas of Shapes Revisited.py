import math


def computer_area_rectangle (length,width):
   return length*width

def compute_area_square (side):
    return side*side

def compute_area_circle (radius):
    return math.pi * (radius * radius)

user_choice = 0
while user_choice != 4:
    print ("""Please select one of the following options:
1. Calculate the area of a rectangle.
2. Calculate the area of a square.
3. Calculate the area of a circle.
4. Quite the program.""")

    print()

    user_choice = int(input("Please enter the number of the option you desire: "))
    if user_choice == 1:
        length = float(input("What is the length? "))
        width = float(input("What is the width? "))
        area = computer_area_rectangle (length,width)
        print (f"The area of the rectangle is {area}.\n")
        input (print("Press enter to continue.\n"))
    
    elif user_choice == 2:
        side = float(input("What is the length of a side of the square? ")) 
        area = compute_area_square(side)
        print (f"The area of the square is {area}.\n")
        input (print("Press enter to continue.\n"))
    
    elif user_choice == 3:
        radius = float(input("What is the radius of the circle? "))
        area = compute_area_circle (radius)
        print (f"The area of the circle is {area}. \n")
        input (print("Press enter to continue.\n"))
    
    elif user_choice == 4:
        break
    else:
        input (print ("""We're sorry, that was not a valid response. 
Please choose a number between 1 and 4. 
Press enter to continue.\n"""))
        
