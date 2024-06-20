from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')

# Access the EmployeeDB database
db = client['EmployeeDB']

collection = db['employeeCollection']

# Find the first record with last name "Rigby"
record = collection.find_one({"LastName": "Rigby"})

# Print the record
print(record)

# Close the connection
client.close()