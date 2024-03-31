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
               'nesa.usf' : 'https://www.instagram.com/nesa.usf/',
               'belsausf' : 'https://www.instagram.com/belsausf/',
               'lsa_usf' : 'https://www.instagram.com/lsa_usf/',
               'eso_usf' : 'https://www.instagram.com/eso_usf/',
               'pdtampa' : 'https://www.instagram.com/pdtampa/',
               'sos_usf' : 'https://www.instagram.com/sos_usf/',
               'usf_nihongobu' : 'https://www.instagram.com/usf_nihongobu/',
               'usf_je' : 'https://www.instagram.com/usf_je/',
               'usf_tsa' : 'https://www.instagram.com/usf_tsa/',
               'censa_usf' : 'https://www.instagram.com/censa_usf/',
               'usf_hillel' : 'https://www.instagram.com/usf_hillel/',
               'visa.usf' : 'https://www.instagram.com/visa.usf/',
               'colsausf' : 'https://www.instagram.com/colsausf/',
               'usf_bullsformoffitt' : 'https://www.instagram.com/usf_bullsformoffitt/',
               'hexaconsulting' : 'https://www.instagram.com/hexaconsulting/',
               'iiseusf' : 'https://www.instagram.com/iiseusf/',
               'usffoi' : 'https://www.instagram.com/usffoi/',
               'usf.mbsm' : 'https://www.instagram.com/usf.mbsm/',
               'usfaiche' : 'https://www.instagram.com/usfaiche/',
               'kwusfclub' : 'https://www.instagram.com/kwusfclub/',
               'uzsc.usf' : 'https://www.instagram.com/uzsc.usf/',
               'tmcusf' : 'https://www.instagram.com/tmcusf/',
               'bsa.usf' : 'https://www.instagram.com/bsa.usf/',
               'usfswe' : 'https://www.instagram.com/usfswe/'
}
def clubs_list():
    clubs_list = []
    for i, (k, v) in enumerate(insta_links.items()):
        clubs_list.append(k)
    return clubs_list

def link(index, dict_index):
    link = insta_links[dict_index[index]]
    return link
