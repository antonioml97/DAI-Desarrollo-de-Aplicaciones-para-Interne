import random


numero_a_adivinar=random.randint(1, 100)

print(numero_a_adivinar)

print("Estoy pensado un numero... Adivinalo esta entre 1 y 100")
numero_usuario=int(input());

for i in range(0,10):
    if numero_a_adivinar == numero_usuario :
        print("Lo has adivinado! Es " + str(numero_usuario) )
        break

    elif numero_a_adivinar > numero_usuario :
        print("El numero es más grande")
    else:
        print("El numero es más pequeño")

    if i == 9:
        print("Ya no te quendas máss intentos")    
        break
    
    print("Dime otro número")
    numero_usuario=int(input())