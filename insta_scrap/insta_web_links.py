insta_links = {'unicef' : 'https://www.instagram.com/usf_unicef/',
               'arabsatusf' : 'https://www.instagram.com/arabsatusf/',
               'bootsusf' : 'https://www.instagram.com/boostusf/',
               'bridgesinternational' : 'https://www.instagram.com/usfbridgesinternational',
               'usf_casa' : 'https://www.instagram.com/usf_casa/',
               'intousf' : 'https://www.instagram.com/intousf/',
               'usf.hsc': 'https://www.instagram.com/usf.hsc/',
               'boricuas_usf' : 'https://www.instagram.com/boricuas_usf/,',
               'acdusf' : 'https://instagram.com/acdusf/',
               'isaatusf' : 'https://www.instagram.com/isaatusf/',
               'usf.asa' : 'https://www.instagram.com/usf.asa/',
               'nesa.usf' : 'https://www.instagram.com/nesa.usf/'}
def keys_list():
    keys_list = []
    for i, (k, v) in enumerate(insta_links.items()):
        keys_list.append(k)
    return keys_list

def link(index, dict_index):
    link = insta_links[dict_index[index]]
    return link
