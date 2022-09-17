<<<<<<< HEAD
#Programme permettant de lancer un programme en plein écran sur le minitel

import os
=======
>>>>>>> d00fab818950fed315e3aa5c4ac9665b66e9db2f
import sys
import time
import random
import logging
<<<<<<< HEAD
from pyzabbix import ZabbixAPI
import serial
import pynitel


minitel = serial.Serial("COM3", 1200, parity=serial.PARITY_EVEN, stopbits=serial.STOPBITS_TWO, timeout=1, bytesize=7)
minitel.write(b'\n') #Saute une ligne
minitel.write(b'\r') #Reviens au début de la ligne

=======

#Initialisation liaison série USB --> Minitel
>>>>>>> d00fab818950fed315e3aa5c4ac9665b66e9db2f
