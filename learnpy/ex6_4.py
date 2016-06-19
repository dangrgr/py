#!/c/Python27/python
'''
4. Create a function using your dotted decimal to binary conversion code from Class3, exercise1. In the function--do not prompt for input and do not print to standard output. The function should take one variable 'ip_address' and should return the IP address in dotted binary format always padded to eight binary digits (for example, 00001010.01011000.00010001.00010111). You might want to create other functions as well (for example, the zero-padding to eight binary digits).
'''

from iptools import validate_ip
from iptools import zero_pad_bin

'''Function: convert decimal ip address to binary'''
def dec_to_bin(ip_address):
	
	# Sanitize Input with validate_ip function
	if validate_ip(ip_address) == True:

		# Extract octects from ip_address
		ip_octets = ip_address.split('.')

		# Convert each octet into binary
		bin_octets = []
		for i,ip_octet in enumerate (ip_octets):
			bin_octet = (bin(int(ip_octet))).split('b').pop()

			# Zero pad each octet (function written in this excersise)
			bin_octet = zero_pad_bin(bin_octet)

			bin_octets.append(bin_octet)

		# Build string of binary octets
		bin_addr = ".".join(bin_octets)

		return bin_addr

	else:
		print 'Error: Function dec_to_bin() detected an invalid IP (input).'
		quit()



a = dec_to_bin('192.168.1.1')
print a