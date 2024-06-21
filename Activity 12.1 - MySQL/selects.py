from datetime import datetime
import uuid
from mysql_connector import cnx


# create cursor
cursor = cnx.cursor()

# insert
query = ("SELECT * FROM restaurants.posts")
cursor.execute(query)

for row in cursor.fetchall():
    print(row)

# clean up
cursor.close()
cnx.close()    
