def calcular_distancia(val1, val2):

    arr_bits_v1 = [bin(ord(c))[2:].zfill(8) for c in val1]

    arr_bits_v2 = [bin(ord(c))[2:].zfill(8) for c in val2]

    print(arr_bits_v1)
    print(arr_bits_v2)

    contador = 0
    distancia = 0

    for p in arr_bits_v1:
        indice = arr_bits_v1.index(p)

        for b in p:

            b1 = arr_bits_v2[indice][contador]

            if b != b1:

                distancia += 1

            contador += 1

        if contador == 8:

            contador = 0
    
    return distancia



cadena_1 = input('¿Cual es la primer cadena de texto?\n')
cadena_2 = input('¿Cual es la segunda cadena de texto?\n')


if len(cadena_1) == len(cadena_2):

    distancia = calcular_distancia(cadena_1.lower(), cadena_2.lower())
    print('La distancia es de',distancia)

else:

    print('Los textos deben de tener la misma longitud')



