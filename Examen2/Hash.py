import hashlib
BLOCK_SIZE = 65536


def SHA1(data):

    hash = hashlib.sha1()
    hash.update(data.encode('utf-8'))
    res = hash.hexdigest()

    return res


def SHA1_file(data):
    file_hash = hashlib.sha1()

    with open(data, 'rb') as f:
            
        fb = f.read(BLOCK_SIZE)

        while len(fb) > 0:

            file_hash.update(fb)
            fb = f.read(BLOCK_SIZE)

    return file_hash.hexdigest()
        

def SHA256(data):
    
    hash = hashlib.sha256()
    hash.update(data.encode('utf-8'))
    res = hash.hexdigest()

    return res

def SHA256_file(data):
    file_hash = hashlib.sha256()

    with open(data, 'rb') as f:
            
        fb = f.read(BLOCK_SIZE)

        while len(fb) > 0:

            file_hash.update(fb)
            fb = f.read(BLOCK_SIZE)

    return file_hash.hexdigest()

def SHA512(data):
    hash = hashlib.sha512()
    hash.update(data.encode('utf-8'))
    res = hash.hexdigest()

    return res

def SHA512_file(data):
    file_hash = hashlib.sha512()

    with open(data, 'rb') as f:
            
        fb = f.read(BLOCK_SIZE)

        while len(fb) > 0:

            file_hash.update(fb)
            fb = f.read(BLOCK_SIZE)

    return file_hash.hexdigest()

def MD5(data):
    hash = hashlib.md5()
    hash.update(data.encode('utf-8'))
    res = hash.hexdigest()

    return res

def MD5_file(data):
    file_hash = hashlib.md5()

    with open(data, 'rb') as f:
            
        fb = f.read(BLOCK_SIZE)

        while len(fb) > 0:

            file_hash.update(fb)
            fb = f.read(BLOCK_SIZE)

    return file_hash.hexdigest()


def menu():

    opcion = int(input('Que es lo que deseas encriptar\n 1)Mensaje de texto\n 2)Archivo\n'))

    metodo_opcion = int(input('¿Que metodo quieres usar para encriptar?\n1) SHA1\n2) SHA256\n3) SHA512\n4) MD5\n')) 

    if(opcion == 1):

        texto = input('¿Cual es tu mensaje?\n')
        

        if metodo_opcion == 1:
            hash = SHA1(texto)
            print(hash)

        elif metodo_opcion == 2:
            hash = SHA256(texto)
            print(hash)

        elif metodo_opcion == 3:
            hash = SHA512(texto)
            print(hash)

        elif metodo_opcion == 4:
            hash = MD5(texto)
            print(hash)

        else:
            print('Opcion no valida')
        
    if(opcion == 2):

        ruta = input('Cual es la ruta del archivo?\n')
        
        if metodo_opcion == 1:
            hash_file = SHA1_file(ruta)
            print(hash_file)

        elif metodo_opcion == 2:
            hash_file = SHA256_file(ruta)
            print(hash_file)

        elif metodo_opcion == 3:
            hash_file = SHA512_file(ruta)
            print(hash_file)

        elif metodo_opcion == 4:
            hash_file = MD5_file(ruta)
            print(hash_file)

        else:
            print('Opcion no valida')

menu()