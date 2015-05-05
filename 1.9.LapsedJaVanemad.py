
#nimedefail on nimed.txt
#lastefail on lapsed.txt



    
def seosta_lapsed_ja_vanemad(nimedefail,lastefail):
    seos = {}
    lapsed = {}
    f = open(lastefail)
    g = open(nimedefail)
    for rida in g:
        seos[rida.split()[0]] = rida.split()[1] + " " + rida.split()[2]

# Esimene seos ütleb, millisele isikukoodile vastab milline nimi

    for rida in f:
       
        if  seos[rida.split()[0]] in lapsed:
            seos[rida.split()[0]].append(seos[rida.split()[1]])
        
                                        
# Kui vanem on juba sõnastikus olemas, tuleb uus laps lisada appendiga
# d[value].append(value)

        else:   
            lapsed[seos[rida.split()[0]]] = seos[rida.split()[1]]
        print(lapsed)


 

# Teine seos annab iga lapse võtmeks enda vanemale, so. vanemale annab lapse
    
