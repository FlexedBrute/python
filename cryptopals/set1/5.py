#!/usr/bin/python3.5
from base64 import b64encode, b64decode
from binascii import hexlify,unhexlify
from string import ascii_letters
import cryptopals
import os

string1="""Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal"""
key='ICE'
xor1='0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f'


def genKeyString(key,length):
    keyString=''
    for i in range(length):
        keyString+=key[i%len(key)]
    return keyString

keyString=genKeyString(key,len(string1.encode()))
result=cryptopals.xor(string1.encode(),keyString.encode()).encode()
assert(hexlify(result)==xor1.encode())
