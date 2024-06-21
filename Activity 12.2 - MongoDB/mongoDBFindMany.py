from mongoDBConnector import db, client

# Access the employees collection
collection = db.employeeCollection

# Find all employees with the last name of Smith
employeeCursor = collection.find({"LastName": "Smith"})

# Loop through the employees and print them. Can also use list(employeeCursor) to convert to a list and iterate through the list
for employee in employeeCursor:
  print(employee)

client.close()