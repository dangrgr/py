#!/c/Python27/python
'''
  7a. Create a program that opens the 'r1_cdp.txt' file and using regular expressions extracts the remote hostname, remote IP address, model, vendor, and device_type.
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
	f = open("CDP_DATA/r1_cdp.txt")
	cdp_data = f.read()
	f.close()

	network_devices = {}

	remote_ip = cdp_parser(r'IP address: (.+)', cdp_data)
	remote_hostname = cdp_parser(r'Device ID: (.+)', cdp_data)
	model = cdp_parser(r'Platform: .+? (.+?), ', cdp_data)
	vendor = cdp_parser(r'Platform: (.+?) ', cdp_data)
	device_type = cdp_parser(r'Capabilities: (.+?) ', cdp_data)

	
	network_devices['remote_ip'] = remote_ip
	network_devices['remote_hostname'] = remote_hostname
	network_devices['model'] = model
	network_devices['vendor'] = vendor
	network_devices['device_type'] = device_type

	print
	pprint(network_devices)
	print

