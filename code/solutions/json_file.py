import json

""" 
  Process list data into JSON
  
"""

nobel_winners = [
    {
        "category": "Math",
        "name": "Jon Kamau",
        "nationality": "Kenya",
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
        "sex": "Famale",
        "year": "2030",
    },
]

# Write to a new file
with open('../data/json_data.json', 'w') as json_data:
    json.dump(nobel_winners, json_data)

# Load the data and print it out
# data = open('../data/json_data.json').read()
# print(data)

# Load the data and print it out
with open('../data/json_data.json') as f_json:
    nobel_winners_json = json.load(f_json)
print(nobel_winners_json)