#!/c/Python27/python
'''
Assignement 5:
Create a script that checks the validity of an IP address.  The IP address should be supplied on the command line.
[X]  A. Check that the IP address contains 4 octets.
[X]  B. The first octet must be between 1 - 223.
[X]  C. The first octet cannot be 127.
[X]  D. The IP address cannot be in the 169.254.X.X address space.
[X]  E. The last three octets must range between 0 - 255.

For output, print the IP and whether it is valid or not.
'''
import sys

#Parse input
script_name = sys.argv[0].split('\\')[-1]
usage = '\nUsage: %s <IP address>\n' % script_name
if len(sys.argv) == 2:
	ip_addr = sys.argv[1]
else:
	sys.exit(usage)

octets = ip_addr.split('.')
first_octet = int(octets[0])
second_octet = int(octets[1])

#Validate valid IP address
for i,octet in enumerate(octets):
	try:
		int(octet)
	except:
		sys.exit('\nError: Invalid IP Address: %s\n' % ip_addr)
	if octet == '':
		sys.exit('\nError: Invalid IP Address: %s\n' % ip_addr)
	elif not 0 <= int(octet) <= 255:
		sys.exit('\nError: Invalid IP Address: %s\n' % ip_addr)
if i != 3:
	sys.exit('\nError: Invalid IP Address: %s\n' % ip_addr)

#Validate IP address forbidden range conditions
elif not 1 <= first_octet <= 223 or first_octet == 127:
	sys.exit('\nError: First octet must be between 1 - 223, and cannot be 127.\n')
elif first_octet == 169 and second_octet == 254:
	sys.exit('\nError: IP cannot be in 169.254.X.X address space.\n')

print '\nGood! You entered: %s\n' % ip_addr