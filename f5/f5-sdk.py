# f5-sdk playground
from getpass import getpass
from f5.bigip import ManagementRoot

username = "admin"
password = getpass()

# Connect to the BIG-IP
mgmt = ManagementRoot("192.168.56.32", username, password)

# Get syslog config
syslog = mgmt.tm.sys.syslog.load()
print(syslog.raw)
