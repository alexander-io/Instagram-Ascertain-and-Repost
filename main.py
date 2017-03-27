# main method

import x
# from Instagram-API-python/InstagramAPI import InstagramAPI
import pymongo
import queue
import time
import os
import sys
from bson.objectid import ObjectId
import pprint
# import imp

sys.path.append('Instagram-API-python')
# sys.path[0:0] = './Instagram-API-python'

# InstagramAPI = imp.load_source('InstagramAPI', 'Instagram-API-python/InstagramAPI.py')
from InstagramAPI import InstagramAPI

# configfile = 'Instagram-API-python/InstagramAPI.py'
# sys.path.append(os.path.expanduser(configfile))
# from InstagramAPI import InstagramAPI
# import InstagramAPI







def main():
    # declare & fill the queue with ObjectId types, corresponding to the values contained in the post_map
    q = queue.Queue()
    q = fill_queue(q)

    # start the mongo client, access the posts database
    client = pymongo.MongoClient()
    db = client.post_database
    posts = db.posts

    # login to session throigh instagram api
    print('input username')
    IGUSER = input()

    print('input password')
    PASSWD = input()

    igapi = InstagramAPI(IGUSER,PASSWD)
    igapi.login() # login
    i=0
    while not q.empty():
        # pprint.pprint(posts.find_one({"_id":q.get()}))
        p = posts.find_one({"_id":q.get()})

        print('posting next, #'+str(i))
        print(p['image_path'])
        igapi.uploadPhoto(p['image_path'], "source : @"+p['username']+" - '"+p['description']+"'")

        # media_id = igapi.uploadPhoto(p['image_path'], p['username']+" - "+p['description'])
        # with open("live_posts", "a") as f:
        #     f.write(media_id+"\n")


        # sleep until next post
        time.sleep(5)
        i+=1
    # log out of session
    igapi.logout()

def fill_queue(q):
    with open("post_map", "r") as f:
        map_content = f.readlines()

    # print(map_content)
    for x in map_content:
        # print('x : ', x)
        x = x.replace("\n", "")
        q.put(ObjectId(x))


    # pprint.pprint(posts.find_one({"_id":pidd}))

    return q
main()
