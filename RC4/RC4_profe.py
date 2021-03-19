#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 23:25:57 2021

@author: antonio
"""

from Crypto.Cipher import ARC4

plaintext = "Este es el  mensaje a cifrar con RC4"
key = 'Esta es la llave'

cipher = ARC4.new(key)
cifrado = cipher.encrypt(plaintext)
print("Mensaje cifrado: ",cifrado)

cipher = ARC4.new(key)
descifrado = cipher.decrypt(cifrado).decode()
print("Mensaje descifrado: ",descifrado)




