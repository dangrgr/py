#!/c/Python27/python
'''
I. Create a Python class representing an IPAddress.  The class should have only one initialization variable--an IP address in dotted decimal formation.  You should be able to do the following with your class:

>>> test_ip = IPAddress('192.168.1.1')
>>> test_ip.ip_addr
'192.168.1.1'

    A. Write a method for this class that returns the IP address in dotted binary format (each octet should be eight binary digits in length).

>>> test_ip.display_in_binary()
'11000000.10101000.00000001.00000001'

    B. Write a method for this class that returns the IP address in dotted hex format (each octet should be two hex digits in length).

>>> test_ip.display_in_hex()
'c0.a8.01.01'

    C. Re-using the IP address validation code from class8, exercise1--create an is_valid() method that returns either True or False depending on whether the IP address is valid.

>>> test_ip.is_valid()
True
'''

class IPAddress(object):
	#init method
	def __init__(self, ip):
		self.ip = ip

	#Return IPAddress in dotted binary format
	def display_in_binary(self):
		octets = self.ip.split('.')
		bin_octets = []
		for octet in octets:
			try:
				bin_octet = bin(int(octet)).split('b')[1]
			except ValueError:
				print "Cannot convert non numerical octet to binary"
			while len(bin_octet) < 8:
				bin_octet = '0' + bin_octet
			bin_octets.append(bin_octet)
		bin_octets = '.'.join(bin_octets)
		return bin_octets

	#Return IPAddress in dotted hex format
	def display_in_hex(self):
		octets = self.ip.split('.')
		hex_octets = []
		for octet in octets:
			try:
				hex_octet = hex(int(octet)).split('x')[1]
			except ValueError:
				print "Connot convert non numberical octet to hex"
			hex_octets.append(hex_octet)
		hex_octets = '.'.join(hex_octets)
		return hex_octets

	#Validate IPAddress is a valid IP Address
	def is_valid(self):
		# Guilty until proven innocent
		ValidIP = False
		# Sanitize imput to ensure input is string
		if not type(self.ip) == str:
			return 'Error: input parameter must be a string.'
		# Extract octects from self.ip
		octets = self.ip.split('.')
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


##Test##
a = IPAddress('27.28.29.131')
print 'IP: %s' % a.ip
print 'Binary: %s' % a.display_in_binary()
print 'Hex: %s' % a.display_in_hex()
print 'Valid IP: %s' % a.is_valid()