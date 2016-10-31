#!/usr/bin/python3.5
from base64 import b64encode, b64decode
from binascii import hexlify,unhexlify
from string import printable
import operator
import itertools
import cryptopals
import os
import re

alphabet=[car for car in printable]
string1='this is a test'
string2='wokka wokka!!!'

def hammingDistance(s1,s2):
    assert(len(s1)==len(s2))
    s1=bytearray(s1)
    s2=bytearray(s2)
    count=0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            count+=bin(s1[i]^s2[i]).count("1")
    return count

def genKeySizeList(min,max):
    KeySizeList=[(0,90)]
    for keySize in range(min,max):
        block1=string[:keySize]
        block2=string[keySize:keySize*2]
        block3=string[keySize*2:keySize*3]
        block4=string[keySize*3:keySize*4]
        value=hammingDistance(block1,block2)
        value+=hammingDistance(block1,block3)
        value+=hammingDistance(block1,block4)
        value+=hammingDistance(block2,block3)
        value+=hammingDistance(block2,block4)
        value+=hammingDistance(block3,block4)
        value=value/keySize
        if KeySizeList[len(KeySizeList)-1][1]> value:
            KeySizeList.append((keySize,value))
        KeySizeList.sort(key=operator.itemgetter(1))
    KeySizeList= [KeySizeList[i] for i in range(0,4)]
    return KeySizeList

def genDico(size):
    for i in range(1,size+1):
        dico=itertools.product(alphabet,repeat=i)
    return dico

def genByteBlock(blocks,value):
    byteString=b''
    for block in blocks:
        byteString+=block[value:value+1]
    return byteString

def genBlock(string,keysize):
    blocks=[]
    for i in range(int(len(string)/keySize[0])):
        blocks.append(string[keySize[0]*i:keySize[0]*(i+1)])
    return blocks
try:
    with open('6.txt','rb') as file:
        string=b''
        for line in file:
            string+=line[:-1]
        string=b64decode(string)
        keySizeList=genKeySizeList(2,40)
        for keySize in keySizeList:
            bestKey=[]
            key=''
            allBlocks=genBlock(string,keySize)
            for i in range(0,keySize[0]):
                bytesString=genByteBlock(allBlocks,i)
                result=cryptopals.bruteForce(hexlify(bytesString))
                bestKey=cryptopals.findBestKey(result)
                key+=bestKey[0][0]
            keyString=cryptopals.genKeyString(key,len(string))
            print('la clé est =>{}'.format(key))
            print(cryptopals.xor(string,keyString.encode()))
except OSError as error:
    raise error
