#puudusin tunnist, lahendused pruugivad olla pisut teistsugused kui seal

def summa(täisarv,ujukomaarv,sone):
    return str(täisarv) + " " + str(ujukomaarv) + " " + str(sone)

def imeliksumma(täisarv,ujukomaarv,sone):
   a=0
   
   if type(täisarv) != str:
       a += float(täisarv)
   if type(ujukomaarv) != str:
       a += float(ujukomaarv)
   if type(sone) != str:
       a += float(sone)
   if type(täisarv) == str:
       b = täisarv
   if type(ujukomaarv) == str:
       b = ujukomaarv
   if type(sone) == str:
       b = sone        

   return str(a) + " " + b
           
def printsumma(täisarv,ujukomaarv,sone):
    imelik = imeliksumma(täisarv,ujukomaarv,sone)
    print(imelik)

def tehe(arv):
    return (arv + 2)*3

def tehted(järjend):
    a= []
    for el in järjend:
        tulemus = tehe(el)
        a = a + [tulemus]
    return a

def tehted_paaritu(järjend):
    arvud = tehted(järjend)
    a = []
    for el in arvud:
        if el % 2 != 0:
            a = a + [el]
    return(a)


# Siin on easygui osa.

import easygui
from random import randint

täis = easygui.enterbox("Sisesta siia täisarv")
ujukoma = easygui.enterbox("Sisesta siia ujukomaarv")
sõne = easygui.enterbox("Sisesta siia sone")

if täis == "":
    täis = randint(0,12)

# Või randint (1,11) kui tõlgendada vahemikku rangelt matemaatiliselt.

easygui.msgbox((summa(täis,ujukoma,sõne)))
