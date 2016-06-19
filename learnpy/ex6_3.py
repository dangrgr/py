#!/c/Python27/python
'''
3a.Convert the IP address validation code (Class4, exercise1) into a function,
take one variable 'ip_address' and return either True or False
(depending on whether 'ip_address' is a valid IP). Only include IP address
checking in the function--no prompting for input, no printing to standard output.
'''

def func_validate_ip_addr(ip_address):

	# Guilty until proven innocent!
	ValidIP = False

	# Sanitize imput
	if not type(ip_address) == str:
		return "Input must be a string."
		exit()

	# Parse octets from imput string
	octets = ip_address.split('.')

	# Validate IP address is valid
	if len(octets) != 4:
		ValidIP = False
	else:
		for i,octet in enumerate(octets):
			try:
				int(octet)
			except ValueError:
				ValidIP = False
				break
			if not 0 <= int(octet) <= 255:
				ValidIP = False
				break
			else:
				ValidIP = True

	# Return True if IP is valid
	if ValidIP == True:
		return True
	else:
		return False


a = func_validate_ip_addr('255.255.255.0')
print a