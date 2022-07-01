#Area of a square

side_length_of_square = float(input('What is the legnth of a side of the square in centimeters? '))
print(f'The area of the square in centimeters is: {side_length_of_square**2}')
print(f'The area of the square in meters is: {(side_length_of_square/100)**2}')

#Area of  a rectangle
length_of_rectangle = float(input('What is the length of the rectangle in centimeters? '))
width_of_rectangle = float(input('What is the width of the triangle in centimeters? '))
print(f'The area of the rectangle in centimeters is: {(length_of_rectangle/100)*(width_of_rectangle/100)}')

#import library
import math

#Area of the circle
radius_of_circle = float(input('What is the radius of the cirlce in centimeters? '))
print(f'The area of the circle in centimeters is: {math.pi*((radius_of_circle/100)**2)}')

#square and circle area and volumes from one input
distance_of_length = float(input('Please enter the legnth you wish to use: '))
print(f'The area of the corresponding square would be: {distance_of_length**2}')
print(f'The area of the corresponding circle would be: {math.pi*(distance_of_length**2)}')
print(f'The volume of the corresponding cube would be: {distance_of_length**3}')
print(f'The volume of the corresponding sphere would be: {(4/3)*(math.pi)*(distance_of_length**3)}')