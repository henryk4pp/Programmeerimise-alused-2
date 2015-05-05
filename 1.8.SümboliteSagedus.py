

def erinevad_sümbolid(sõne):
    a = set()
    for el in sõne:
        a.add(el)
    print(a)

def sümbolite_sagedus(sõne):
    sõnastik = {}
    for el in sõne:
        a = sõne.count(el)
        sõnastik[el]=a
    return sõnastik
