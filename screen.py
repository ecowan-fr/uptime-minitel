#Programme permettant de lancer un programme en plein écran sur le minitel

import os
import sys
import time
import random
import logging
from pyzabbix import ZabbixAPI
import serial
import pynitel


minitel = serial.Serial("COM3", 1200, parity=serial.PARITY_EVEN, stopbits=serial.STOPBITS_TWO, timeout=1, bytesize=7)
minitel.write(b'\r') #Reviens au début de la ligne
minitel.write(b'\x1b[2J') #Efface l'écran
logo = open("ecowan.txt", "tr")
lines = logo.readlines()
for line in lines:
    minitel.write(line.encode())
    minitel.write(b'\r')
    time.sleep(0.1)

