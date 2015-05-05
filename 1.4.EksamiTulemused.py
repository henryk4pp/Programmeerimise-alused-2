# faili avamine
file = open("Eksam.txt")

# tulemuste lugemine tabelisse
tabel = []
nimed = []


for rida in file :
   # eralda tudengi nimi
   jupid = rida.split("|")
   nimed.append(jupid[0].strip())

   # võta ülejäänud osa juppideks
   tulemuste_jupid = jupid[1].split(",")

   # märgi tudengi tulemused tabelisse
   tulemused = []
   for tulemus in tulemuste_jupid:
       tulemused.append(int(tulemus))
   tabel.append(tulemused)
   k = len(tulemuste_jupid)

# nüüd on olemas tabel, milles on ridades inimestele vastavad tulemused


# faili sulgemine
file.close()


n = len(tabel)


# Tulemuste väljastamine
print("Tulemused:")
for i in range(n):
    print("{0:>2}. {1:<25}: ".format(i+1, nimed[i]), end=' ')
    for j in range(k) :
        print("{0:>2}".format(tabel[i][j]), end=' ')
    print()

#lõpus on reavahetus    
    


print("-----------------")
# reasummad
for i in range(n) :
    summa = 0
    for j in range(k) :
        summa += tabel[i][j]

    print("{0} sai {1} punkti".format(nimed[i], summa))

print("-----------------")

for i in range(k):
    summa = 0
    for j in range(n):
        summa += tabel[j][i]
    
    print("{0}.ülesande kesmine punktide arv oli {1}".format(i+1,round(summa/j,2)))

print("-----------------")

for i in range(k):
   a = 0
   for j in range(n):
      if tabel[j][i] > a:
         a = tabel[j][i]

   print("{0}.ülesande kõrgeim punktide arv oli {1}".format(i+1,a))

print("-----------------")
     
for i in range(n):
   nullid = 0
   kümned = 0
   for j in range(k):
      if tabel[i][j] == 0:
         nullid +=1
      if tabel[i][j] == 10:
         kümned +=1
   if nullid and kümned != 0:
      print("{0} tulemused olid seinast seina".format(nimed[i]))

print("-----------------")

tulemused = []
hulk = set()

for i in range(n):
   summa = 0
   for j in range(k):
      summa += tabel[i][j]
   tulemused.append(summa)

for i in range(len(tulemused)):
   if abs(tulemused[i]-tulemused[i-1]) <= 2:
      hulk.add(nimed[i])
      hulk.add(nimed[i-1])

print(hulk, "kahtlustatakse spikerdamises")

print("-----------------")

tabel1 = tabel[:]

for i in range(k):
   a = 0
   for j in range(n):
      if tabel[j][i] > a:
         a = tabel[j][i]
   if a != 10:
      for j in range(n):
         tabel1[j][i] = tabel1[j][i] * a/10


for i in range(n):
   print("{0:>2}.{1:<25}:".format(i+1,nimed[i]), end= " ")
   for j in range(k):
      print("{0:>2}".format(tabel1[i][j]), end=" " )
   print()



