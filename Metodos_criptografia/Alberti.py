class alberti:

    def __init__(self, mensaje, clave):
        self.clave = clave
        self.letras = 'abcdefghijklmnopqrstuvwxyz'
        self.mensaje = mensaje
        self.mensaje_resultado = ''
        self.matriz_alfabetos = []
        self.encriptar()
        

    def generar_discos(self):

        for i in self.letras:
    
            for x in self.clave:

                if i == x:

                    arr_tempo = []

                    indice = self.letras.index(x)

                    while(indice < len(self.letras) ):

                        arr_temporal = []
                        
                        valor = self.letras[indice]

                        indice += 1

                        arr_tempo.append(valor)

                        if indice == len(self.letras):

                            indice2 = 0

                            if(valor == 'z'):
                                valor = self.letras[0]

                            while(valor != x):

                                valor = self.letras[indice2]

                                if(valor == x):
                                    break

                                indice2 += 1

                                arr_tempo.append(valor)

                    self.matriz_alfabetos.append(arr_tempo)


    def encriptar(self):
        
        self.generar_discos()

        print('Abecedario:')

        print(list(self.letras))

        print('Tus discos son:')
        for abs in self.matriz_alfabetos:
            print(abs)
        
        print('\n')
        
        arr_let_mensaje = []

        for l in self.mensaje:

            for l2 in self.letras:

                if (l == l2):

                    arr_let_mensaje.append(self.letras.index(l))

        for pos in arr_let_mensaje:
            
            for abs in self.matriz_alfabetos:

                for l in abs:

                    if (pos == abs.index(l)):

                        self.mensaje_resultado += l


                        


            

                

                    

                        


                    





        





