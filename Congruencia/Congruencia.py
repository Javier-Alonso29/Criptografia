
def calcula_congruencia(a,b,n):

    for i in range(1,a+1):

        multi = i * n

        if (a == (b + multi)):

            print('El valor de k es:', i)
            break

        


a = int(input('¿Cual es el valor del primer numero?\n'))
b = int(input('¿Cual es el valor del segundo numero?\n'))
n = int(input('¿Cual es el valor del modulo numero?\n'))

calcula_congruencia(a,b,n)