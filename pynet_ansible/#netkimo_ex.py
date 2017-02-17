#netkimo_ex.py

from netmiko import ConnectHandler
from getpass import getpass
password = getpass()

pynet1 = { 
    'device_type': 'cisco_ios',
    'ip': '184.105.247.70',
    'username': 'pyclass',
    'password': password,
    }   

pynet2 = { 
    'device_type': 'cisco_ios', 
    'ip': '184.105.247.71',
    'username': 'pyclass',
    'password': password,
    'port': 22, 
    }   

pynet_sw3 = { 
    'device_type': 'arista_eos',    
    'ip': '184.105.247.74',
    'username': 'admin1',
    'password': password,
    }   

pynet_rtr1 = ConnectHandler(**pynet1)    
pynet_rtr2 = ConnectHandler(**pynet2) 
srx = ConnectHandler(**pynet_srx1)