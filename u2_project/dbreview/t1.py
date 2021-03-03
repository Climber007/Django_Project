import redis
import simplejson

db = redis.Redis('192.168.0.100')
print(db.keys('*'))
reviewlist = db.lrange('review:items', 0, -1)
count = 0
for comment in reviewlist:
    count +=1
    try:
        review = simplejson.loads(comment).get('comment')
        print(review.strip())
    except Exception as e:
        print(e)
print(count)


