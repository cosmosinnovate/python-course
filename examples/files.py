# This will allow you to read files from the computer.
# Make sure that your file in the same directory

file = open("test.txt", "r") # Load the file

# Run this then comment it out before you run the below function
print(file.read()) # Use the read() function to read the loaded files in file print it

# You can read lines from a file. 
# Uncomment this line before you can run this. 
print("\n")
print(file.readline())
