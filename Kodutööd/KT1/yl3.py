def sudoku():

   f = open("sudoku.txt")
   tabel = []

   for rida in f:
       jupid = rida.split()
    
       sudoku_rida = []

       for jupp in jupid:
           sudoku_rida.append(int(jupp))
       tabel.append(sudoku_rida)

   f.close()
   return tabel
        
      
