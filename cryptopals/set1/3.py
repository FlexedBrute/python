#!/usr/bin/python3.5
from base64 import b64encode, b64decode
from binascii import hexlify,unhexlify
from string import ascii_letters
import operator
#
#
input='1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
alphabet=[car for car in ascii_letters]
alphaFreq=[car for car in 'EeTtAaOoIiNn SsHhRrDdLlUu']
anwser="Cooking MC's like a pound of bacon"

def xor(a,b):
    result=''
    assert(len(a)==len(b))
    for c in range(len(a)):
        result+=chr(a[c]^b[c])
    return result

def searchLetterFreq(a,c):
    count=0
    for e in range(len(a)):
        if a[e]==c:
            count+=1
    return count

def searchFreq(a,dico):
    dist={}
    for e in dico:
        dist[e]=searchLetterFreq(a,e)
    for k in dist:
        dist[k]=round(dist[k]/len(a)*100,3)
    listFreq=list(dist.items())
    listFreq.sort(key=operator.itemgetter(1),reverse=True)
    return listFreq

def bruteForce(string):
    result={}
    for c in alphabet:
        cString=c.encode()*len(unhexlify(string))
        output=xor(unhexlify(string),cString)
        total=0
        for el in searchFreq(output,alphaFreq):
            total+=el[1]
        result[c]=[total,output]
    return result

result=bruteForce(input)
assert(result['X'][1]==anwser)
