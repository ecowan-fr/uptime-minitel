#Programme permettant de lancer un programme en plein écran sur le minitel

import os
import sys
import time
import random
import logging
from pyzabbix import ZabbixAPI
import serial
import pynitel
user = 0

minitel = serial.Serial("COM3", 1200, parity=serial.PARITY_EVEN, stopbits=serial.STOPBITS_TWO, timeout=1, bytesize=7)
minitel.write(b'\r') #Reviens au début de la ligne
minitel.write(b'\x1b[2J') #Efface l'écran
logo = open("ecowan.txt", "tr")
lines = logo.readlines()
for line in lines:
    minitel.write(line.encode())
    minitel.write(b'\r')
    time.sleep(0.1)
logo.close()
minitel.write(b'\n')
minitel.write(b'\n')
minitel.write(b'\n')
minitel.write(b'\n')
accueil = open("accueil.txt", "tr")
lines = accueil.readlines()
for line in lines:
    minitel.write(line.encode())
    minitel.write(b'\r')
    time.sleep(0.1)
logo.close()
minitel.write(b'\n')

while user == 0 or user == b'':
    user = minitel.read(1)
if user == b'8':
    minitel.write(b'\x1b[2J') #Efface l'écran
    close = open("close.txt", "tr")
    lines = close.readlines()
    minitel.write(b'\r')
    minitel.write(b'\n')
    for line in lines:
        minitel.write(line.encode())
        minitel.write(b'\r')
        time.sleep(0.1)
    exit()

if user == b'1':
    minitel.write(b'\x1b[2J') #Efface l'écran
    minitel.write(b'\r') #Reviens au début de la ligne
    minitel.write(b'\n')
    minitel.write(b'Affichage des serveurs')
    minitel.write(b'\r')
    minitel.write(b'\n')
    minitel.write(b'Veuillez patienter...')
    minitel.write(b'\r')
    minitel.write(b'\n')
    time.sleep(1)
    minitel.write(b'\x1b[2J') #Efface l'écran
    minitel.write(b'\r') #Reviens au début de la ligne
    minitel.write(b'\n')
    minitel.write(b'Affichage des serveurs')
    minitel.write(b'\r')
    minitel.write(b'\n')
    minitel.write(b'Veuillez patienter...')
    minitel.write(b'\r')
    minitel.write(b'\n')
    time.sleep(1)
    minitel.write(b'\x1b[2J') #Efface l'écran
    minitel.write(b'\r') #Reviens au début de la ligne
    minitel.write(b'\n')
    minitel.write(b'Affichage des serveurs')
    minitel.write(b'\r')
    minitel.write(b'\n')
    minitel.write(b'Veuillez patienter...')
    minitel.write(b'\r')
    minitel.write(b'\n')
    time.sleep(1)
    minitel.write(b'\x1b[2J') #Efface l'écran
    minitel.write(b'\r') #Reviens au début de la ligne
    minitel.write(b'\n')
    minitel.write(b'Affichage des serveurs')
    minitel.write(b'\r')
    minitel.write(b'\n')
    minitel.write(b'Veuillez patienter...')
    minitel.write(b'\r')
    minitel.write(b'\n')
    time.sleep(1)
    minitel.write(b'\x1b[2J') #Efface l'écran
    minitel.write(b'\r') #Reviens au début de la ligne
    minitel.write(b'\n')
    minitel.write(b'Affichage des serveurs')
    minitel.write(b'\r')
    while user == 0 or user == b'':
        user = minitel.read(1)

    