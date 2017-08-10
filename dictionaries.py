# get user input to choose a dictionary to ascertain content from
def choose_dictionary():
    print('choose dictionary, enter leading character :\n\tclay\tceramics\n\tcs\tcomputers\n\tups\tuniv. puget sound')
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
            'lunaceramics' : 'https://www.instagram.com/lunaceramics/',
            'love_ceramic' : 'https://www.instagram.com/love_ceramic/',
            'lindseywherrett' : 'https://www.instagram.com/lindseywherrett/',
            'nur_ceramics' : 'https://www.instagram.com/nur_ceramics/',
            'gerhard_ceramics' : 'https://www.instagram.com/gerhard_ceramics/',
            'kira_ni' : 'https://www.instagram.com/kira_ni/',
            'ar.ceramics' : 'https://www.instagram.com/ar.ceramics/',
            'notary_ceramics' : 'https://www.instagram.com/notary_ceramics/',
            'ceramics274' : 'https://www.instagram.com/ceramics274/',
            'ceramics.daily' : 'https://www.instagram.com/ceramics.daily/',
            'matthewchambers_' : 'https://www.instagram.com/matthewchambers_/',
            'tortus' : 'https://www.instagram.com/tortus/',
            'suepryke' : 'https://www.instagram.com/suepryke/',
        }
    elif d == 'cs':
        # dictionary of cs pages to acquire
        post_dictionary = {
            'archiecodes' : 'https://www.instagram.com/archiecodes/',
            'world_programmers' : 'https://www.instagram.com/worldofprogrammers/',
            'world_code' : 'https://www.instagram.com/worldcode/',
            'republic' : 'https://www.instagram.com/programmerrepublic/',
            'codeness' : 'https://www.instagram.com/thecodeness/',
            'quotes' : 'https://www.instagram.com/codingquotes/',
            'buildtheweb' : 'https://www.instagram.com/buildtheweb/',
            'studiokivi' : 'https://www.instagram.com/studiokivi/',
            'famsh05' : 'https://www.instagram.com/famsh05/',
            'what_the_for_loop' : 'https://www.instagram.com/what_the_for_loop/',
            'developer_area' : 'https://www.instagram.com/developer_area/',
            'setupinspiration' : 'https://www.instagram.com/setupinspiration/',
            'designyourworkspace' : 'https://www.instagram.com/designyourworkspace/',
            'isetups' : 'https://www.instagram.com/isetups/',
            'becreatives' : 'https://www.instagram.com/becreatives/',
            'macintosh_setups' : 'https://www.instagram.com/macintosh_setups/',
            'codinblog' : 'https://www.instagram.com/codinblog/',
            'themaxsandelin' : 'https://www.instagram.com/themaxsandelin/',
            'codingcouple' : 'https://www.instagram.com/codingcouple/',
            'madeawkward' : 'https://www.instagram.com/madeawkward/',
            'pixelsdigital' : 'https://www.instagram.com/pixelsdigital/',
            'setuptour_' : 'https://www.instagram.com/setuptour_/',
            'andreassterneer' : 'https://www.instagram.com/andreassterneer/',
            'codingsetups' : 'https://www.instagram.com/codingsetups/',
            'c.oding' : 'https://www.instagram.com/c.oding/'

        }
    elif d == 'ups':
        # dictionary of ups pages to acquire
        post_dictionary = {
            'theyellowhouse_ups' : 'https://www.instagram.com/theyellowhouse_ups/',
            'wetlands' : 'https://www.instagram.com/wetlands_magazine/',
            'dogsofpugetsound' : 'https://www.instagram.com/dogsofpugetsound/',
            'rmulhausen' : 'https://www.instagram.com/rmulhausen/',
            'psloggers' : 'https://www.instagram.com/psloggers/',
            'logger_swimming_fan_page' : 'https://www.instagram.com/logger_swimming_fan_page/',
            'kupsthesound' : 'https://www.instagram.com/kupsthesound/',
            'pugetsoundoutdoors' : 'https://www.instagram.com/pugetsoundoutdoors/',
            'univpugetsound' : 'https://www.instagram.com/univpugetsound/',
            'pugetsoundpiphi' : 'https://www.instagram.com/pugetsoundpiphi/',
            'pugetsound_phideltatheta' : 'https://www.instagram.com/pugetsound_phideltatheta/',
            'alphaphi_gammazeta' : 'https://www.instagram.com/alphaphi_gammazeta/',
            'pugetsoundrsa' : 'https://www.instagram.com/pugetsoundrsa/',
            'ups_diner' : 'https://www.instagram.com/ups_diner/',
            'blp' : 'https://www.instagram.com/protectthebrand/',
            'pugetsoundmusic' : 'https://www.instagram.com/pugetsoundmusic/',
            'loggerlax' : 'https://www.instagram.com/loggerlax/',
            'saepugetsound' : 'https://www.instagram.com/saepugetsound/',
            'pugetsound.cwlt' : 'https://www.instagram.com/pugetsound.cwlt/',
            'sigmachipugetsound' : 'https://www.instagram.com/sigmachipugetsound/',
            'pugetsoundadmission' : 'https://www.instagram.com/pugetsoundadmission/',
            'upslymcrew' : 'https://www.instagram.com/upslymcrew/',
            'oppcafe' : 'https://www.instagram.com/oppcafe/',
            'diversionscafe' : 'https://www.instagram.com/diversionscafe/',
            'upscellar' : 'https://www.instagram.com/upscellar/',
            'art.arthistory.pugetsound' : 'https://www.instagram.com/art.arthistory.pugetsound/',
            'lilliscafe' : 'https://www.instagram.com/lilliscafe/',
            'crosscurrents_ups' : 'https://www.instagram.com/crosscurrents_ups/'
        }
    return post_dictionary
