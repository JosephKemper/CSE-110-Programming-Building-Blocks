import math


side_of_square = input ("What is the length of a side of the square? ")
rectangle_length = input("What is the length of the rectangle? ")
rectangle_width = input("What is the width of the rectangle? ")
circle_radius = input("What is the radius of the circle? ")

square_area = float(side_of_square)*float(side_of_square)
rectangle_area = float(rectangle_length)*float(rectangle_width)
circle_area = math.pi * (float(circle_radius)*float(circle_radius))

print()

print("The area of the square is: " + str(square_area))
print("The area of the rectangle is: " + str(rectangle_area))
print("The area of the circle is: " + str(circle_area))

print()

multi_shape_length = float(input ("What length would you like to have turned into multiple shapes? "))

print()

print(f"A square of that length would have an area of {multi_shape_length**2}")
print(f"A a circle of that radius would have an area of {math.pi*(multi_shape_length**2)}")
print(f"A cube with sides of that length would have a volume of {multi_shape_length**3}")
print(f"A cube with sides of that length would have a volume of {4/3*math.pi*(multi_shape_length**3)}")

print()

