#!/usr/bin/env python
#-*-coding:UTF-8-*-
import socket,sys

taille=5
host=sys.argv[1]
port=int(sys.argv[2])
id=sys.argv[3]
passwd=sys.argv[4]

def read():
    data=client.recv(taille)
    return data

#Création du serveur sur le port donnée en argument

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind((host,port))
s.listen(5)
print "Serveur démarré sur le port :",port
client,adresse=s.accept()
print "une connexion s'est effectuee depuis ",
print client.getpeername()

#demande de l'identifiant et du mot de passe
while 1:
    client.send("Votre identifiant:  ")
    identifiant=read()
    client.send("Votre Mot de passe: ")
    password=read()
    if identifiant == id:
        if password == passwd:
            client.send("connexion réussi !!!")
            print "L'utilisateur ",identifiant+" vient de se connecter"
            print "fin du serveur"
            client.close()
            s.close()
        else:
            print "Tentative de connexion de ",identifiant+" avec le mot de passe :",password
            client.send("Erreur !!!!!!!!!!!!!")
