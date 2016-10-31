#!/usr/bin/python3.5
from base64 import b64encode, b64decode
from binascii import hexlify,unhexlify


string1='1c0111001f010100061a024b53535009181c'
string2='686974207468652062756c6c277320657965'
result=b'746865206b696420646f6e277420706c6179'

def xor(a,b):
    result=''
    assert(len(a)==len(b))
    for c in range(len(a)):
        result+=chr(a[c]^b[c])
    return result

output=hexlify(xor(unhexlify(string1),unhexlify(string2)).encode())
assert(output==result)
