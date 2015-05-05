def teisenda(järjend):
    # teen järjendist koopia
    uus = järjend[:]

    for i in range(len(uus)):
        for j in range(i+1):
            if uus[j] < uus[i]:
                uus[i], uus[j] = uus[j], uus[i]
        print(uus)
    return uus
