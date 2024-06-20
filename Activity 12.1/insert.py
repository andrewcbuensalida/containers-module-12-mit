import mysql.connector
from datetime import datetime
import uuid
from mysql_connector import cnx

# create cursor
cursor = cnx.cursor()

# insert
# id = str(uuid.uuid4())
id = 1
time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
query = (f'INSERT INTO `posts` VALUES("{id}","{time}")')
cursor.execute(query)

# clean up
cnx.commit()
cursor.close()
cnx.close()    