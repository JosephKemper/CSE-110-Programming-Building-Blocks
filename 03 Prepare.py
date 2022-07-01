user_age = input ("How old are you? ")
number_of_egg_cartons = input ("How many full egg cartons do you have? ")
number_of_cookies = input ("How many cookies do you have? ")
number_of_people = input ("How many people want a cookie? ")

add_one_to_user_age = int(user_age)+1
eggs_to_cartons = int(number_of_egg_cartons)*12
cookies_per_person = (int(number_of_cookies)/int(number_of_people))
whole_cookies_per_person = int(cookies_per_person)
remaining_cookies = int(number_of_cookies)-(whole_cookies_per_person*int(number_of_people))

print()

print ("On your next birthday you will be " + str(add_one_to_user_age))
print ("You have " + str(eggs_to_cartons) + " eggs.")
print ("Each person can have " + str(cookies_per_person) + " cookie/s.")
print ("Or each person can have " + str(whole_cookies_per_person) + " cookie/s. With " + str(remaining_cookies) + " extra cookie/s.")