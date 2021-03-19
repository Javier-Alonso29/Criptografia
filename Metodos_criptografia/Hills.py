class hills:

    def __init__(self, mensaje, d, mensaje_clave):
        self.mensaje = mensaje.replace(" ","")
        self.d = d
        self.mensaje_clave = mensaje_clave
        self.matriz_clave = []
        self.matriz_mensaje = []

        self.encriptar()


    def procesar_texto(self):

        # Agregar los valores de la clave a la matriz clave

        numero_letra = 1
        list_mensaje_separado = []
        abs = 'abcdefghijklmnopqrstuvwxyz'

        for l in self.mensaje_clave:

            if numero_letra < self.d:

                list_mensaje_separado.append(l)
                numero_letra += 1
                continue

            if numero_letra == self.d:

                list_mensaje_separado.append(l)                
                list_mensaje_separado.append(':')
                numero_letra = 1
            
        ultimo_elemento = list_mensaje_separado[len(list_mensaje_separado)-1]

        # Si la ultima letra del arreglo es un : quiere decir que es una letra inpar por la cantida
        # de caracteres que tiene y por lo tanto se lo eliminamos

        if ultimo_elemento == ':':
            list_mensaje_separado.pop(len(list_mensaje_separado)-1)

        mensaje_separado = "".join(list_mensaje_separado)

        self.matriz_clave = mensaje_separado.split(':')

        numero_letra = 1
        lista_tempo_mensaje = []

        for l2 in self.mensaje:
            
            

            if numero_letra < self.d:
                lista_tempo_mensaje.append(l2)
                numero_letra += 1
                continue

            if numero_letra == self.d:
                lista_tempo_mensaje.append(l2)
                lista_tempo_mensaje.append(':')
                numero_letra = 1

        ultimo_elemento = lista_tempo_mensaje[len(lista_tempo_mensaje)-1]

        if ultimo_elemento == ':':
            lista_tempo_mensaje.pop(len(lista_tempo_mensaje)-1)

        mensaje_separado = "".join(lista_tempo_mensaje)

        self.matriz_mensaje = mensaje_separado.split(':')

        print(self.matriz_mensaje,'\n------\n',self.matriz_clave,'\n------\n')


    def encriptar(self):

        self.procesar_texto()

        abs = 'abcdefghijklmnopqrstuvwxyz'
        valores = []
        indice = 0

        rclave = len(self.matriz_clave)
        cclave = len(self.matriz_clave[0])

        rmensaje = len(self.matriz_mensaje)
        cmensaje = len(self.matriz_mensaje[0])

        for r in range(0,rmensaje):

            for c in range(0,cclave):

                # print(r,c)

                for k in range(0,rclave):

                    print(self.matriz_mensaje[r][k],' ',self.matriz_clave[k][c])

        
        
        print('Hasta aqui me quede, no logre hacer la multiplicacion de las matrices :c')



                                





        
                


        

        
    