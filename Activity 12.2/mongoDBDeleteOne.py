from mongoDBConnector import db, client

# Access the employees collection
collection = db.employeeCollection

filter = {"LastName": "Rose"}
collection.delete_one(filter)
results = list(collection.find()) # Can also not convert to list and iterate through cursor
for result in results: 
  print(result)

client.close()