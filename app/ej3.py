def CribadeEratóstenes(n):
  print(n)
  a = [True] * (n-1)  
  a[0] = a[1] = False 
  for (i, isprime) in enumerate(a): 
    if isprime: 
        for n in range(i*i, n-1, i):  
            a[n] = False 

  cadena = "<h1>Números primos hasta "+str(n)+"</h1>"
  for p in range(0,n-1):
    if a[p]:
      cadena += str(p)+", "
    
  """ Borra el ultimo ',' borra los dos ultimos caracter """
  cadena = cadena[:-2] 
  return cadena
