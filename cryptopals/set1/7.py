#!/usr/bin/python3.5
#-*-coding:UTF-8-*-
from base64 import b64encode, b64decode
from binascii import hexlify,unhexlify
from Crypto.Cipher import AES
from Crypto import Random

key=b'YELLOW SUBMARINE'
BLOCK_SIZE=16

def decrypt( string,key,mode):
    IV = Random.new().read(BLOCK_SIZE)
    decryptor=AES.new(key,mode,IV)
    return decryptor.decrypt(string)

try:
    with open('7.txt','rb') as file:
        string=b''
        for lines in file:
            string+=b64decode(lines)
        decrypted=decrypt(string,key,AES.MODE_ECB)
        print(decrypted.decode())
except Exception as e:
    raise
