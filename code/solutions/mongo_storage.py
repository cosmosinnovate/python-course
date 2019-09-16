""" 
    This section will show you how to do CRUD in Mongodb (NoSQL database)
    CREATE
    READ/RETREIVE
    UPDATE
    DELETE

    First you need to make sure that you install mondo database on your machin (https://docs.mongodb.com/manual/installation/)
    Install pymongo to connect to mongo database which runs on localhost:27017

"""

from pymongo import MongoClient

# Create mongo client to connect to.
mongo_client = MongoClient("localhost", 27017)

# The database to access
database = mongo_client["learning"]

#  Your databse colleciton name
collection = database["data"]

# Create data to post
record = {
    "title": "Go data to MongoDB",
    "desc": "MongoDB is no SQL database",
    "tags": ["Go", "NoSQL", "Database"],
}

#  Capture return object and print out the inserted_id
object_returned = collection.insert_one(record)
print(object_returned.inserted_id)

# Find one function returns the first one item in the database
print(collection.find_one())


"""
   For you exercise, try the following

    0. Try the insert many function

    1. Delete by id

    2. Updating specific data

    3. Find one data

    4. Find by id
    
    5. Find all data

    6. Search the collections

    Complete code will be posted.

"""

