import json

# Json data:
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
        "name": "Taban Cosmos",
        "nationality": "South Sudanese-American",
        "sex": "Male",
        "year": "2026",
    },
    {
        "category": "Data Science",
        "name": "Kaku Cosmos",
        "nationality": "South Sudanese-American",
        "sex": "Male",
        "year": "2030",
    },
]

# Write to a new file
with open('../data/json_data.json', 'w') as json_data:
    json.dump(nobel_winners, json_data)

#  Load the data and print it out
data = open('../data/json_data.json').read()
print(data)