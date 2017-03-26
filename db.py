import pymongo
# from pymongo.objectid import ObjectId
from bson.objectid import ObjectId
import pprint
# client = pymongo.MongoClient()
client = pymongo.MongoClient()


db = client.test_database

collection = db.test_collection

post = {'key':'val'}
posts = db.posts
post_id = posts.insert_one(post).inserted_id



pidd = ObjectId('58d81b5e7d454c75f6bb9e3d')
# o = pymongo.objectid.ObjectId()
pprint.pprint(posts.find_one({"_id":pidd}))
# pprint.pprint(posts.find_one({"_id":"ObjectId("58d81b5e7d454c75f6bb9e3d")"}))
