# main method

import x
import post_queue
import pymongo
import queue

def main():
    q = queue.Queue()
    item = 'meh'
    q.put(item)
    print(q.get())
    print(q.qsize())
main()
