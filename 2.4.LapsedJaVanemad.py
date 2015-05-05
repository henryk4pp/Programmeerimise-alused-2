
def seosta_lapsed_ja_vanemad(nimedefail,lastefail):
    koodid_nimedeks = {}
    lapsed_vanematele = {}

    f = open(lastefail)
    g = open(nimedefail)
  
    for rida in g:
        koodid_nimedeks[rida.split()[0]] = rida.split()[1] + " " + rida.split()[2]


    
    for rida in f:
        vanem = koodid_nimedeks[rida.split()[0]]
        laps = koodid_nimedeks[rida.split()[1]]


        if vanem in lapsed_vanematele:
            lapsed_vanematele[vanem] = (lapsed_vanematele[vanem],laps)
            
        else:
            lapsed_vanematele[vanem] = laps

    return lapsed_vanematele
        
        
