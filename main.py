import math
import sys
import time
import random
import logging
from pyzabbix import ZabbixAPI


# Zabbix API connection
zapi = ZabbixAPI("http://mon.ecowan.network")
zapi.login("zabbix user", "zabbix pass")
print("Connecté au serveur Zabbix d'ECOWAN. Version %s" % zapi.api_version())