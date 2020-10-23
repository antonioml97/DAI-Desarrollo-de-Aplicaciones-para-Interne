def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)

def leerFichero():
    n = open("numero.txt", "r")
    numero = int(n.read())
    n.close()
    return numero

def escribirFichero(numero):
    salida = open('ficheroNumeroSalida.txt', "w")
    salida.write('SUCESIÓN DE FIBONACCI: \n')
    salida.write(str(fib(numero)))
    salida.write('\n')
    salida.close()