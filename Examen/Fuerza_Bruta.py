def fuerza_bruta(num, k):
    print('Fuerza bruta')
    
    contador_divisores = 0
    contador_pasos = 1

    for i in range(1, num+1):

        for j in range(1, k+1):

            if i == j:
        
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


numero = int(input('¿Cual es el numero?\n'))
k = int(input('¿Cual es el valor de k?\n'))

fuerza_bruta(numero, k)