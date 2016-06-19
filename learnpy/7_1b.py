#!/c/Python27/python
'''
b. Create a program that opens the 'sw1_cdp.txt' file and finds all of the remote hostnames, remote IP addresses, and remote platforms.  Your output should look similar to the following:
   remote_hosts: ['R1', 'R2', 'R3', 'R4', 'R5']
   IPs: ['10.1.1.1', '10.1.1.2', '10.1.1.3', '10.1.1.4', '10.1.1.5']
   platform: ['Cisco 881', 'Cisco 881', 'Cisco 881', 'Cisco 881', 'Cisco 881']
'''
import re

#  Modified generic cdp_parser (Old way)
def cdp_parser(pattern, cdp_data):
	cdp_data = cdp_data.split('\n')
	output = []
	for line in cdp_data:
		match = re.search(pattern, line)
		if match:
			output.append(match.group(1))	
	return output


f = open("CDP_DATA/sw1_cdp.txt")
cdp_data = f.read()
f.close()

# Old way
remote_hosts1 = cdp_parser(r'Device ID: (.+)', cdp_data)
IPs1 = cdp_parser(r'IP address: (.+)', cdp_data)
platform1 = cdp_parser(r'Platform: (.+),', cdp_data)

# New way
temp_dict = {}
temp_dict['remote_hosts'] = re.findall(r'Device ID: (.+)', cdp_data)
temp_dict['IPs'] = re.findall(r'IP address: (.+)', cdp_data)
temp_dict['platform'] = re.findall(r'Platform: (.+),', cdp_data)

# Print output
print
output = ('remote_hosts', 'IPs', 'platform')
for i in output:
	print '%15s: %-20s' % (i,temp_dict[i])
print