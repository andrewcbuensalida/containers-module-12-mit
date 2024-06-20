from mongoDBConnector import db, client

# Access the employees collection
collection = db.employeeCollection

filter = {"LastName": "Smith"}
collection.delete_many(filter)
results = list(collection.find())
for result in results:
  print(result)