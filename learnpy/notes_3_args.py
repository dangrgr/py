#!/c/Python27/python
import sys

if len(sys.argv) == 2:
    ip_addr = sys.argv.pop()
    print "The IP address is : %s" % ip_addr
else:
    print "You made an error."
