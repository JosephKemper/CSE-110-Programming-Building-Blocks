
# Open books.txt
with open ("books.txt") as book_list:
    for line in book_list:
# Strip off extra characters from each line
        book =line.strip()
# Print lines to screen
        print (book)





