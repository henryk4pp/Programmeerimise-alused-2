
f = open("telefoniraamat.txt")

telefoniraamat = {}

for rida in f:
    nimi = rida.split("-")[0]
    telefon = rida.split("-")[1].strip()
    telefoniraamat[nimi] = telefon

sisestus = input("Sisesta nimi: ")
print(telefoniraamat[nimi])
