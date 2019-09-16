""" 
    This section will show you how to do CRUD in Mongodb (NoSQL database)
    CREATE
    READ/RETREIVE
    UPDATE
    DELETE

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

"""
   For you exercise, try the following
    1. Delete by id

    2. Updating specific data

    3. List all data

"""






