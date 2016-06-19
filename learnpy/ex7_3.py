#!/c/Python27/python
'''
3.  In the following directory there is a file 'ospf_data.txt':

https://github.com/ktbyers/pynet/tree/master/learnpy_ecourse/class7/OSPF_DATA

This file contains the output from 'show ip ospf interface'.  Using functions and regular expressions parse this output to display the following (note, I ended up using re.split() as part of the solution to this problem):

Int:     Loopback0
IP:     10.90.3.38/32
Area: 30395
Type: LOOPBACK
Cost: 1

Int:     GigabitEthernet0/1
IP:      172.16.13.150/29
Area:  30395
Type:  BROADCAST
Cost:  1
Hello: 10
Dead: 40

Int:      GigabitEthernet0/0.2561
IP:      10.22.0.117/30
Area:  30395
Type:  POINT_TO_POINT
Cost:  1
Hello: 10
Dead: 40
'''
import re

# Function to parse ospf data for pattern matches. Returns data if mach.
def parse_ospf_data(pattern, ospf_data):
	ospf_data = ospf_data.split('\n')
	for line in ospf_data:
		match = re.search(pattern, line)
		if match:
			return match.group(1)
	return None

def print_out(a_dict):
	for i in ('Int','IP','Area','Type','Cost','Hello','Dead',):
		if a_dict[i]:
			print '%15s:   %-20s' % (i, a_dict[i])
	print

if __name__ == '__main__':
	
	# Open file and read in data
	f = open('OSPF_DATA/ospf_data.txt')
	ospf_data = f.read()
	f.close()

	# Split osfp_data using re.split with a look ahead expression
	ospf_data_split = re.split(r'\n(?=Loopback0|GigabitEthernet)', ospf_data)

	# Define patterns for parsing ospf data
	patterns = [
		('Int', r'(Loopback[0-9]|GigabitEthernet[0-9]+/[0-9\.]+)'),
		('IP', r'Internet Address ([\w\./]+),'),
		('Area', r'Area (.+),'),
		('Type', r'Network Type (.+?),'),
		('Cost', r'Cost: (\w+)'),
		('Hello', r'Hello (\w+)'),
		('Dead', r'Dead (\w+)')
	]

	# Initialize a dictionary for each interface
	for line in ospf_data_split:
		int_dict = {}	
		
		# Add data for each interface to dictionary
		for (name,pattern) in patterns:
			int_dict[name] = parse_ospf_data(pattern, line)

		# print output for each interface
		print_out(int_dict)

		