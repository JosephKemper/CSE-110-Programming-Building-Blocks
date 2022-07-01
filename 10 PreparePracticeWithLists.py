
shopping_list = []
add_item = ""

change_item = ""

print ("Please enter the items of the shopping list (type: QUIT to finish):")
while add_item.lower () != "quit":
    add_item = input ("Item: ")
    if add_item.lower() != "quit":
        shopping_list.append (add_item)

print  ()

print ("The shopping list with indexes is:")
for i in range (len (shopping_list)):
    item = shopping_list[i]
    print (f"{i}. {item}")

print ()

index = int(input ("Enter the index number of the item you would like to change: "))
change_item = input ("What is the new item: ")

shopping_list [index] = change_item
print ("\nThe shopping list with indexes is:")
for i in range (len (shopping_list)):
    item = shopping_list [i]
    print (f"{i}. {item}")
    