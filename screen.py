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
minitel.write(b'\n') #Saute une ligne
minitel.write(b'\r') #Reviens au début de la ligne

