

friends = []
friend_input = ""

while friend_input != "end":
    friend_input = input ("Please type the name of a friend: ")
    if friend_input.lower () != "end":
        friends.append (friend_input)
    else:
        break
    if friend_input.lower () == "end":
        break

print ("Your friends are: ")
for friend in friends:
    print (friend)


if len(friends) > 10:
    print (f"WOW! You have {len(friends)} That's a lot of friends!")
