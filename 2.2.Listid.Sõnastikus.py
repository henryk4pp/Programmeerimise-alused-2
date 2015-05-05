def listid_sõnastikus(list1,list2):
    sõnastik = {}
    for i in range(len(list1)):
        võti = list1[i]
        väärtus = list2[i]
        sõnastik[võti] = väärtus
    return sõnastik


#def listid_sõnastikus2(list1,list2):
    
#    return dict(zip(list1,list2))
