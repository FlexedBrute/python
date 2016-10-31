#!/usr/bin/python3.5
from base64 import b64encode, b64decode
from binascii import hexlify,unhexlify
from string import ascii_letters
import cryptopals
import os

alphabet=[car for car in ascii_letters]

def findBestKey(dico):
    bestKey=(0,(0.0,0))
    for key in dico:
        if dico[key][0]> bestKey[1][0]:
            bestKey=(key,dico[key])
    return bestKey

def findKey(dico):
    bestKey=(0,(0,(0,0)))
    for key in dico:
        if dico[key][1][0] > bestKey[1][1][0]:
            bestKey=(key,dico[key])
    return bestKey

try:
    with open('1.4.txt','rb') as file:
        dicoKeys={}
        for line in file:
            lineBestKey=cryptopals.bruteForce(line[:-1])
            dicoKeys[line]=findBestKey(lineBestKey)
        result=findKey(dicoKeys)
        print(result)
except OSError as error:
    raise error
