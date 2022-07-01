# Lists for storing shopping cart info. 
product_names = []
product_prices = []

product_input = ""
user_choice = 0
remove_item = 0
product_quantity = 0

# Program currently errors out if you do not enter a number. Want to figure out how to stop that. 
# I tried using the while tue and try loops I tried earlier, but everything I tried with that just caused different errors. 
while user_choice != 5:
    print ("""Please select one of the following:
1. Add item
2. View cart
3. Remove item
4. Compute total
5. Quit\n""")

    user_choice = int(input ("Please enter the number of the action you wish to perform: "))
    if user_choice == 1:
        product_input = str(input ("\nWhat item would you like to add? ")).capitalize()
        price_input = float(input ("What is the price? "))
# I wanted to give the user an option to enter a quantity of items for example, add 2 dozen eggs at $1.49 each but I ran out of time. 

        product_names.append (product_input)
        product_prices.append (price_input)
        print ()
# I wanted to have the program format the numbers to include commas if the user put larger numbers in, so I had to research that. 
# I also had to search for how to format numbers with decimal points because I did not remember that offhand. 
        print (f"{product_input} has been added to your cart with a price of ${price_input:,.2f}.")
        reading_pause = input ("Press Enter to continue\n")
        

    
    elif user_choice == 2:
        for i in range(len(product_names)):
            print (f"{i+1}. {product_names[i]} - ${product_prices[i]:,.2f}")
        reading_pause = input ("Press Enter to continue\n")     
    
    elif user_choice == 3:
        print ("Your shopping cart currently consists of the following items:")
        for i in range(len(product_names)):
            print (f"{i+1}. {product_names[i]} - ${product_prices[i]:,.2f}")

        remove_item = int(input("What is the number of the item you want to remove? "))
        product_names.pop (remove_item-1)
        product_prices.pop (remove_item-1)
        actual_index = int(remove_item -1)
        # Wanted to print the item that they removed and its price, but for some reason I kept getting an error. 
        print ("Item Removed Successfully")

        print ("Your shopping cart now consists of the following:")
        for i in range(len(product_names)):
            print (f"{i+1}. {product_names[i]} - ${product_prices[i]:,.2f}")

        reading_pause = input ("Press Enter to continue\n")

    
    elif user_choice == 4:
        total_price = 0
        for i in range(len (product_prices)):
            total_price += product_prices[i]
        
        print (f"The total of all items in your shopping cart is ${total_price:,.2f}.")
        average_price = total_price / len (product_names)
        print (f"The average price of all items in your cart is ${average_price:,.2f}")

        # Learned how to make next line from https://datagy.io/python-index-of-max-item-list/
        # I wanted to turn it into a list to enable the program to handle situations where there are multiple products with the highest price. 
        highest_price = [index for index, item in enumerate (product_prices) if item == max (product_prices)]
        if len (highest_price) > 1:
            print ("The products with the highest price are: ")
        else:
            print ("The product with the highest price is: ")
        
        for i in highest_price:
            print (f"{product_names [i]} - ${product_prices[i]:,.2f}")
        
        reading_pause = input ("Press Enter to continue\n")


    elif user_choice == 5:
        break
    
    else:
        print ("\nWe're sorry that was not a valid option. \nValid options are the numbers from 1 to 5.\n")
        reading_pause = input ("Press Enter to continue\n")
