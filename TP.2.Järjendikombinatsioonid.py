
def korrutis(järjend):
    a= järjend
    c = []
    for i in range(len(järjend)):
        b = []
        for j in range(i+1,len(järjend)):
            e = a[i]*a[j]
            b.append(e)
        if  b != []:
            c.append(b)
    return c
        
            
            
        
