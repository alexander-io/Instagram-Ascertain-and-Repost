import requests
import re
import os
import time

programmer_dictionary = {
    'codeness' : 'https://www.instagram.com/thecodeness/',
    'mononoke' : 'https://www.instagram.com/mononoke.io/',
    'world' : 'https://www.instagram.com/worldofprogrammers/',
    'republic' : 'https://www.instagram.com/programmerrepublic/',
    'quotes' : 'https://www.instagram.com/codingquotes/'

}

# print(page_directory['codeness'])

def scrape(page):
    page_segments = page.split('.com/')
    # print(page_segments[1])
    page_segments = page_segments[1].split('/')

    page_title = page_segments[0]
    print(page_title)

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





scrape(programmer_dictionary['mononoke'])
