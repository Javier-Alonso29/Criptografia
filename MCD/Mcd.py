
def calcular_mcd(dividendo,divisor):

    dividendo_original = dividendo
    divisor_original = divisor

    continua = True


    while continua:

        print('MCD(',dividendo,',',divisor,')')

        res = dividendo % divisor

        if res == 0:
            continua = False
            print('MCD(',dividendo_original,',',divisor_original,') = ',divisor)
        else:
            
            dividendo = divisor
            divisor = res


numero1 = int(input('¿Cual es el valor del numero 1?\n'))
numero2 = int(input('¿Cual es el valor del numero 2?\n'))

calcular_mcd(numero1,numero2)