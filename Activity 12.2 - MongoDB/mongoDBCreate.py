import pymongo

# Establish a connection to the MongoDB server
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Access a specific database. This automatically creates the database if it doesn't exist
db = client["EmployeeDB"]

# delete collection if exists
db.drop_collection("employeeCollection")
# Access a specific collection (aka table) within the database
collection = db["employeeCollection"]

employeeCollection = [
    {"FirstName": "John", "LastName": "Smith", "Age": 25},
    {"FirstName": "Peter", "LastName": "Smith", "Age": 26},
    {"FirstName": "Gabriel", "LastName": "Smith", "Age": 28},
    {"FirstName": "Penny", "LastName": "Lane", "Age": 22},
    {"FirstName": "Eleanor", "LastName": "Rigby", "Age": 23},
    {"FirstName": "Helen", "LastName": "Rose", "Age": 23},
]

# Insert documents into the collection
result = collection.insert_many(employeeCollection)


if "EmployeeDB" in client.list_database_names():
    print("Employee database created!")
# Print the inserted document IDs
print(result.inserted_ids)
# Close the connection
client.close()
