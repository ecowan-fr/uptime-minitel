import math
import sys
import time
import random
import logging
from pyzabbix import ZabbixAPI


# Zabbix API connection
zapi = ZabbixAPI("https://mon.ecowan.network")
zapi.login("api-minitel", "connard68")
print("Connecté au serveur Zabbix d'ECOWAN. Version %s" % zapi.api_version())

# Get all hosts
hosts = zapi.host.get(output="extend")
for h in hosts:
    print("Host: %s" % h["host"])

