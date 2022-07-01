
# CORE
# Open provided hr_system.txt file and display it to the screen. 
with open ("hr_system.txt") as employee_list:
    for line in employee_list:
        # Stretch Strip off any leading and trailing whitespace from each line
        clean_line = line.strip()
        # Split lines into parts
        employee_info =clean_line.split()
        

        employee_name = employee_info [0]
        employee_id = int(employee_info [1])
        employee_title = employee_info [2]
        employee_salary = float(employee_info [3])

# Instead of salary info calculate paycheck, assume twice monthly frequency
        pay_amount = employee_salary/24
# Give a $1k bonus to anyone who is an engineer added to the paycheck
        if employee_title.lower () == "engineer":
            pay_amount += 1000

# Display all 4 provided values in this format
# name (ID: id_number), job_title - $salary

        print (f"{employee_name} ID: {employee_id}, {employee_title} - ${pay_amount:,.2f}")
        
        






