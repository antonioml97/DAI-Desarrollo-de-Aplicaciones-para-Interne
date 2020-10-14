import numpy as np

def dibujaMatriz(M):
 for i in range(len(M)):
    print ('[')
    for j in range(len(M[i])):
        print ('{:>3s}'.format(str(M[i][j])) )
    print (']')

m = np.zeros((3, 1))

dibujaMatriz(m)