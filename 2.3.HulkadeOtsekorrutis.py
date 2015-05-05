
def korrutis(hulk1,hulk2):
    
    a= []
    hulk1 = list(hulk1)
    hulk2 = list(hulk2)
    for i in range(len(hulk1)):
        b = []
        b.append(hulk1[i])

        for j in range(len(hulk2)):
            
            b.append(hulk2[j])
            
        a.append(b)
    return a
        
            
            
        
