#!/c/Python27/python
'''
5. Write a program that prompts a user for an IP address, then checks if the IP address is valid, and then converts the IP address to binary (dotted decimal format). Re-use the functions created in exercises 3 and 4 ('import' the functions into your new program).'''

import iptools

ip_address = raw_input('Please enter an IPv4 address to be converted to decimal:')

a = '\n' + iptools.dec_to_bin(ip_address) + '\n'
print a
