from cassandra.cluster import Cluster

# Connect to the Cassandra database
cluster = Cluster(['localhost'], port=9042)
session = cluster.connect()

# Select the "books" keyspace
session.set_keyspace('books')

# Run a query to select all books
query = "SELECT * FROM book"
result = session.execute(query)

# Print each book
for row in result:
  print(row)

# Close the connection
session.shutdown()
cluster.shutdown()