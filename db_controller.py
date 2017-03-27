import pymongo
# from pymongo.objectid import ObjectId
from bson.objectid import ObjectId
import pprint




def post_to_base(post):
    client = pymongo.MongoClient()
    db = client.post_database
    posts = db.posts

    # post = {'key':'val'}
    
    post_id = posts.insert_one(post).inserted_id
    return post_id
