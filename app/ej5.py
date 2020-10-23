import string
import random

def generarCadenaAleatoria():
    cadena = ""
    tamanio = random.randint(2,8)
    for i in range(tamanio):
        if (random.random() > 0.5):
            cadena += "["
        else:
            cadena += "]"
    return cadena

def comprobarBalanceo(cadena):
    p = ""
    balanceo = True
    i = 0
    while i < len(cadena) and balanceo:
        if cadena[i] == '[':
            p += '['
        else:
            if len(p) is 0:
                balanceo = False
            else:
                p = p[:-1]

        i += 1

    if balanceo and len(p) is 0:
        solucion = "Esta cadena está balanceada"
    else:
        solucion = "Esta cadena NO está balanceada"
    
    return solucion
    
