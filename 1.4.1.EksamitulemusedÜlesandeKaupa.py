file = open("Eksam.txt")


yl_kaupa = []

for rida in file:

    jupid = rida.split("|")
    tulemuste_jupid = jupid[1].split(",")

    for i in range(7):

        yl_kaupa.append(int(jupid[i]))
