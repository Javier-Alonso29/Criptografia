
def cadena_binario(texto):

    matriz_bloques = []
    bytes = ''
    count = 0

    for i in texto:
        bytes += format(ord(i), '08b')
        count += 1 

        if len(bytes) == 128:
            matriz_bloques.append(bytes)
            bytes = ''
            continue

        if count == len(texto):
            matriz_bloques.append(bytes)

    ultimo_bloque = matriz_bloques[-1]
    
    if(len(ultimo_bloque) < 128):

        pading = ultimo_bloque.ljust(128, '0')
        matriz_bloques[-1] = pading

    return matriz_bloques

def hash(matriz):

    bytes = ''
    for x in range(0,128):
		
        bloq = matriz[0]
        xor=int(bloq[x])
		
        for y in range(1,len(matriz)):
                
            bloq = matriz[y]
                
            xor = xor^int(bloq[x])
        bytes+=str(xor)
        
    return (hex(int(bytes,2)))
    

cadena = input('¿Cual es el mensaje?\n')
matriz = cadena_binario(cadena)
resultado_hash = hash(matriz)

print(resultado_hash)


