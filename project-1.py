'''
Create a simple list project that does the following. 
1. Create Empty List 
2. Populate it with data of different types: Two Lists with 5 and 2 items one in 3rd position  and another in 7th position, couple ints, and couple of strings. The general List should be 10.
3. Use the append function. 
4. Print the data out
5. Insert a new data using insert(). Then print the new results
6. Perform remove from the List using the remove()
7. Find an index of the 5th elements 
8. Pop the last item a
9. And pop atleast one more value from any location and find its length. 
'''

list = [] 

# List items
randomListOne = ["Cow", "Dog", 12, 100.00, True]
randomListTwo = ["Cow", 100.00]

list.append("Jon")
list.append("Mark")
list.append(randomListOne)
list.append("Seattle")
list.append("Bell")
list.append("Computer")
list.append(randomListTwo)

print(list)