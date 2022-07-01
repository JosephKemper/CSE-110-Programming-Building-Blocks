# Core Requirements
# 1. Create two lists, one for the names of the bank accounts, and one for the balances.
# Ask the user for the name of the bank account and then for it's current balance. 
# Keep looping until the user types "quit" for the name of an account. 
# For each one, add the name and the balance to the appropriate list. 
# 2. Loop through the lists using an index and display the name of the account with the balance next to it.
# 3. Compute and display the total balance in all of the accounts and the average balance.

# Stretch Challenge
# 1. Determine which bank account has the highest balance and display the name and balance of that account.
# 2. Change your display so that it shows the index of the account next to the name.
# After displaying the list, ask the user if they want to update an account. 
# If they respond with yes, ask for the index of the account, and the new balance.
# 3. Change the last step into a loop, so that the user can keep updating accounts until they say no. 
# After each update, display the new list of balances.

print ('Enter the names and balances of the bank accounts (Type: "quit" without the quotes for the account name when done)')

accounts_list = []
balance_list = []

account_name = ""


# When creating the loop to append the entered balance for some reason the append function would not attach properly to the balance_list
# After a I hit the hour of working on the program, I then looked at the code to see what the instructor did and mirrored my code to what he did
# However even after doing that, I still had problems. 
# Utimately, I deleted all of what is now line 37 and rewrote it and then it worked properly. 

while account_name.lower () != "quit":
    account_name = input ("What is the name of the account? ")
    
    if account_name.lower () != "quit":
        balance_input = float(input ("What is it's balance? "))

        accounts_list.append (account_name)
        balance_list.append  (balance_input)
        print (f"A balance of {balance_input:,.2f} added to {account_name}")

print ()

total = 0

print ("Account Information:")

for i in range (len (accounts_list)):
    print (f"{i}. {accounts_list[i]} - ${balance_list[i]:,.2f}")

    total += balance_list[i]

average = total / len (balance_list)

print()
print (f"Total: ${total:,.2f}")
print (f"Average: ${average:,.2f}")

print ()
# Learned how to make next line from https://datagy.io/python-index-of-max-item-list/
highestBalance = [index for index, item in enumerate (balance_list) if item == max(balance_list)]

if len (highestBalance) > 1:
    print ("The accounts with the highest balance are: ")
else:
    print ("The account with the highest balance is: ")

for index in highestBalance:
    print (f"{accounts_list [index]} - ${balance_list[index]:,.2f}")

change_account = "yes"
print ()

while change_account == "yes":
    change_account = input ("Do you want to update an account? ")

    if change_account.lower() == "yes":
        index = int (input ("Enter the index number of the account you want to update: "))
        new_amount = float ( input ("What is the new balance? "))
        balance_list [index] = new_amount

    print ()

    print ("Account Information:")
    for i in range (len (accounts_list)):
        print (f"{i}. {accounts_list[i]} - ${balance_list[i]:,.2f}")