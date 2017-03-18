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
    # get page title
    page_title = get_page_title(page)

    # request the page
    response = requests.get(page)

    # TODO : create a unique sub directory to contain the post

    # go get the image for the post, write it to disk
    get_image(response, page_title)

    # TODO : get the description for the post, write to disk

    # TODO : get the hashtags associated with the post, write to disk


# function that's used to extract page title, useful for naming files written to disk
def get_page_title(page):
    page_segments = page.split('.com/')
    page_segments = page_segments[1].split('/')
    return page_segments[0]

# get the image link from the response, download the image, write it to disk
def get_image(response, page_title):
    # start by searching the response for the regular expression
    # that corresponds to the image we're looking for
    post_link_start = re.search('thumbnail_src": "', response.text)
    i = post_link_start.end() # iterator used to build image link
    post_link = '' # string builder for the image link
    # loop a bit through the reponse, meanwhile build up the image link
    while True:
        if (response.text[i] == '"'):
            break
        else:
            post_link += response.text[i]
        i+=1

    # download the image, title it uniquely based on the page and time, write file to disk
    os.system('curl ' + post_link + ' -o images/' + page_title + '_' + str(time.time()) + '.jpg')

scrape(programmer_dictionary['mononoke'])
