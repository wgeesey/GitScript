#Backup Network Device Script

import os
import sys
from netmiko import ConnectHandler
from getpass import getpass
from datetime import datetime, date
from paramiko.ssh_exception import SSHException
from netmiko.ssh_exception import AuthenticationException, NetMikoTimeoutException

sys.tracebacklimit = 0

USERNAME = input("Please enter your username: ")
PASSWORD = getpass("Please enter your password: ")

networkDevice = {'ip': '192.168.111.11', 'device_type': 'cisco_ios', 'username': USERNAME, 'password': PASSWORD}

try:
	connection = ConnectHandler(**networkDevice)	
	output = connection.send_command('show run')	
	today  = date.today().strftime("%B,%d,%Y")	
	f = open('Backupconfig_' + today + '.txt', 'x')	
	f.write(output)
	f.close()
except (NetMikoTimeoutException):
	print("Timeout error occured when attempting to connect to: " + networkDevice['ip'])
except (AuthenticationException):
	print("Authentication encountered an error while attempting to connect to: " + networkDevice['ip'])	
except (SSHException):
	print("SSH Error. Verify SSH is enabled on device: " + networkDevice['ip'])
except (EOFError):
	print("EOFError when attempting to connect to: " + networkDevice['ip'])
except Exception as e:
	print(e+ " occurred while connecting to: " + networkDevice['ip'])
	
	
print("Script Complete!")


