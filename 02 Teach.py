#Building app themed off of prior projects
#I intend to turn most or all of the apps into one big app. 
#Prior app I turned into an Agent recruitment app. 
print ("""Welcome to your first day Agent! We need to collect 10 bits of data for your record. 
Please Enter the Following""")

print()

First_Name = input ("First Name: ")
Last_Name = input ("Last Name: ")
Job_Title = input ("Job Title: ")
ID_Number = input ("ID Number: ")
Email_Address = input ("Email Address: ")
Phone = input ("Phone: ")
Hair = input ("Hair Color: ")
Month = input ("Start Month: ")
Eyes = input ("Eye Color: ")
Traning = input ("Training Complete [Y/N]: ")

print ()
print ()
print ("The ID Card is:")
print ("----------------------------------------")
print (f"{Last_Name.upper()}, {First_Name.capitalize()}")
print (Job_Title.title())
print (f"ID: {ID_Number}")

print ()

print (Email_Address.lower())
print (Phone)

print ()

print (f"Hair: {Hair.capitalize()}".ljust(20) + f"Eyes: {Eyes.capitalize()}")
print (f"Month: {Month.capitalize()}".ljust(20) + f"Training: {Traning.capitalize()}")
print ("----------------------------------------")


