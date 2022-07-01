from operator import index


book_list = []
chapter_count_list = []
volume_list = []

# Open books.txt
with open ("books_and_chapters.txt") as books_file:
    for line in books_file:
# Strip off extra characters from each line
        cleaned_line =line.strip()
# Split each line into its different parts
        split_line = cleaned_line.split(":")

        book = split_line [0]
        chapter = int(split_line [1])
        volume = split_line [2]

# Append each line segment to its appropriate list
        book_list.append (book)
        chapter_count_list.append (chapter)
        volume_list.append (volume)

# Test import
#        print (f"{book} which is in the {volume}, has {chapter} chapters/sections in it.")
# Commented out after successful test

# Get list of unique entries in volume_list for implimenting stretch challenge
# Learned this from reading the Python Documentation on https://docs.python.org/3.10/tutorial/datastructures.html
unique_volumes = set(volume_list)
# Test to confirm the filter worked
# print (unique_volumes)
# Commented out after successful test

# Identify most chapters in specific book
most_chapters = max(chapter_count_list)
index_most_chapters = chapter_count_list.index (most_chapters)

# Print most chapters
# In my study of the PEP 8 style guide that best practice is to keep lines shorter than 80 characacters
# https://peps.python.org/pep-0008/
# Still working on it, but I am getting better. 
# Learned from Python documentation that we can split longer strings into multiple lines,
# using the + operator and putting the second half in its own quotes
# And because of how Python handles the merging of strings, 
# even though in the code the string is on multiple lines, 
# it will print on the same line.
# Source https://docs.python.org/3.10/tutorial/inputoutput.html
print (f"The book of scripture with the most chapters in it is {book_list[index_most_chapters]}, " +
        f"it has {chapter_count_list [index_most_chapters]} chapters in it. "+
         f"{book_list[index_most_chapters]} is located in the {volume_list [index_most_chapters]}.")


