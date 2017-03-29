# get user input to choose a dictionary to ascertain content from
def choose_dictionary():
    print('choose dictionary, enter leading character :\n\tclay\tceramics\n\tcs\tcomputers')
    d = input()
    if d == 'clay':
        # ceramics dict
        post_dictionary = {
            'ceramicsaretrending' : 'https://www.instagram.com/ceramicsaretrending/',
            'floriangadsby' : 'https://www.instagram.com/floriangadsby/',
            'khwurtz' : 'https://www.instagram.com/khwurtz/',
            't_endoh' : 'https://www.instagram.com/t_endoh/',
            'studio_ramonabarfuss' : 'https://www.instagram.com/studio_ramonabarfuss/',
            'kira_ni' : 'https://www.instagram.com/kira_ni/',
            'jonosmart' : 'https://www.instagram.com/jonosmart/',
            'madebywan' : 'https://www.instagram.com/madebywan/',
            'henrystreetstudio' : 'https://www.instagram.com/henrystreetstudio/',
            'ghostwares' : 'https://www.instagram.com/ghostwares/',
            'kazunori_ohnaka' : 'https://www.instagram.com/kazunori_ohnaka/',
            'luke_eastop_ceramics' : 'https://www.instagram.com/luke.eastop.ceramics/',
            'miromadethis' : 'https://www.instagram.com/miromadethis/',
            'lunaceramics' : 'https://www.instagram.com/lunaceramics/',
            'love_ceramic' : 'https://www.instagram.com/love_ceramic/',
            'lindseywherrett' : 'https://www.instagram.com/lindseywherrett/',
            'lindseywherrett' : 'https://www.instagram.com/lindseywherrett/'
        }
    elif d == 'cs':
        # dictionary of pages to acquire
        post_dictionary = {
            # 'natanya' : 'https://www.instagram.com/product_of_the_world',
            'mononoke' : 'https://www.instagram.com/mononoke.io/',
            'world_programmers' : 'https://www.instagram.com/worldofprogrammers/',
            'world_code' : 'https://www.instagram.com/worldcode/',
            'republic' : 'https://www.instagram.com/programmerrepublic/',
            # 'codeness' : 'https://www.instagram.com/thecodeness/',
            'quotes' : 'https://www.instagram.com/codingquotes/',
            'buildtheweb' : 'https://www.instagram.com/buildtheweb/',
            'studiokivi' : 'https://www.instagram.com/studiokivi/',
            'coder_forevers' : 'https://www.instagram.com/coder_forevers/',
            'famsh05' : 'https://www.instagram.com/famsh05/',
            'what_the_for_loop' : 'https://www.instagram.com/what_the_for_loop/',
            'developer_area' : 'https://www.instagram.com/developer_area/',
            'setupinspiration' : 'https://www.instagram.com/setupinspiration/',
            'designyourworkspace' : 'https://www.instagram.com/designyourworkspace/',
            'isetups' : 'https://www.instagram.com/isetups/',
            'becreatives' : 'https://www.instagram.com/becreatives/',
            'macintosh_setups' : 'https://www.instagram.com/macintosh_setups/',
            'codinblog' : 'https://www.instagram.com/codinblog/',
            # 'thavy' : 'https://www.instagram.com/thavytillest/',
            'themaxsandelin' : 'https://www.instagram.com/themaxsandelin/',
            'codingcouple' : 'https://www.instagram.com/codingcouple/',
            'madeawkward' : 'https://www.instagram.com/madeawkward/',
            'pixelsdigital' : 'https://www.instagram.com/pixelsdigital/',
            'setuptour_' : 'https://www.instagram.com/setuptour_/'
        }
    return post_dictionary
