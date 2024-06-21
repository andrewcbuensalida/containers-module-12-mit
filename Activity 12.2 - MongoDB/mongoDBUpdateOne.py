from mongoDBConnector import db, client

collection = db.employeeCollection
filter = {"LastName": "Rose"}
newvalues = {"$set": {"Age": 32}}
collection.update_one(filter, newvalues)
employeeCursor = collection.find()
for employee in employeeCursor:
    print(employee)

client.close()
