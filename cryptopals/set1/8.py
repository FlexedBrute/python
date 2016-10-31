#!/usr/bin/python3.5
#-*-coding:UTF-8-*-
from base64 import b64encode, b64decode
from binascii import hexlify,unhexlify
from Crypto.Cipher import AES
from Crypto import Random
import re
import cryptopals

def detectRep(string):
    result=False
    for i in range(0,int (len(string)/16)):
        pattern=string[i*16:(i+1)*16]
        test=re.findall(pattern,string)
        if len(test)>1:
            result=True
    return result
    
try:
    with open('8.txt','rb') as file:
        string=b''
        nbLine=1
        for line in file:
            line=line[:-1]
            if detectRep(line):
                print(nbLine,line)
            nbLine+=1
except Exception as e:
    raise
