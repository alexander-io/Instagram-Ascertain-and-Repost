# main method

import x
# from Instagram-API-python/InstagramAPI import InstagramAPI
import pymongo
import queue
import time
import os
import sys
# import imp

sys.path.append('Instagram-API-python')
# sys.path[0:0] = './Instagram-API-python'

# InstagramAPI = imp.load_source('InstagramAPI', 'Instagram-API-python/InstagramAPI.py')
from InstagramAPI import InstagramAPI

# configfile = 'Instagram-API-python/InstagramAPI.py'
# sys.path.append(os.path.expanduser(configfile))
# from InstagramAPI import InstagramAPI
# import InstagramAPI
# IGUSER = 'mononoke.io'
# PASSWD = 'deathrace2'






def main():
    print('input username')
    IGUSER = input()
    print('input password')
    PASSWD = input()
    igapi = InstagramAPI(IGUSER,PASSWD)
    igapi.login() # login
    igapi.uploadPhoto("coder_forevers_1490599663.367273.jpg", "ayy")
    igapi.logout()

    q = queue.Queue()
    q = fill_queue(q)
    i = 0

    while(True):
        print('posting next, #'+str(i))
        # InstagramAPI = InstagramAPI.InstagramAPI("#", "#")
        # igapi = InstagramAPI(IGUSER,PASSWD)
        # igapi.login() # login
        # igapi.uploadPhoto("coder_forevers_1490599663.367273.jpg", "ayy")
        # igapi.logout()

        # post_next(q)
        time.sleep(5)
        i+=1

# def post_next(q):
#     q.get()

def fill_queue(q):
    print('fill queue')
    return q
main()
