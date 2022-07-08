# calculate and return the wind chill based on a given temperature and wind speed.
def calculate_wind_chill (temperature,wind_speed):
    wind_chill_factor =35.74+0.6215*temperature-35.75(wind_speed**0.16)+0.4275*temperature*(wind_speed**0.16)
    return wind_chill_factor

# Write a function to convert from Celsius to Fahrenheit
def celsius_to_farenheit (temperature):
    return (temperature*(9/5))+32

print ("Welcome to the wind chill calculator!\n")
user_choice = 0
while user_choice != 3:
    print ("""Please select one of the following:
1. Enter a temperature in Farenheit
2. Enter a temperature in Celsius
3. Quit""")

    user_choice = int(input("Please enter the number of the option you wish to select: "))
    if user_choice == 1:
        user_temperature = float(input("What is the temperature you wish to know the wind chill for? "))
        wind_speed = 0
        while wind_speed < 60:
            wind_speed += 5
            wind_chill_factor = calculate_wind_chill(user_temperature,wind_speed)
            print (f"At a temperature of {user_temperature}f, "+
            f"and a wind speed of {wind_speed}, "+
            f"the windchill would be {wind_chill_factor:.2f}F.")
            
# Error in line 3. 
# float object not callable. 
# will figure out when I resume tomorrow. 