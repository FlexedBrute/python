#!/usr/bin/python3.5
from base64 import b64encode, b64decode
from binascii import hexlify,unhexlify
from string import ascii_letters,ascii_lowercase,printable
from Crypto.Cipher import AES
from Crypto import Random
import operator
import re

alphabet=[car for car in printable]
alphaFreq=[car for car in 'EeTtAaOoIiNn SsHhRrDdLlUu']
BLOCK_SIZE=16

def xor(a,b):
    assert(len(a)==len(b))
    result=bytearray()
    for c in range(len(a)):
        result.append(a[c]^b[c])
    return bytes(result)


def searchLetterFreq(a,c):
    assert(len(a)!=0)
    count=0
    for e in range(len(a)):
        if a[e]==c:
            count+=1
    return count

def searchFreq(a,dico):
    assert(len(a)!=0)
    dist={}
    for e in dico:
        dist[e]=searchLetterFreq(a,e)
    for k in dist:
        dist[k]=dist[k]/len(a)*100
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
        result[c]=(total,output)
    return result

def findBestKey(dico):
    bestKey=(0,(0.0,0))
    for key in dico:
        if dico[key][0]> bestKey[1][0]:
            bestKey=(key,dico[key])
    return bestKey


def string2Hex(string):
    return(hexlify(string.encode()))

def genKeyString(key,length):
    keyString=''
    for i in range(length):
        keyString+=key[i%len(key)]
    return keyString

def hammingDistance(s1,s2):
    assert(s1!=s2)
    assert(len(s1)==len(s2))
    s1=bytearray(s1.encode())
    s2=bytearray(s2.encode())
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
        value=hammingDistance(block1,block2)/keySize
        if KeySizeList[len(KeySizeList)-1][1]> value:
            KeySizeList.append((keySize,value))
        KeySizeList.sort(key=operator.itemgetter(1))
    KeySizeList= [KeySizeList[i] for i in range(0,4)]
    return KeySizeList

def decrypt( string,key,mode):
    decryptor=AES.new(key,mode)
    return decryptor.decrypt(string)


def detectRep(string):
    result=False
    for i in range(0,int (len(string)/16)):
        pattern=string[i*16:(i+1)*16]
        test=re.findall(pattern,string)
        if len(test)>1:
            result=True
    return result

def genPadding(string,length):
    if type(string)==str:
        string=string.encode()
    for i in range(length-len(string)):
        string+=b'\x04'
    return string

if __name__ == '__main__':
    #XOR test
    string1='1c0111001f010100061a024b53535009181c'
    string2='686974207468652062756c6c277320657965'
    result=b'746865206b696420646f6e277420706c6179'
    output=hexlify(xor(unhexlify(string1),unhexlify(string2)))
    assert(output==result)

    #Féquence test
    string="Il n'acheva point. Une seconde balle du meme tireur l'arreta court. Cette fois il s'abattit la face contre le pave, et ne remua plus. Cette petite grande ame venait de s'envoler."
    aCount=14
    eCount=28
    assert(searchLetterFreq(string,'e')==eCount)
    assert(searchLetterFreq(string,'a')==aCount)


    #bruforce test
    input='1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
    anwser="Cooking MC's like a pound of bacon"
    result=bruteForce(input)
    assert(result['X'][1]==anwser.encode())


    #Hamming Distance test
    string1='this is a test'
    string2='wokka wokka!!!'
    result=37
    assert (hammingDistance(string1,string2)==result)

    # genPadding test
    string='YELLOW SUBMARINE'
    result=b'YELLOW SUBMARINE\x04\x04\x04\x04'
    length=20
    assert(genPadding(string,length)==result)
