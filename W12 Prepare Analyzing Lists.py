friend_list = []
age_list = []

# List of names provided in assignment
people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]

for person in people:
# Cleaning whitespace
    clean_line = person.strip ()

# Splitting data
    data_parts = clean_line.split (" ")
    friend = data_parts [0]
    age = int(data_parts [1])

    print (f"{friend} is {age} years old.")

    friend_list.append (friend)
    age_list.append (age)

print ()

youngest_friend = min(age_list)
index_youngest = age_list.index (youngest_friend)

print (f"The youngest person is {friend_list[index_youngest]} who is only {age_list[index_youngest]} years old.")