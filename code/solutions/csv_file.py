import csv

# This will allow you to read files from the computer.
# Make sure that your file in the same directory

# file = open("Outpatient_Imaging_Efficiency_National.csv", "r")  # Load the file
# # Run this then comment it out before you run the below function
# print(file.read())  # Use the read() function to read the loaded files in file print it
# # You can read lines from a file.
# # Uncomment this line before you can run this.
# print("\n")
# print(file.readline())
# # It is always good to close the file when done
# file.close()
# Writing JSON data to CSV.

# Json data:
nobel_winners = [
    {
        "category": "Agriculture",
        "name": "Jon",
        "nationality": "USA",
        "sex": "Male",
        "year": "1918",
    },
    {
        "category": "Physics",
        "name": "Albert Einstein",
        "nationality": "Swiss",
        "sex": "Male",
        "year": "1918",
    },
    {
        "category": "Environmental",
        "name": "Magrate",
        "nationality": "Kenya",
        "sex": "Female",
        "year": "2010",
    },
    {
        "category": "Technology",
        "name": "Cosmos",
        "nationality": "South Sudanese-American",
        "sex": "Male",
        "year": "2026",
    },
    {
        "category": "Data Science",
        "name": "Jane",
        "nationality": "South Sudanese-American",
        "sex": "Female",
        "year": "2030",
    },
]

# Create a new file or open if you have it
# ********************************************************
cols = nobel_winners[0].keys()  # Get data columns from the keys of he first object.
sorted(cols)  # Sort the keys
print(cols)

# The with key gurantees that file is closed once we the block or any erros
with open("../data/nobel_winner.csv", "w") as f:
    try:
        # Creates a concatenated string from a list of strings (cols) by joining the initial string category, name etc
        f.write(",".join(cols) + "\n")
        for o in nobel_winners:
            # Creates a list using column keys to the object in the nobel_winner
            row = [str(o[col]) for col in cols]
            f.write(",".join(row) + "\n")
    except:
        raise Exception()

# ********************************************************
# Reading data from CSV file and storing it into a list.

import json

with open("../data/nobel_winner.csv", "r") as load_data:
    reader = csv.reader(load_data)
    load_noble_winners = list(reader)  # Convert the file to a list

# You can display your data like so
for row in load_noble_winners:
    print(row[0], row[1], (row[2]), row[3], row[4])  # This will print out the data

# Give it a go with different data and try eot

