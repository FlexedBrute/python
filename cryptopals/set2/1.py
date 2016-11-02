#!/usr/bin/python3.5

string='Yellow SUBMARINE'

def genPadding(string,length):
    for i in range(length-len(string)):
        string+='\x04'
    return string
