from datetime import datetime

# Function to import current date and time
def print_time (task_name):
    print (f"{task_name} Completed")
    print (datetime.now())
    print()

first_name = "Joseph"
print_time ("Print First Name")

for x in range (0,10):
    print (x)

print_time ("Count to Ten")