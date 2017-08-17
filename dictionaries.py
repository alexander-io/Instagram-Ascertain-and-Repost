# get user input to choose a dictionary to ascertain content from
def choose_dictionary():
    print('choose dictionary, enter leading character :\n\nclay\tceramics\ncs\tcomputers\nups\tuniv. puget sound\ncrypt\tcrypto-currency\nrb\trussian blue cats\npug\tpug\n\n... ')
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
    elif d == 'crypt':
        # dictionary of cs pages to acquire
        post_dictionary = {
            'ethereum_updates' : 'https://www.instagram.com/ethereum_updates/',
            'ethereumproject' : 'https://www.instagram.com/ethereumproject/',
            'officialbitcoin' : 'https://www.instagram.com/officialbitcoin/',
            'hackersclub' : 'https://www.instagram.com/hackersclub/'
        }
    elif d == 'rb' or d == 'russian' or d == 'russianblue':
        # dictionary of cs pages to acquire
        post_dictionary = {
            'claudiuscolmus' : 'https://www.instagram.com/claudiuscolmus',
            'russianblueofficial' : 'https://www.instagram.com/russianblueofficial/',
            'sereshka_russian_blues' : 'https://www.instagram.com/sereshka_russian_blues/',
            'teruchan0823' : 'https://www.instagram.com/teruchan0823/',
            'russianbluecute_insta' : 'https://www.instagram.com/russianbluecute_insta/',
            'babette_and_the_pug' : 'https://www.instagram.com/babette_and_the_pug/',
            '_russianblue_cats' : 'https://www.instagram.com/_russianblue_cats/',
            'russianbluemoments' : 'https://www.instagram.com/russianbluemoments/',
            'russian_bluecats' : 'https://www.instagram.com/russian_bluecats/',
            'russianbluenyc' : 'https://www.instagram.com/russianbluenyc/',
            'arkeangelns_russianblue' : 'https://www.instagram.com/arkeangelns_russianblue/',
            'russian_blue_cats' : 'https://www.instagram.com/russian_blue_cats/',
            'xafiandauri' : 'https://www.instagram.com/xafiandauri/',
            'cins.kedi.sahiplendirme' : 'https://www.instagram.com/cins.kedi.sahiplendirme/',
            'russianblue_cats' : 'https://www.instagram.com/russianblue_cats/',
            'silvertown_cats' : 'https://www.instagram.com/silvertown_cats/',
            'russianbluehannibal' : 'https://www.instagram.com/russianbluehannibal/',
            'russianblue_lucky' : 'https://www.instagram.com/russianblue_lucky/',
            'boogieshmooshie' : 'https://www.instagram.com/boogieshmooshie/',
            'pekoe.blue' : 'https://www.instagram.com/pekoe.blue/',
            'the_russianblue_trio' : 'https://www.instagram.com/the_russianblue_trio/',
            'russianblue_travis' : 'https://www.instagram.com/russianblue_travis/',
            'russianbluecats' : 'https://www.instagram.com/russianbluecats/',
            'sereshka.sisi.russian_blue' : 'https://www.instagram.com/sereshka.sisi.russian_blue/',
            'sushi_russian_blue' : 'https://www.instagram.com/sushi_russian_blue/',
            'lukatherussianblue' : 'https://www.instagram.com/lukatherussianblue/'
        }
    elif d == 'pug':
        # dictionary of cs pages to acquire
        post_dictionary = {
            'itsdougthepug' : 'https://www.instagram.com/itsdougthepug/?hl=en',
            'pug.space' : 'https://www.instagram.com/pug.space/',
            'pug.fans' : 'https://www.instagram.com/pug.fans/',
            'pug_a_frenchie_and_brian' : 'https://www.instagram.com/pug_a_frenchie_and_brian/',
            'ronniewoodpug' : 'https://www.instagram.com/ronniewoodpug/',
            'circus_pugs' : 'https://www.instagram.com/circus_pugs/',
            'peeweesbigpugventure' : 'https://www.instagram.com/peeweesbigpugventure/',
            'mokatheadorablepug' : 'https://www.instagram.com/mokatheadorablepug/',
            'meetluluthepug' : 'https://www.instagram.com/meetluluthepug/',
            'pugs_lovers_world' : 'https://www.instagram.com/pugs_lovers_world/',
            'chickenthepug' : 'https://www.instagram.com/chickenthepug/',
            'itsmoosethepug' : 'https://www.instagram.com/itsmoosethepug/',
            'pugbeans' : 'https://www.instagram.com/pugbeans/',
            'thepuglifeofbentley' : 'https://www.instagram.com/thepuglifeofbentley/',
            'pugalier.sisters.and.pearl' : 'https://www.instagram.com/pugalier.sisters.and.pearl/',
            'pugonwheels' : 'https://www.instagram.com/pugonwheels/',
            'pugsngiggles' : 'https://www.instagram.com/pugsngiggles/',
            'pugloulou' : 'https://www.instagram.com/pugloulou/',
            'pugbasement' : 'https://www.instagram.com/pugbasement/',
            'pugareawesome' : 'https://www.instagram.com/pugareawesome/',
            'pug.dogz' : 'https://www.instagram.com/pug.dogz/',
            'pugsofinstagram' : 'https://www.instagram.com/pugsofinstagram/',
            'pugdashians' : 'https://www.instagram.com/pugdashians/',
            'the.pugs.of.insta' : 'https://www.instagram.com/the.pugs.of.insta/',
            'maggiethepug' : 'https://www.instagram.com/_maggiethepug/',
            'edgar_allanpug' : 'https://www.instagram.com/edgar_allanpug/',
            'worldofcutepugs' : 'https://www.instagram.com/worldofcutepugs/',
            'pug_ru' : 'https://www.instagram.com/pug_ru/',
            'pugloversclub' : 'https://www.instagram.com/pugloversclub/',
            'worldofpug' : 'https://www.instagram.com/worldofpug/',
            'pugvision_' : 'https://www.instagram.com/pugvision_/',
            'pugscenter' : 'https://www.instagram.com/pugscenter/',
            'pugs' : 'https://www.instagram.com/pugs/',
            'pug_a_frenchie_and_brian' : 'https://www.instagram.com/pug_a_frenchie_and_brian/',
            'itsbiglolo' : 'https://www.instagram.com/itsbiglolo'
        }
    return post_dictionary
