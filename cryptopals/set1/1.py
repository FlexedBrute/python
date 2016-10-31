#!/usr/bin/python3.5
from base64 import b64encode, b64decode
from binascii import hexlify,unhexlify

input=b'49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
result=b'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'

output=b64encode(unhexlify(input))
assert(output==result)
