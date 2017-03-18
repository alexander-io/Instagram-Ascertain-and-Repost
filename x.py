# Alexander Harris
# Instagram Ascertain & Repost
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

    # get the description for the post, write to disk
    description = get_description(response, page_title)

    # TODO : create uniquely identifying string that's based on the description
    uid_string = make_uid_string(description)

    print('description', description)

    # TODO : create a unique sub directory to contain the post
    # if os.path.exists('posts/')

    # XXX test print XXX
    # print(response.text)

    # go get the image for the post, write it to disk
    get_image(response, page_title)



    # TODO : get the hashtags associated with the post, write to disk


# function that's used to extract page title, useful for naming files written to disk
def get_page_title(page):
    page_segments = page.split('.com/')
    page_segments = page_segments[1].split('/')
    return page_segments[0]

# function that's used to extract the caption, or post description
def get_description(response, page_title):
    description_start = re.search('caption": "', response.text)
    i = description_start.end() # iterator used to grab description
    description = ''
    while True:
        if (response.text[i] == '"'):
            break
        else:
            description += response.text[i]
        i+=1

    return description

def make_uid_string(description):
    s = description.split(' ')
    uid = ''
    for string in s:
        uid += string[:1]
    print('uid string :', uid)

# get the image link from the response, download the image, write it to disk
def get_image(response, page_title):
    # start by searching the response for the regular expression
    # that corresponds to the image we're looking for
    post_link_start = re.search('display_src": "', response.text)
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

scrape(programmer_dictionary['codeness'])
