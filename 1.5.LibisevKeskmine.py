# hindade lugemine failist
hinnad = [] # hinnad on tavaline ühemõõtmeline järjend
f = open("aktsiad.txt")
for rida in f:
    hinnad.append(float(rida))
f.close()


# keskmiste arvutamine
k = int(input("Mitut eelnevat päeva soovid keskmise arvutamisel kasutada: "))

# kuna meil on vaja k eelnevat päeva, siis alustame indeksist k
for i in range(len(hinnad)):
    print("{0:>2}. päev, hind oli {1:>6.2f}.".format(i, hinnad[i]), end=' ')

    # eelneva k päeva keskmist saame näidata alates päevast k
    if i >= k:
        k_eelmise_summa = 0
        for j in range(i-k, i):
            k_eelmise_summa = k_eelmise_summa + hinnad[j]
        keskmine = k_eelmise_summa / k
        print("Eelnenud {0} päeva keskmine hind oli {1:>6.2f}".format(k, keskmine))
    else:
        # esimeste päevade juurde paneme ainult reavahetuse
        print()
