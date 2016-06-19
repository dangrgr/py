#!/c/Python27/python
'''
 8.1
 A. Modify this Python module such that you add a set of tests into the module.  Use the __name__ == '__main__' technique to separate the test code from the function definition.  In your test code, verify your IP address validation function against each of the following IP addresses (False means it is an invalid IP address; True means it is a valid IP address).
 B. Execute this module--make sure all of the tests pass.
 C. Import this module into the Python interpreter shell.  Make sure the test code does not execute.  Also test that you can still correctly call the ip validation function.
'''

def validate_ip(ip_address):
	'''
	Function: validates input parameter is a valid ip_address (in range: 0.0.0.0 to 255.255.255.255).
	Note: can't start with 0
	Returns True or False
	'''
	# Guilty until proven innocent
	ValidIP = False

	# Sanitize imput to ensure input is string
	if not type(ip_address) == str:
		return 'Error: Function validate_ip(): input parameter must be a string.'

	# Extract octects from ip_address
	octets = ip_address.split('.')

	# Parse octets to validate valid IP
	if len(octets) != 4:
		ValidIP = False
	elif octets[0] == '0':
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
			elif len(octet) >=2 and int(octet[0]) == 0:
				ValidIP = False
				break
			else:
				ValidIP = True

	# Return True if IP is valid
	if ValidIP == True:
		return True
	else:
		return False

if __name__ == '__main__':

	test_ip_addresses = {
        '192.168.1' : False,
        'x.10.10.10' : False,
        '10.1.1.' : False,
        '10.1.1.x' : False,
        '0.77.22.19' : False,
        '-1.88.99.17' : False,
        '241.17.17.9' : True,
        '127.0.0.1' : True,
        '169.254.1.9' : True,
        '192.256.7.7' : False,
        '192.168.-1.7' : False,
        '10.1.1.256' : False,
        '1.1.1.1' : True,
        '223.255.255.255': True,
        '223.0.0.0' : True,
        '10.200.255.1' : True,
        '192.168.17.1' : True,
    }

	for ip_addr in test_ip_addresses:
		test_case = test_ip_addresses[ip_addr]
		result = validate_ip(ip_addr)
		if result == test_case:
			print "%s: Pass" % ip_addr
		else:
			print "%s: Fail" % ip_addr
