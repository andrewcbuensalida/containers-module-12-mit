import mysql.connector
import sys
import os
from dotenv import load_dotenv

load_dotenv()

sys.dont_write_bytecode = True
# Get database credentials from environment variables
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
host = os.getenv("DB_HOST")
database = os.getenv("DB_DATABASE")
port = os.getenv("DB_PORT")

# create connection
cnx = mysql.connector.connect(
    user=user,
    password=password,
    port=port,
    host=host,
    database=database,
    auth_plugin="mysql_native_password",
)
