from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")

# Access the EmployeeDB database
db = client["EmployeeDB"]
