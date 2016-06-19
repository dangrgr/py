#!/c/Python27/python
'''
  a. Create a program that opens the 'r1_cdp.txt' file and using regular expressions extracts the remote hostname, remote IP address, model, vendor, and device_type.
  '''
import re
from pprint import pprint


#Generic cdp data parser
def cdp_parser(pattern, cdp_data):
	
	cdp_data = cdp_data.split('\n')

	for line in cdp_data:
		match = re.search(pattern, line)
		
		if match:
			return match.group(1)

	return ''


if __name__ == '__main__':
	f = open("r1_cdp.txt")
	cdp_data = f.read()
	f.close()

	remote_ip = cdp_parser(r'IP address: (.+)', cdp_data)
	remote_hostname = cdp_parser(r'Device ID: (.+)', cdp_data)
	model = cdp_parser(r'Platform: .+? (.+?), ', cdp_data)
	vendor = cdp_parser(r'Platform: (.+?) ', cdp_data)
	device_type = cdp_parser(r'Capabilities: (.+)', cdp_data)

	try:	
		print('\n')
		print 'remote_ip = %s' % remote_ip
		print 'remote_hostname = %s' % remote_hostname
		print 'model = %s' % model
		print 'vendor = %s' % vendor
		print 'device_type = %s' % device_type
		print('\n')
	except:
		print "\nNo Match!\n"

