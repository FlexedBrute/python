#!/usr/bin/python3.5
#-*-coding:UTF-8-*-

from base64 import b64encode, b64decode
from binascii import hexlify,unhexlify
from Crypto.Cipher import AES
from Crypto import Random
from cryptopals import *

BLOCK_SIZE=16
string=b"Il n'acheva point. Une seconde balle du meme tireur l'arreta court. Cette fois il s'abattit la face contre le pave, et ne remua plus. Cette petite grande ame venait de s'envoler."
key=b'YELLOW SUBMARINE'

def encrypt(string,key,mode):
    encryptor=AES.new(key,mode)
    return encryptor.encrypt(string)

def decrypt(string,key,mod):
    decryptor=AES.new(key)
    return decryptor.decrypt(string)

def encryptCBC(string,key,IV):
    encryptedString=b''
    for i in range(int(len(string)/16)+1):
        block=string[i*16:(i+1)*16]
        if i<0:
            IV=blockEncrypted
        if len(block)< 16:
            block=genPadding(block,16)
        blockXor=xor(block,IV)
        blockEncrypted=encrypt(blockXor,key,AES.MODE_ECB)
        encryptedString+=blockEncrypted
    return encryptedString


def decryptCBC(string,key,IV):
    decryptedString=b''
    for i in range(int(len(string)/16)):
        block=string[i*16:(i+1)*16]
        if i<0:
            IV=lastBlock
        if len(block)<16:
            block=genPadding(block,16)
        blockDecrypted=decrypt(block,key,AES.MODE_ECB)
        blockXor=xor(blockDecrypted,IV)
        decryptedString+=blockXor
        lastBlock=block
    return decryptedString

IV=b'\x00'*BLOCK_SIZE
print(string)
print(decryptCBC(encryptCBC(string,key,IV),key,IV))
