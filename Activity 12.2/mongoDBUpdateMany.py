from mongoDBConnector import db, client

# Access the employees collection
collection = db.employeeCollection

# Create a filter and set it to {"LastName":"Smith"}
filter = {"LastName":"Smith"}

# Create newvalues containing the new values to be updated
newvalues = { "$set": { "Department": "Computer Science" } }

# Call the update_many method and pass the two parameters filter and newvalues
collection.update_many(filter, newvalues)

# Print the employees collection and verify that the new attribute, Department, has been added to employees with the last name of "Smith"
for employee in collection.find():
  print(employee)

client.close()
