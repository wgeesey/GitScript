#Backup Network Device Script

import os
from netmiko import ConnectHandler
from getpass import getpass
from datetime import datetime, date

USERNAME = input("Please enter your username: ")
PASSWORD = getpass("Please enter your password: ")

networkDevice = {'ip': '192.168.111.11', 'device_type': 'cisco_ios', 'username': USERNAME, 'password': PASSWORD}

connection = ConnectHandler(**networkDevice)

output = connection.send_command('show run')

today  = date.today().strftime("%B,%d,%Y")
f = open('Backupconfig_' + today + '.txt', 'x')

f.write(output)

f.close()



