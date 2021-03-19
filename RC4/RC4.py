
def KSA(llave):    
    
    long_llave = len(llave)
    S = list(range(256))
    j = 0

    for i in range(256):
        j = (j + S[i] + llave[i % long_llave]) % 256
        S[i], S[j] = S[j], S[i]

    
    return S

def PRGA(S, n):
    
    i = 0
    j = 0
    key = []

    while n > 0:
        n = n -1

        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]

        k =  S[ (S[i] + S[j]) % 256]
        key.append(k)

    return key


def preparar_llave_arr(s):
    
    return [ord(c) for c in s]



key = input('¿Cual es la clave a utilizar?\n')

key = preparar_llave_arr(key) 

mensaje = input('¿Cual es el mensaje a utilizar?\n')

S = KSA(key)

salida_llave = [ PRGA(S, len(mensaje)) ]

bytes_mensaje = [ord(i) for i in mensaje]

print(salida_llave, bytes_mensaje)

print(len(salida_llave), len(bytes_mensaje))





