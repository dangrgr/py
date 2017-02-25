#!/home/dgrindall/applied_python/bin/python
#
# Use Paramiko to retrieve the entire 'show version' output from pynet-rtr2. 

import paramiko
from getpass import getpass


def main():
    # Set connection variables 
    ip_addr = '184.105.247.71'
    port = 22
    username = 'pyclass'
    password = getpass()

    # Initialize SSH client and establish SSH connection
    remote_conn_pre=paramiko.SSHClient()
    remote_conn_pre.load_system_host_keys()
    remote_conn_pre.connect(ip_addr, username=username, password=password, look_for_keys=False, allow_agent=False, port=port)
    
    # Startup channel
    remote_conn = remote_conn_pre.invoke_shell()

    # Commands:
    outp = remote_conn.send("terminal length 0\nshow run\n")
    outp = remote_conn.recv(2000)
    print outp

if __name__ == "__main__":
    main()
