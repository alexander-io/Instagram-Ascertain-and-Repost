# Alexander Harris
# Instagram Ascertain & Repost
# Spring 2017

import requests
import re
import os
import time
import sys

# dictionary of pages to acquire
post_dictionary = {
    'natanya' : 'https://www.instagram.com/product_of_the_world',
    'mononoke' : 'https://www.instagram.com/mononoke.io/',
    'world_programmers' : 'https://www.instagram.com/worldofprogrammers/',
    'world_code' : 'https://www.instagram.com/worldcode/',
    'republic' : 'https://www.instagram.com/programmerrepublic/',
    'codeness' : 'https://www.instagram.com/thecodeness/',
    'quotes' : 'https://www.instagram.com/codingquotes/',
    'buildtheweb' : 'https://www.instagram.com/buildtheweb/',
    'studiokivi' : 'https://www.instagram.com/studiokivi/',
    'coder_forevers' : 'https://www.instagram.com/coder_forevers/',
    'famsh05' : 'https://www.instagram.com/famsh05/',
    'insta_code1' : 'https://www.instagram.com/insta_code1/',
    'what_the_for_loop' : 'https://www.instagram.com/what_the_for_loop/',
    'developer_area' : 'https://www.instagram.com/developer_area/',
    'setupinspiration' : 'https://www.instagram.com/setupinspiration/'

}


# function to acquire page content and write it to disk
def acquire(page):
    # get page title
    page_title = get_page_title(page)

    # request the page
    response = requests.get(page)

    # get the description for the post, write to disk
    description = get_description(response, page_title)

    # create uniquely identifying string that's based on the description
    uid_string = make_uid_string(description)

    print('description :', description)
    print('uid string :', uid_string)

    # create a unique sub directory to contain the post
    post_path = 'posts/' + page_title + '/' + uid_string

    # translate post path to remove unwanted characters
    translated_post_path = translate_post_path(post_path)

    # create a unique sub directory to contain the post
    make_post_path(post_path, page_title, uid_string, translated_post_path)


    # XXX test print XXX
    # print(response.text)

    # go get the image for the post, write it to disk also write description.json to disk
    write_post(response, page_title, translated_post_path, description, uid_string)





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

# this function is used to creat a uniquely identifying string
# this string is to be used to identify posts, descriptions, & images for
# writing to the filesystem
def make_uid_string(description):
    s = description.split(' ')
    uid = ''
    for string in s:
        uid += string[:1]
    # print('uid string :', uid)
    return uid

def make_post_path(post_path, page_title, uid_string, translated_post_path):

    # check if the post path exists, if not make it...
    if os.path.exists(translated_post_path):
        print('path exists!')
    else:
        print('path does not exist')
        os.makedirs(translated_post_path)

# remove all unwanted characters from the path
def translate_post_path(post_path):
    translated_post_path = post_path.replace("\\", "")
    translated_post_path = translated_post_path.replace("!", "")
    translated_post_path = translated_post_path.replace("@","")
    translated_post_path = translated_post_path.replace("#","")
    translated_post_path = translated_post_path.replace("$", "")
    translated_post_path = translated_post_path.replace("%","")
    translated_post_path = translated_post_path.replace("^","")
    translated_post_path = translated_post_path.replace("&", "")
    translated_post_path = translated_post_path.replace("*","")
    translated_post_path = translated_post_path.replace("(","")
    translated_post_path = translated_post_path.replace(")", "")
    translated_post_path = translated_post_path.replace("_","")
    translated_post_path = translated_post_path.replace("+","")
    translated_post_path = translated_post_path.replace("=","")
    return translated_post_path



# get the image link from the response, download the image, write it to disk
def write_post(response, page_title, post_path, description, uid_string):
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

    post_time = str(time.time())

    f_name = page_title+'_'+post_time
    # download the image, title it uniquely based on the page and time, write file to disk
    # os.system('curl ' + post_link + ' -o images/' + page_title + '_' + str(time.time()) + '.jpg')
    os.system('curl ' + post_link + ' -o ' + post_path + '/' + f_name + '.jpg')


    # write json with description to disk
    post_file = open(post_path + "/" + f_name + ".json", "w")
    uid_string = translate_post_path(uid_string)
    post_file.write('title : ' + page_title + '\ntime : ' + post_time +'\n'+'id : ' +uid_string + '\n' + description)

    # TODO : get the hashtags associated with the post, write to disk
    # extract the hashtags from two places, from the post description and from the post comments

    post_file.close()

# acquire all recent posts from the pages contained in post_dictionary
def acquire_all(post_dictionary):
    for post in post_dictionary:
        acquire(post_dictionary[post])
        print(post)

# call to acquire all
acquire_all(post_dictionary)
