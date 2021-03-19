from math import log
import sys

def entropia(cantidad_estados):
    
    sumatoria = 0.0
    entropia = 0.0

    for i in range(cantidad_estados):

        print('¿Cual es el valor de',i+1,'?')
        probabilidad = float(input())
        arr_probabilidades.append(probabilidad)

        sumatoria += probabilidad

    if sumatoria == 1:
        print('La suma de las probabilidades no puede ser igual a 1')
        sys.exit(0)

    else:

        for p in arr_probabilidades:

            entropia += (p * log(p,2))
            print(entropia)

        entropia = -(entropia)

        return entropia



cantidad_estados = int(input('¿Cuantas probabilidades son?\n'))
arr_probabilidades = [] 

resultado = entropia(cantidad_estados)

print('Tu resultado es: ',resultado)