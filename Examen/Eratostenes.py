
def eratostenes(n):
    # Arrego que almacena los numeros de 2 hasta n
    numeros_base = [i for i in range(2,n+1)]
    # Arreglo donde guardaremos los numeros encontrados
    primos = []
    # Arreglo que guarda los numeros que no son primos en el recorrido
    no_primos = []
    
    arr_tempo = []

    for i in numeros_base:

        # En caso de que el numero actual ya haya
        # sido marcado como numero no primo
        if i in no_primos:

            continue
        
        # Obtengo los multiplos del numero en el que estoy iterando hasta 
        # el numero n con saltos saltos del numero actual
        for j in range(i*2, n + 1, i):

            # Agrego los valores obtenidos como numeros no primos
            no_primos.append(j)
            # Arreglo temporal para identificar el conjunto de numeros no
            # primos del numero primo y mostrar aquellos numeros que se tachan con
            # ese numero primo
            arr_tempo.append(j)


        if arr_tempo != []:

            print('Se toma el',i,'como primo y se tachan',arr_tempo)

        else:

            print('Se toma el',i,'ya no hay mas numeros para tachar')

        primos.append(i)
        arr_tempo.clear()


n = int(input('¿Cual es el valor de n?\n'))
eratostenes(n)