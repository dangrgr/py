#!/home/dgrindall/applied_python/bin/python
import sys, re
import pexpect
from getpass import getpass


def main():
    ip_addr = '184.105.247.71'
    username = 'pyclass'
    port = 22
    password = getpass()
    
    ssh_conn = pexpect.spawn('ssh -l {} {} -p {}'.format(username, ip_addr, port))
    #ssh_conn.logfile=sys.stdout
    ssh_conn.timeout = 3
    
    ssh_conn.expect('ssword:')
    ssh_conn.sendline(password)
    
    ssh_conn.expect('#')

    ssh_conn.sendline('show ip int brief')
    ssh_conn.expect('#')

    ssh_conn.sendline('terminal length 0')
    ssh_conn.expect('#')
    
    ssh_conn.sendline('show version')
    ssh_conn.expect('pynet-rtr2#')

    #Example of cathing and handling a timeout
    #try:
    #    ssh_conn.sendline('show version')
    #    ssh_conn.expect('zzzz')
    #except pexpect.TIMEOUT:
    #    print "found timeout"

    pattern = re.compile(r'^Lic.*DI:.*$', re.MULTILINE)
    ssh_conn.sendline('show version')
    ssh_conn.expect(pattern)
    print ssh_conn.after

if __name__ == "__main__":
    main()