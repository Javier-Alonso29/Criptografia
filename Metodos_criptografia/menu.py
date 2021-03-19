from Polybios import polybios
from Cesar import cesar
from Alberti import alberti
from Vigenere import vigenere
from Playfair import playfair
from Hills import hills

continuar = True

while(continuar):
   
    print('1) Polybios\n2) Cesar\n3) Alberti\n4) Vigenere\n5) Playfair\n6) Hills\n7) salir')

    opcion = int(input('¿Cual metodo de encriptamiento quieres usar?\n'))
    mensaje = input('¿Cual es tu mensaje?\n')

    if(opcion == 1):
        
        poly = polybios(mensaje)
        print('El mensaje resultado es:')
        
        print('----------------------\n')
        print(poly.mensaje_resultado)
        print('\n----------------------\n')

    elif(opcion == 2):

        numero_desplazamiento = int(input('¿Cuanto quieres desplazar el abecedario?\n'))

        ces = cesar(mensaje,numero_desplazamiento)
        print('El mensaje resultado es:')
        
        print('----------------------\n')
        print(ces.mensaje_res)
        print('\n----------------------\n')

    elif(opcion == 3):

        clave = input('¿Cual es la clave?\n')

        albe = alberti(mensaje, clave);

        print('El mensaje resultado es:')

        print('----------------------\n')
        print(albe.mensaje_resultado)
        print('\n----------------------\n')

    elif(opcion == 4):

        clave = input('¿Cual es la clave?\n')

        vige = vigenere(mensaje,clave)

        print('El mensaje resultado es:')

        print('----------------------\n')
        print(vige.mensaje_resultado)
        print('\n----------------------\n')

    elif(opcion == 5):

        play = playfair(mensaje) 

        print('El mensaje resultado es: ')

        print('----------------------\n')
        print(play.mensaje_resultado)
        print('\n----------------------\n')

    elif(opcion == 6):

        # Validar que la longitud del mensaje sea par

        long_mensaje = len(mensaje.replace(" ",""))

        if long_mensaje % 2 != 0:

            # Agregamos una letra al mensaje para hacerlo par 

            mensaje += '.'

            long_mensaje = len(mensaje.replace(" ",""))

        print('Tu clave debe de ser de una longitud de',long_mensaje,'caracteres')

        clave = input('¿Cual es la clave?\n')

        lon_clave = len(clave)

        if long_mensaje == lon_clave:

            d = lon_clave / 2

            hill = hills(mensaje,d,clave)

        else:
            print('El mensaje es mas largo que la clave, por lo que esta no lo soporta')

            


        # hill = hills(mensaje,d,mensaje_clave)


        
    else:
        continuar = False

else:
    print('Bye')