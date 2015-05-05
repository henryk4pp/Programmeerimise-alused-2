f = open("sudoku.txt")

sudoku_tabel = []
for rida in f:
    jupid = rida.split()

    # kõigepealt teen abimuutujasse valmis ühe tabeli rea ...
    sudoku_rida = []

    for jupp in jupid:
        sudoku_rida.append(int(jupp))

    # ... ja siis lisan selle tabelisse
    sudoku_tabel.append(sudoku_rida)

f.close()
print(sudoku_tabel)
