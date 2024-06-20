from cassandra.cluster import Cluster
# from cassandra.auth import PlainTextAuthProvider

# Connect to Cassandra cluster
cluster = Cluster(["localhost"], port=9042)
keyspace = None
# auth_provider = PlainTextAuthProvider(username='your_username', password='your_password')
session = cluster.connect(keyspace)

# Create keyspace
session.execute("CREATE KEYSPACE IF NOT EXISTS books WITH replication = {'class':'SimpleStrategy', 'replication_factor':1}")

# Set current session to the books keyspace
session.set_keyspace('books')

# Create table
session.execute("""
  CREATE TABLE IF NOT EXISTS book (
    Book_ID int PRIMARY KEY,
    Name text,
    Author text,
    Year_Published int,
    Number_of_Pages int
  )
""")

# Insert rows
session.execute("""
  INSERT INTO book (Book_ID, Name, Author, Year_Published, Number_of_Pages)
  VALUES (1, 'The Mystery of Capital', 'Hernando de Soto', 1970, 209)
""")
session.execute("""
  INSERT INTO book (Book_ID, Name, Author, Year_Published, Number_of_Pages)
  VALUES (2, 'Fairy Tales', 'Hans Christian Andersen', 1836, 784)
""")
session.execute("""
  INSERT INTO book (Book_ID, Name, Author, Year_Published, Number_of_Pages)
  VALUES (3, 'The Divine Comedy', 'Dante Alighieri', 1315, 928)
""")
session.execute("""
  INSERT INTO book (Book_ID, Name, Author, Year_Published, Number_of_Pages)
  VALUES (4, 'Romeo and Juliet', 'William Shakespeare', 1597, 100)
""")

# Close the connection
session.shutdown()
cluster.shutdown()
