import subprocess
from collections import defaultdict
import re
import sys

def database():
    database=defaultdict(list)

    ifconfig = subprocess.Popen('ifconfig',stdout=subprocess.PIPE,shell=True)
    ifcfg_out= ifconfig.stdout.read().decode()
    ifcfg= ifcfg_out.split("\n\n")
    ifcfg=list(filter(None,ifcfg))
    exint=["lo"]
    #Loop to remove keep only actual interfaces
    intcfg2=[]
    for j in range (0,len(ifcfg)):
        result = re.compile('^enp[0-9]s[0-9]').search(ifcfg[j])
        if result:
            intcfg2.append(ifcfg[j])
    ifcfg=intcfg2
    #loop to create a list of interface names
    intlist = []
    for j in range (0,len(ifcfg)):
        intlist.append(re.compile('^enp[0-9]s[0-9]').search(ifcfg[j]).group(0))

    #makes the database
    for interface in intlist:
        ipaddr, mask, macadd=ip_mask(ifcfg,interface)
        gatewy = gateway()
        database[interface].append(ipaddr)
        database[interface].append(mask)
        database[interface].append(macadd)
        database[interface].append(gatewy)
    #print database.items()
    return database
    #Stored in the order: IP address, Netmask, MAC, Gateway

#extracts ip and mask from list b
def ip_mask(ifcfg,interface):
    for i in range (0,len(ifcfg)):
        if re.compile('^enp[0-9]s[0-9]').search(ifcfg[i]).group(0) ==interface:
            ip = re.compile('inet [0-9]*.[0-9]*.[0-9]*.[0-9]*').search(ifcfg[i])
            if ip:
                ip= ip.group(0).split(' ')[1]
            mask = re.compile('netmask [0-9]*.[0-9]*.[0-9]*.[0-9]*').search(ifcfg[i])
            if mask:
                mask= mask.group(0).split(' ')[1]
            mac = re.compile('ether ([0-9a-f]{2}[:-]){5}([0-9a-f]{2})').search(ifcfg[i])
            if mac:
                mac= mac.group(0).split(' ')[1]
    return ip, mac, mask

#extracts gateway from routing table
def gateway():
    gateway = subprocess.Popen('route -n | grep "^0.0.0.0" | tr -s " " | cut -f2 -d" "',stdout=subprocess.PIPE,shell=True).stdout.read().decode().strip("\n")
    return gateway

#db=database()
#print(db)

#print(db.keys())
#for key in db.keys():
#	print(key)
#	print(db[key])
