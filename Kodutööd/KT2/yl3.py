
def võitjaks(maatriks,märk):
     diagonaal1 = 0
     diagonaal2 = 0 
     for i in range(3):
        rida1 = 0
        rida2 = 0
        for j in range(3):
            if i == j and maatriks[i][j] == märk:
                diagonaal1 +=1
            if maatriks[i][j] == märk:
                rida1 +=1
            if i + j == 2 and maatriks[i][j] == märk:
                diagonaal2 +=1
            if maatriks[j][i] == märk:
                rida2 +=1
            if diagonaal1 == 3 or diagonaal2 == 3 or rida1 == 3 or rida2 == 3:
                return märk
     


def võitja(maatriks):
    if võitjaks(maatriks, "X") == "X" and not võitjaks(maatriks, "O") == "O":
        return võitjaks(maatriks,"X")
    if võitjaks(maatriks, "O") == "O" and not võitjaks(maatriks, "X") == "X":
        return võitjaks(maatriks,"O")
    if võitjaks(maatriks, "X") == "X" and võitjaks(maatriks, "O") == "O":
        return "?"
    else:
        return "?"
    


 
    
