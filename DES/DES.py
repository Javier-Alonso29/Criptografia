#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 23:25:57 2021

@author: antonio
"""

from Crypto.Cipher import DES


def pad(text):
    n = len(text) % 8
    return text + (' ' * (8-n))


plaintext = input("Texto a cifrar: ")
padded_text = pad(plaintext)


key = input("Llave (8 caracteres): ")

cipher = DES.new(key)
cifrado = cipher.encrypt(padded_text)
print("Mensaje cifrado: ",cifrado)

cipher = DES.new(key)
descifrado = cipher.decrypt(cifrado)
print("Mensaje descifrado: ",descifrado)




