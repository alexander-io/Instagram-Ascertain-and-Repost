# Alexander Harris
# Instagram Scrape Repost
# Spring 2017

import requests
import re
import os
import time

# dictionary of pages to scrape
programmer_dictionary = {
    'codeness' : 'https://www.instagram.com/thecodeness/',
    'mononoke' : 'https://www.instagram.com/mononoke.io/',
    'world' : 'https://www.instagram.com/worldofprogrammers/',
    'republic' : 'https://www.instagram.com/programmerrepublic/',
    'quotes' : 'https://www.instagram.com/codingquotes/'

}

# function to scrape page content and write it to disk
def scrape(page):
    page_title = get_page_title(page)


    # request the page
    response = requests.get(page)
    # print(response)
    post_link_start = re.search('thumbnail_src": "', response.text)
    # print(response.text)
    # print(post_link.end())

    # post_link_len = 0
    i = post_link_start.end()
    post_link = ''
    # while char in response.text not is '"'
    while True:
        if (response.text[i] == '"'):
            break
        else:
            post_link += response.text[i]
        i+=1

    # post_link_len = i-post_link.end()
    print(post_link)

    os.system('curl ' + post_link + ' -o images/' + page_title + '_' + str(time.time()) + '.jpg')


def get_page_title(page):
    page_segments = page.split('.com/')
    page_segments = page_segments[1].split('/')
    return page_segments[0]



scrape(programmer_dictionary['mononoke'])
