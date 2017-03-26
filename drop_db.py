import pymongo
client = pymongo.MongoClient()

db = client.post_database

result = db.posts.delete_many({})
print('db items deleted : ', result.deleted_count)
