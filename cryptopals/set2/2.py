#!/usr/bin/python3.5
#-*-coding:UTF-8-*-

from base64 import b64encode, b64decode
from binascii import hexlify,unhexlify
from Crypto.Cipher import AES
from Crypto import Random
from cryptopals import *

BLOCK_SIZE=16
string="Il n'acheva point. Une seconde balle du meme tireur l'arreta court. Cette fois il s'abattit la face contre le pave, et ne remua plus. Cette petite grande ame venait de s'envoler."
key=b'YELLOW SUBMARINE'

def encrypt(string,key,mode):
    encryptor=AES.new(key,mode)
    print(len(string),len(key))
    return encryptor.encrypt(string)

def decrypt(string,key,mod):
    decryptor=AES.new(key)
    return decryptor.decrypt(string)

encryptedString=b''
for i in range(int(len(string)/16)):
    block=string[i*16:(i+1)*16]
    if i==0:
        IV=b'\x00'*BLOCK_SIZE
    else:
        IV=blockEncrypted
    blockXor=xor(block.encode(),IV)
    blockEncrypted=encrypt(blockXor,key,AES.MODE_ECB)
    # print(block, IV, blockEncrypted)
    encryptedString+=blockEncrypted
print(encryptedString)
