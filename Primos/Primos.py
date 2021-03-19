import math, random

def fuerza_bruta(num):
    print('Fuerza bruta')
    
    contador_divisores = 0
    contador_pasos = 1

    for i in range(1, num+1):
        

        divisor = num % i
        contador_pasos+= 2

        if divisor == 0:
            contador_pasos+= 1
            contador_divisores += 1

    if contador_divisores > 2:
        contador_pasos+= 1
        print('El numero', num, 'no es primo')

    if contador_divisores == 2:
        contador_pasos+= 1
        print('El numero', num, 'si es primo')

    print('La cantidad de pasos que hizo fue de',contador_pasos)

    print('----------------------------------')


def raiz_n(num):
    print('Raiz de numero')
    contador_pasos = 1

    raiz = round(math.sqrt(num))
    contador_divisores = False

    contador_pasos+= 2

    for i in range(2, raiz+1):

        divisor = num % i
        contador_pasos+= 2

        if divisor == 0:
            contador_divisores = True
            contador_pasos+= 1

    if contador_divisores == True:
        print('El numero',num,'no es primo')
        contador_pasos+= 1
    
    if contador_divisores == False:
        print('El numero',num,'si es primo')
        contador_pasos+= 1

    print('La cantidad de pasos que hizo fue de',contador_pasos)

    print('----------------------------------\n')

def fermat(num,k):
    print('Fermat')
    contador_pasos = 1

    if num == 2:
        
        contador_pasos+= 1
        print('La cantidad de pasos que hizo fue de',contador_pasos)
        return True

    if num % 2 == 0:
        
        contador_pasos+= 1
        print('La cantidad de pasos que hizo fue de',contador_pasos)
        return False

    for i in range(1,k+1):

        a = random.randint(1, num-1)

        contador_pasos+= 2

        if pow(a, num-1) % num != 1:
            contador_pasos+= 1
            print('La cantidad de pasos que hizo fue de',contador_pasos)
            return False

    print('La cantidad de pasos que hizo fue de',contador_pasos)
    return True


numero = int(input('¿Cual es el numero?\n'))
fuerza_bruta(numero)
raiz_n(numero)
k = int(input('¿Cual es el valor de k?\n'))
respuesta = fermat(numero, k)

if respuesta == True:
    print('El numero',numero,'es un posible numero primo')

if respuesta == False:
    print('Es un compuesto')

print('----------------------------------\n')
