# Functions for Program Operation


# calculate and return the wind chill based on a given temperature and wind speed.
def calculate_wind_chill (temperature,wind_speed):
    return 35.74+0.6215*temperature-35.75*(wind_speed**0.16)+0.4275*temperature*(wind_speed**0.16)

# Write a function to convert from Celsius to Fahrenheit
def celsius_to_fahrenheit (temperature):
    return (temperature*(9/5))+32

# Converting back to Celsius for also displaying in original selected temperature. 
def fahrenheit_to_celsius (temperature):
    return (temperature-32)/1.8

# Not sure why, 
# something about putting a reading pause into the program causes it to display "None"
# after the function has completed. 
# The only thing I found online (from someone who had a similar issue)
# was that it is because the function is not returning anything. 
# However, it was doing this (but only when I had the reading pause enabled)
# even before I put it into a function. 
# And when I disabled the code, it would stop. 
# I tried putting it into a function as part of troubleshooting the problem.

def reading_pause ():
    input (print ("\nPress enter to continue.\n"))
    
# After creating the reading pause function I wanted to see how many things I could turn into a function.
# Printing windspeed for users
def print_wind_speed (temperature,wind_speed,windchill):
    print (f"At a temperature of {temperature}F, "+
        f"and a wind speed of {wind_speed}, "+
        f"the windchill would be {windchill:.2f}F.")

# Printing windchill in Celsius. 
def print_celsius_windchill (temperature):
    print (f"In Celsius that is a windchill of {temperature:.2f}C.")

# getting the temperature from the user
def get_temperature ():
    user_temperature = float(input("What is the temperature you wish to know the wind chill for? "))
    return user_temperature



# Main body of program.

# Allow users to enter multiple temperatures
print ("Welcome to the wind chill calculator!\n")
user_choice = 0
while user_choice != 3:
    print ("""Please select one of the following:
1. Enter a temperature in Fahrenheit
2. Enter a temperature in Celsius
3. Quit""")

# Display windchill for temperatures entered in Fahrenheit.
    user_choice = int(input("Please enter the number of the option you wish to select: "))
    if user_choice == 1:
        user_temperature = get_temperature ()
        wind_speed = 0
        while wind_speed < 60:
            wind_speed += 5
            wind_chill_factor = calculate_wind_chill(user_temperature,wind_speed)
            print_wind_speed (user_temperature,wind_speed,wind_chill_factor)
        reading_pause()

# Display windchill for temperatures entered in Celsius            
    elif user_choice == 2:
        print ("Great! We'll first convert the temperature to Fahrenheit, and then display the results.")
        user_temperature = get_temperature ()
        converted_temperature = celsius_to_fahrenheit (user_temperature)
        wind_speed = 0
        while wind_speed < 60:
            wind_speed += 5
            wind_chill_factor = calculate_wind_chill(converted_temperature,wind_speed)            
            celsius_windchill = fahrenheit_to_celsius (wind_chill_factor)
            print_wind_speed (converted_temperature,wind_speed,wind_chill_factor)
            print_celsius_windchill (celsius_windchill)            

        reading_pause()

# Exit program
    elif user_choice == 3:
        break

# Bug catcher for incorrectly entered options
    else:
        print ("We're sorry, but that is not a valid option. Please enter a number from 1 to 3.")
        reading_pause()