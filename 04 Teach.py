#Calculate how fast an object will fall
#Provided fomula 
# v(t) = sqrt(mg/c) * (1 - exp((-sqrt(mgc)/m)t))
import math 
print ("Welcome to the velocity calculator. Please enter the following:")

print ()

m = float (input ("Mass (in kg): "))
g = float (input ("Gravity (in m/s^2 9.8 for Earth, 24 for Jupiter): "))
t = float (input("Time (In Seconds): "))
p = float (input("Density of the fluid (in kg/m^3, 1.3 for air, 1000, for water): "))
big_a = float(input("Cross Sectional Area (in M^2): "))
big_c = float (input("Drag constant (0.5 for sphere, 1.1 for cylinder): "))

little_c = (1/2) * p * big_a * big_c
v = math.sqrt(m * g / little_c) * (1 - math.exp((-math.sqrt(m * g * little_c) / m) * t))

print()

print (f"The inner value of c is: {little_c:.3f}")
print (f"The Velocity after {t} seconds is: {v:.3f} m/s")