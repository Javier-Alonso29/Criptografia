class cesar:

    def __init__(self, mensaje, numero_recorrido):
        self.mensaje = mensaje.lower()
        self.mensaje_res = ''
        self.numero_recorrido = numero_recorrido
        self.lista_letras_normal ='abcdefghijklmnñopqrstuvwxyz'

        self.encriptar()

    def encriptar(self):

        for i in self.mensaje:

            if(i in self.lista_letras_normal):

                pasada_posicion = self.lista_letras_normal.index(i)

                nueva_posicion = (pasada_posicion + self.numero_recorrido) % len(self.lista_letras_normal)

                self.mensaje_res  += self.lista_letras_normal[nueva_posicion]
            else:

                self.mensaje_res += i
        

