
def vahe(hulk1,hulk2):
    a=set()
    for el in hulk1:
        if el not in hulk2:
            a.add(el)
    return a

            
