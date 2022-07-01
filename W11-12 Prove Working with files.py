# Ran into problems trying to use file with headings on it. 
# Had to remove the headings from the file to get the program to work properly.

country_list = []
code_list = []
year_list = []
life_expectancy_list = []

# Open provided life-expectancy.csv file
with open ("life-expectancy.csv") as country_data:
    for line in country_data:
        # Clean any leading and trailing whitespace
        clean_line = line.strip ()
        
        # Split line into parts
        data_parts = clean_line.split(",")


        country = data_parts [0]
        code = data_parts [1]
        year = int(data_parts [2])
        life_expectancy = data_parts [3]

# When trying to find the shortest life expetancy, I first ran into a problem where I only got a period. 
# When trying to troubleshoot the problem, 
# I ultimately realized that I had not put things into a list. I only broke it into parts.
        country_list.append (country)
        code_list.append (code)
        year_list.append (year)
        life_expectancy_list.append (life_expectancy)

# # Removing headings to allow for averages and other functions to work better. 
# country_list.pop(0)        
# code_list.pop(0)
# year_list.pop(0)
# life_expectancy_list.pop(0)



# Test to confirm heading was removed from the lists properly. 
# print (f"The first item in each list is {year_list[0]}, {code_list[0]}, {country_list[0]}, and {life_expectancy_list[0]}.")

# Used for testing quality of list import. 
# print (len(country_list))
# print (len(code_list))
# print (len(year_list))
# print (len(life_expectancy_list))

 

user_choice = 0
print ("Welcome to the Life Expectancy Tracker!\n")
while user_choice != 4:
    print("""Please select one of the following:
1. View the max and minimum life expectancy on record
2. Enter a specific year and see general data about it
3. Enter a specific country and see data about it
4. Quit
    """)
    user_choice = int(input("Please enter the number of the option you wish to select: "))
    if user_choice == 1:
        # Find the max and minimum life expectancy
        # Finding the shortest life expetancy on record
        shortest_life_expectancy = min(life_expectancy_list)
# Code to find the index of the shorest average life expectancy and assign it to a shorter variable name for readability
        lowest_index = life_expectancy_list.index (shortest_life_expectancy)
        lowest_year = year_list[lowest_index]
        lowest_code = code_list[lowest_index]
        lowest_country = country_list[lowest_index]
        lowest_expectancy = life_expectancy_list[lowest_index]

# Finding the country with the highest life expeancy on record
        longest_expectancy = max(life_expectancy_list)
        highest_index = life_expectancy_list.index (longest_expectancy)
        highest_year = year_list [highest_index]
        highest_code = code_list[highest_index]
        highest_country = country_list[highest_index]
        highest_expectancy = life_expectancy_list[highest_index]

# printing desired user data
        print (f"In the year {lowest_year}, {lowest_country} (Code {lowest_code})"+ 
        f" had the lowest average life expectancy on record at {lowest_expectancy} years.")
        print (f"In the year {highest_year}, {highest_country} (Code {highest_code})" + 
        f" had the longest average life expectancy on record at {highest_expectancy} years.")
        
        input ("Press Enter to continue\n")

    elif user_choice == 2:
# Enter a specific year and see general data about it
# Calculating Year range for display to user
        oldest_year = min(year_list)
        newest_year = max(year_list)

# Print to user year range.
        print (f"We have average data on countries from the year {oldest_year} to {newest_year}.")
        # Get year from user
        user_year = int(input ("What year did you want to know about? "))
        if user_year in year_list:
            for i in range(len(year_list)):
                # Print desired data to user
                if year_list [i] == user_year:
                    print (f"In {user_year}, {country_list[i]} (Code {code_list[i]})" +
                    f" had an average life expectancy of {life_expectancy_list[i]}.")
        else:
            # Include option for possible gaps in data. 
            print ("We're sorry we don't have data on that year. \nPlease try another year.\n")

# Give user time to breate before displaying the menu for them. 
        input ("Press Enter to continue\n")

    elif user_choice == 3:
# Enter a specific country and see data about it
        user_country = input (" Which country would you like to see specific data about? ")
        if user_country.capitalize in country_list:
            # Historical Average Life Expectancy
            #filler
            #test
            # Historical Average Live Expecancy compared with most recent data
            
            # Largest change of life Expectancy betwen years
            
            print()     

        input ("Press Enter to continue\n")
    elif user_choice == 4:
# Quit
        break

    else:
# Number not in range
        print ("\nWe're sorry that was not a valid option. \nValid options are the numbers from 1 to 4.\n")
        input ("Press Enter to continue\n")








        
