# controller function that's used to make a new entry in db
import pymongo
from bson.objectid import ObjectId
import pprint

# here's a function that's used to post to the database and make a new entry
def post_to_base(post):
    client = pymongo.MongoClient()
    db = client.post_database
    posts = db.posts

    post_id = posts.insert_one(post).inserted_id
    return post_id
