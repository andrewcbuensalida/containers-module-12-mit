# pip install redis
import redis

# connect to server
r = redis.Redis(host='localhost', port=6379, db=0)

# read items
# for item in r.lrange("nums", 0, -1):
#     print(item)

# read items
for key in r.keys():
  value = r.get(key) # Can't do a get if it's a list like nums
  print(value)
