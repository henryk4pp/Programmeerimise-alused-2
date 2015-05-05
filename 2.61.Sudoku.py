hulk = {"1","2","3","4","5","6","7","8","9"}


import sys



failinimi = sys.argv[1]


def loe_tabel(failinimi):
    tabel = []
    
    f = open(failinimi)
    for rida in f:
        jupid = rida.split()
        tabel.append(jupid)
    return tabel

            
def rida_on_korras(tabel,rea_indeks):
    for i in range(9):
        if tabel[rea_indeks][i] not in hulk:
            return False
    if len(set(tabel[rea_indeks])) != 9:
        return False
    else:
        return True

def veerg_on_korras(tabel,veeru_indeks):
    numbrid = set()
    for i in range(9):
        numbrid.add(tabel[i][veeru_indeks])

        if tabel[i][veeru_indeks] not in hulk:
            return False
    
    if len(numbrid) != 9:
        return False
    else:
        return True

def ruut_3x3_on_korras(tabel,nurga_rea_indeks,nurga_veeru_indeks):
    numbrid = []
    for i in range(nurga_rea_indeks-3,nurga_rea_indeks):
        for j in range(nurga_veeru_indeks-3,nurga_veeru_indeks):
            numbrid.append(tabel[i][j])
    if len(set(numbrid)) == 9:
        return True
    else:
        return False


def kontroll():

    tingimused = 0

    maatriks = loe_tabel(failinimi)            
    for i in range(9):
        if rida_on_korras(maatriks,i) != True:
            print("Viga on " + str(i+1) + " reas")
            tingimused +=1

        if veerg_on_korras(maatriks,i) != True:
            print("Viga on " + str(i+1) + " veerus")
            tingimused +=1

    for i in range(1,4):
        for j in range(1,4):
            if ruut_3x3_on_korras(maatriks,i*3,j*3) != True:
                print("Viga on ruudus " + str(3*i-3) + "-" + str(3*i) + " rida : " + str(3*j-3) + "-" + str(3*j) + " veerg.")
                tingimused +=1

    if tingimused == 0:
        print("OK")

kontroll()




