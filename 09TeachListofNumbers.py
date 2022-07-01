print ("Enter a list of number, type 0 when finished.")

numbers =[]
number = -1

while number != 0:
    number = int(input ("Enter a number: "))

    if number != 0:
        numbers.append (number)

sum = 0
for number in numbers:
    sum += number

count = len(numbers)
print (f"You entered {count} numbers.\n")
readingPause = input ("Press Enter to Continue\n")

print (f"The sum is: {sum}\n")
readingPause = input ("Press Enter to Continue\n")

count = len(numbers)
average = sum/count

print (f"The average is: {average}\n")
readingPause = input ("Press Enter to Continue\n")

bestSoFar = -1

for number in numbers:
    if number > bestSoFar:
        bestSoFar = number

print (f"The lagest number is: {bestSoFar}\n")
readingPause = input ("Press Enter to Continue\n")

smallestSoFar = 999999999999999999999
for number in numbers:
    if number > 0 and number < smallestSoFar:
        smallestSoFar = number

print (f"The smallest positive number is: {smallestSoFar}\n")
readingPause = input ("Press Enter to Continue\n")

sortedList = sorted (numbers)
print ("The sorted list is:")
for number in sortedList:
    print (number)
