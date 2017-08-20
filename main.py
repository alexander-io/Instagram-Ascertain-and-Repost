# main method
import copy
import xx
# from Instagram-API-python/InstagramAPI import InstagramAPI
import pymongo
import queue
import time
import os
import sys
from bson.objectid import ObjectId
import pprint
sys.path.append('Instagram-API-python')
from InstagramAPI.InstagramAPI import InstagramAPI
import dictionaries
import getpass

time_between_posts = 15

# declare & fill the queue with ObjectId types, corresponding to the values contained in the post_map
q = queue.Queue()
post_queue = queue.Queue()
# main routine for instagram ascertain & repost
def main():

    # choose post dictionary
    post_dictionary = dictionaries.choose_dictionary()

    # acquire all new content from dictionary, fill queue for posting
    xx.acquire_all(post_dictionary['dict'])


    # login to session throigh instagram api
    print('input username')
    IGUSER = input()
    #
    #
    print('input password')
    # # PASSWD = input()
    PASSWD = getpass.getpass()


    # call to api
    igapi = InstagramAPI(IGUSER,PASSWD)

    # start the mongo client, access the posts database
    client = pymongo.MongoClient()
    db = client.post_database
    posts = db.posts

    # print('test printing post')
    # pprint.pprint(posts.find_one())


    # q = fill_queue(q)
    with open("post_map", "r") as f:
        map_content = f.readlines()

    # print(map_content)
    for x in map_content:
        # print('x : ', x)
        # y = x.clone()
        y = copy.copy(x)
        y = y.replace("\n", "")
        q.put(ObjectId(y))
        post_queue.put(posts.find_one(ObjectId(y)))
        # print(q.get())

    i=0
    igapi.login() # login

    while not post_queue.empty():
        # print(q.get())
        # print(post_queue.get())

        entry_filter = str(q.get())

        # remove the dequeued() entry from the list
        map_content.remove(entry_filter+"\n") # XXX
        # open the post_map file, and write back the remaining entries
        with open("post_map", "w") as f: # XXX
            for x in map_content: # XXX
                f.write(x) # XXX

        p = post_queue.get()

        print('posting next, #'+str(i))

        tag_lst_builder = []
        i = 0
        while i < len(post_dictionary['tags']) :
            tag_lst_builder.append('#'+post_dictionary['tags'][i])
            i += 1

        tags = ' '.join(tag_lst_builder)

        try:
            igapi.uploadPhoto(p['image_path'], " ∴ " + "Source : @"+p['username']+" ∴ " + tags)
        except AttributeError:
            print('ig uploading error, probably a video')
            pass

        time.sleep(time_between_posts)

        i+=1

    igapi.logout()


def fill_queue():
    with open("post_map", "r") as f:
        map_content = f.readlines()

    # print(map_content)
    for x in map_content:
        # print('x : ', x)
        x = x.replace("\n", "")
        q.put(ObjectId(x))


    # pprint.pprint(posts.find_one({"_id":pidd}))

    return q
if __name__=="__main__":
    main()
