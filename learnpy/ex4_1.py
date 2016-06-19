#!/c/Python27/python
'''
I. Prompt a user to input an IP address.
Re-using some of the code from class3, exercise4--determine if the IP address is valid.
Continue prompting the user to re-input an IP address until a valid IP address is input.
For output, print the IP and whether it is valid or not.
'''
import sys
ValidIP = False

#Loop until a valid IP address is entered
while ValidIP == False:

	#Request IP address (input)
	ip_addr = raw_input('\nPlease enter an IP address:')
	octets = ip_addr.split('.')

	#Validate IP address is valid
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

	#Print result; Exit loop if Ip address is valid
	if ValidIP == True:
		print '\nGood! You entered: %s\n' % ip_addr
	else:
		print('\nError: Invalid IP Address: %s\n' % ip_addr)

