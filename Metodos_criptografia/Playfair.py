
class playfair:

    
    def __init__(self, mensaje):
        self.mensaje = mensaje.replace(" ","")
        self.arr_palabras_separadas = []
        self.mensaje_resultado = ''
        self.tabla_valores = [
            ['a','b','c','d','e'],
            ['f','g','h','i','k'],
            ['l','m','n','o','p'],
            ['q','r','s','t','u'],
            ['v','w','x','y','z']
        ]

        self.encriptar()
    
    def procesar_texto(self):

        list_mensaje_separado = []
        numero_letra = 1

        for l in self.mensaje:

            index_letra = self.mensaje.index(l)

            if(self.mensaje[index_letra] == 'j' or self.mensaje[index_letra] == 'i'):
                    l = 'i'

            if numero_letra < 2:

                list_mensaje_separado.append(l)
                numero_letra += 1
                continue

            if numero_letra == 2:

                list_mensaje_separado.append(l)                
                list_mensaje_separado.append(':')
                numero_letra = 1

        ultimo_elemento = list_mensaje_separado[len(list_mensaje_separado)-1]

        # Si la ultima letra del arreglo es un : quiere decir que es una letra inpar por la cantida
        # de caracteres que tiene y por lo tanto se lo eliminamos

        if ultimo_elemento == ':':
            list_mensaje_separado.pop(len(list_mensaje_separado)-1)

        mensaje_separado = "".join(list_mensaje_separado)

        self.arr_palabras_separadas = mensaje_separado.split(':')

        for i in self.arr_palabras_separadas:

            if len(i) < 2:

                # En caso de que el arreglo no tenga 2 letras le agregamos una x
                conjunto = i + 'x'

                index_letra = self.arr_palabras_separadas.index(i)

                self.arr_palabras_separadas[index_letra] = conjunto  


    def encriptar(self):

        self.procesar_texto()

        # Se viene lo cabron

        for part in self.arr_palabras_separadas:


            arr = list(part)
            m1 = arr[0]
            m2 = arr[1]

            for abs in self.tabla_valores:

                for l1 in abs:

                    if m1 == l1:

                        fila_c1 = self.tabla_valores.index(abs)
                        columna_c1 = abs.index(l1)

                        for abs_2 in self.tabla_valores:

                            for l2 in abs_2:

                                if m2 == l2:

                                    fila_c2 = self.tabla_valores.index(abs_2)
                                    columna_c2 = abs_2.index(l2)

                                    # Empezamos a validar los casos
                                    
                                    # Caso 1 m1 y m2 tienen las mismas filas
                                    if fila_c1 == fila_c2 :
                                        
                                        # posibles indices de c1 y c2
                                        indice_c1 = columna_c1 + 1
                                        indice_c2 = columna_c2 + 1

                                        if indice_c1 > len(abs)-1:

                                            indice_c1 = 0
                                        
                                        elif indice_c2 > len(abs)-1:

                                            indice_c2 = 0

                                        # Obtenemos los valores con los indices
                                    
                                        c1 = self.tabla_valores[fila_c1][indice_c1]
                                        c2 = self.tabla_valores[fila_c2][indice_c2]

                                        
                                        self.mensaje_resultado = self.mensaje_resultado + c1 + c2

                                    # Caso 2 m1 y m2 tienen las misma columna
                                    elif columna_c1 == columna_c2:

                                        # posibles indices de c1 y c2
                                        indice_c1 = fila_c1 + 1
                                        indice_c2 = fila_c2 + 1


                                        if indice_c1 > len(self.tabla_valores)-1:
    
                                            indice_c1 = 0
                                        
                                        elif indice_c2 > len(self.tabla_valores)-1:

                                            indice_c2 = 0

                                        # Obtenemos los valores con los indices
                                    
                                        c1 = self.tabla_valores[indice_c1][columna_c1]
                                        c2 = self.tabla_valores[indice_c2][columna_c2]

                                        self.mensaje_resultado = self.mensaje_resultado + c1 + c2

                                    # Caso 1 m1 y m2 tienen diferente columa y fila
                                    elif columna_c1 != columna_c2 and fila_c1 != fila_c2:


                                        #  Distancia de m1
                                        if columna_c1 > 2:
                                            # Se tiene que retroceder porque ya se paso el eje de simetria
                                            if columna_c1 == 4:
                                                
                                                distancia_c1 = 0

                                            else:

                                                distancia_c1 = 1

                                            columna_c1 = distancia_c1

                                        elif columna_c1 < 2:
                                            # Se tiene que avanzar porque aun no pasa el eje de simetria

                                            if columna_c1 == 0:

                                                distancia_c1 = 4

                                            else:
                                                
                                                distancia_c1 = 3

                                            columna_c1 = distancia_c1 
                                        


                                        #  Distancia de m2
                                        if columna_c2 > 2:
                                            # Se tiene que retroceder porque ya se paso el eje de simetria
                                            if columna_c2 == 3:
                                                distancia_c2 = 1
                                            
                                            else:
                                                distancia_c2 = 0

                                            columna_c2 = distancia_c2

                                        elif columna_c2 < 2:
                                            # Se tiene que avanzar porque aun no pasa el eje de simetria
                                            if columna_c2 == 1:
                                                distancia_c2 = 3

                                            else:
                                                distancia_c2 = 4

                                            columna_c2 = distancia_c2 

                                        c1 = self.tabla_valores[fila_c1][columna_c1]
                                        c2 = self.tabla_valores[fila_c2][columna_c2]

                                        self.mensaje_resultado = self.mensaje_resultado + c1 + c2

                                        
                                        




