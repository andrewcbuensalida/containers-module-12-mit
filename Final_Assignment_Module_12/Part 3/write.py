# pip install redis
import redis
from datetime import datetime

# connect to server. db=0 initializes the database 0. In Redis, by default, there are 16 available databases numbered from 0 to 15.
r = redis.Redis(host="localhost", port=6379, db=0)

# delete redis database
r.flushdb()

# write to server
# t = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
# r.rpush('nums',t)

r.mset({"Milk": "Lactose", "Bread": "Gluten"})
