import time
import decimal


def float_to_str(f):
    ctx = decimal.Context()
    ctx.prec = 20

    d1 = ctx.create_decimal(repr(f))
    return format(d1, 'f')

def ordena(lista):
  return burbuja(lista)+mergeSort(lista)

def burbuja(lista):
  start = time.process_time()

  vector = lista.split(',')

  for i in range(len(vector)-1):
    for j in range(0, len(vector)-i-1):
      if vector[j] > vector[j+1] :
        vector[j], vector[j+1] = vector[j+1], vector[j]
    
  end = time.process_time()
  tiempo= end - start

  cadena = "<h1>Ordenación por burbuja</h1>"
  cadena += "<p>Vector inicial: "+lista+"</p>"

  cadena = cadena + "<p>Cadena final: "
  for i in range(0,len(vector)):
    cadena += vector[i]
    if i != len(vector)-1:
      cadena += ","

  
  cadena+="</p>"
  cadena += "<h3>Ha tardado en tiempo: "+ float_to_str(tiempo)  +"</h3>"
  return cadena

def mergeSort(lista):
  start = time.process_time()

  A = lista.split(',')
  for i in range(len(A)):
    min_idx = i
    for j in range(i+1, len(A)):
      if A[min_idx] > A[j]:
        min_idx = j
    A[i], A[min_idx] = A[min_idx], A[i]

  end = time.process_time()
  tiempo= end - start

  cadena = "<h1>Ordenación por selección</h1>"
  cadena += "<p>Vector inicial: "+lista+"</p>"

  cadena += "<p>Cadena final: "
  for i in range(0,len(A)):
    cadena += A[i]
    if i != len(A)-1:
      cadena += ","

  cadena+="</p>"
  cadena += "<h3>Ha tardado en tiempo: "+ float_to_str(tiempo)  +"</h3>"
  return cadena