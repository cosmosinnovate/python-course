"""
Write a book library program using list.
Your program should be able to do this action:
- Add/Append
- Search
- Delete

1. Store book title in a list
2. Accept user input
3. Add a new book title to the library
4. Make sure that you can delete from the library
5. Search a if a book exists in the library
6. Print book not found if there is no book
7. End program when when actions are done print out the lists.
8. Validate inputs as a string

"""


### TASKS

# Create a list with data on in. Look at examples of lists
list_of_books = [""]

# get user input: Look at examples of inputs
book_title = input("Enter a book\'s title")

# add book to the list: Look at example for adding element to list
list_of_books.append(book_title)

# print the print the newly created list
print(list_of_books)

# search list: Loop through the list to find the item you want to search in your book library
book_title = input("Enter a book\'s title")
for item in list_of_books:
    pass # do something here

# delete a single book title from the list then print out the remining list of book titles in the library
book_title = input("Enter a book\'s title")
list_of_books.remove(book_title)

# print the list of the books