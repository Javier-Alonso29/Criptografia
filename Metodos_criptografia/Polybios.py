class polybios:
    
    def __init__(self,mensaje):
        self.mensaje_original = mensaje
        self.mensaje = list(mensaje.lower())
        self.arregloIndices = []
        self.mensaje_resultado = []
        self.tabla_valores = [
            ['a','b','c','d','e'],
            ['f','g','h','i,j','k'],
            ['l','m','n','o','p'],
            ['q','r','s','t','u'],
            ['v','w','x','y','z']
        ]
        self.tabla_valores_resultados = [
            ['AA','AB','AC','AD','AE'],
            ['BA','BB','BC','BD','BE'],
            ['CA','CB','CC','CD','CE'],
            ['DA','DB','DC','DD','DE'],
            ['EA','EB','EC','ED','EE']
        ]

        self.encriptar()

    def evaluarTexto(self):

        for x in range(len(self.mensaje)):

            if(self.mensaje[x] == 'j' or self.mensaje[x] == 'i'):

                # Remplazamos las J o las I por 'i,j'
                self.mensaje[x] = 'i,j'


    def encriptar(self):

        self.evaluarTexto()
        
        # Letra del mensaje
        for l in self.mensaje:
            
            # filas de tabla valores
            for i in self.tabla_valores:

                # letras que estan detro de cada filas
                for x in i:

                    if(l == x):
                        indice_letra_vertical = self.tabla_valores.index(i)
                        indice_letra_horizontal = i.index(x)
                        valor = str(indice_letra_vertical) +':'+ str(indice_letra_horizontal)
                        self.arregloIndices.append(valor)

        self.asignaValores()

    def asignaValores(self):

        for i in self.arregloIndices:
            
            arr_tempo = i.split(':')

            valorY = int(arr_tempo[0])
            valorX = int(arr_tempo[1])

            resultado = self.tabla_valores_resultados[valorY][valorX]

            self.mensaje_resultado.append(resultado)



       


                    
                    


        
    