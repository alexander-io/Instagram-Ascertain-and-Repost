# main method

import x

import pymongo
import queue
import time

def main():
    q = queue.Queue()
    q = fill_queue(q)
    i = 0
    while(True):
        print('posting next, #'+str(i))
        # post_next(q)
        time.sleep(5)
        i+=1

# def post_next(q):
#     q.get()

def fill_queue(q):
    print('fill queue')
    return q
main()
