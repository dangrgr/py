#!/c/Python27/python
'''
Module: iptools
A libray of ip related tools to help with common tasks in network automation
--Dan G
'''

def validate_ip(ip_address):
	'''
	Function: validates input parameter is a valid ip_address (in range: 0.0.0.0 to 255.255.255.255).
	Returns True or False
	'''
	# Guilty until proven innocent!
	ValidIP = False

	# Sanitize imput to ensure input is string
	if not type(ip_address) == str:
		return 'Error: Function validate_ip(): input parameter must be a string.'

	# Extract octects from ip_address
	octets = ip_address.split('.')

	# Parse octets to validate valid IP
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



def zero_pad_bin(bin_num):
	'''
	Function: zero pad an inputed binary number to 8 dgits
	i.e. 101 > 00000101
	'''
	# Sanitize input to ensure input parameter is a number
	try:
		int(bin_num)
		bin_num = str(bin_num)
	except:
		return 'Error: iptools.zero_pad_bin: input parameter must be a number (string or integer).'

	# Loop until bin_num is zero padded
	while len(bin_num) < 8:
		bin_num = '0' + bin_num

	return bin_num



def dec_to_bin(ip_address):
	'''
	Function: convert a decimal ip address to binary form
	'''
	# Sanitize input with validate_ip function (iptools)
	if validate_ip(ip_address) == True:

		# Extract octects from ip_address
		ip_octets = ip_address.split('.')

		# Convert each octet into binary
		bin_octets = []
		for i,ip_octet in enumerate (ip_octets):
			bin_octet = (bin(int(ip_octet))).split('b').pop()

			# Zero pad each octet with zero_pad_bin function (iptools)
			bin_octet = zero_pad_bin(bin_octet)

			# Build string of binary octets
			bin_octets.append(bin_octet)
		bin_addr = ".".join(bin_octets)

		return bin_addr

	else:
		return 'Error: iptools.validate_ip: parameter is not a valid IP address.'
