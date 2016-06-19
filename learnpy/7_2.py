#!/c/Python27/python
'''
2. In the following directory there is a file 'ospf_single_interface.txt':
Open this file and extract the interface, IP address, area, type, cost, hello timer, and dead timer.  Use regular expressions to accomplish your extraction.
Your output should look similar to the following:

Int:        GigabitEthernet0/1
IP:        172.16.13.150/29
Area:    30395
Type:    BROADCAST
Cost:    1
Hello:   10
Dead:   40
'''
import re
from pprint import pprint

def cdp_parser(pattern, ospf_data):
	for line in ospf_data:
		match = re.search(pattern, line)
		if match:
			return match.group(1)
	return 'no match!'

if __name__ == '__main__':
	f = open('OSPF_DATA/ospf_single_interface.txt')
	ospf_data = f.read()
	ospf_data = ospf_data.split('\n')
	f.close	

	temp_dict = {}
	temp_dict['Int'] = cdp_parser(r'^([\w/]+)', ospf_data)
	temp_dict['IP'] = cdp_parser(r'Internet Address (.+?),', ospf_data)
	temp_dict['Area'] = cdp_parser(r'Area (.+),', ospf_data)
	temp_dict['Type'] = cdp_parser(r'Network Type (\w+)', ospf_data)
	temp_dict['Cost'] = cdp_parser(r'Cost: (.+)', ospf_data)
	temp_dict['Hello'] = cdp_parser(r'Hello (.+?),', ospf_data)
	temp_dict['Dead'] = cdp_parser(r'Dead (.+?),', ospf_data)

	print
	for i in ('Int', 'IP', 'Area', 'Type', 'Cost', 'Hello', 'Dead'):
		print '%10s: %-20s' % (i, temp_dict[i])
	print