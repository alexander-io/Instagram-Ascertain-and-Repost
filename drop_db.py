# this is a quick script to drop the collection's entries
# from the database, this script is executed on issuance of $ make clean

import pymongo
client = pymongo.MongoClient()

db = client.post_database

result = db.posts.delete_many({})
print('db items deleted : ', result.deleted_count)
