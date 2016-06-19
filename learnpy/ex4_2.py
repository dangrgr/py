#!/c/Python27/python
'''
II. Parse the below 'show version' data and obtain the following items (vendor, model, os_version, uptime, and serial_number).  Try to make your string parsing generic i.e. it would work for other Cisco IOS devices. 

The following are reasonable strings to look for:

'Cisco IOS Software' for vendor and os_version
'bytes of memory' for model
'Processor board ID' for serial_number
' uptime is ' for uptime

Store these variables (vendor, model, os_version, uptime, and serial_number) in a dictionary.  Print the dictionary to standard output when done.

Note, "Cisco IOS Software...Version 15.0(1)M4...(fc1)" is one line.
'''

show_version_output = '''
>>>>> show version data <<<<<
Switch>show version
Cisco Internetwork Operating System Software
IOS (tm) C2950 Software (C2950-I6Q4L2-M), Version 12.1(22)EA13, RELEASE SOFTWARE (fc2)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2009 by cisco Systems, Inc.
Compiled Fri 27-Feb-09 22:20 by amvarma
Image text-base: 0x80010000, data-base: 0x80570000
ROM: Bootstrap program is C2950 boot loader
Switch uptime is 0 minutes
System returned to ROM by power-on
System image file is "flash:c2950-i6q4l2-mz.121-22.EA13.bin"
cisco WS-C2950-12 (RC32300) processor (revision B0) with 20957K bytes of memory.
Processor board ID FAB0535Q22L
Last reset from system-reset
Running Standard Image
12 FastEthernet/IEEE 802.3 interface(s)
32K bytes of flash-simulated non-volatile configuration memory.
Base ethernet MAC Address: 00:06:D6:AB:A0:40
Motherboard assembly number: 73-5782-08
Motherboard serial number: FAB0535BC1K
Model revision number: B0
Model number: WS-C2950-12
System serial number: FAB0535Q22L
Configuration register is 0xF
>>>>> end <<<<<
'''
from pprint import pprint
rtr_facts = {}
output = show_version_output.split('\n')

for line in output:

	# Extract 'vendor' and 'os_version' if line contains 'Cisco IOS Software'
	if 'Software' in line:
		version_info = line.split(',')
		rtr_facts['vendor'] = 'Cisco'
		for item in version_info:
			if 'Version' in item:
				rtr_facts['os_version'] = item.strip()

	# Set 'model' if line contains 'bytes of memory'
	if 'bytes of memory' in line:
		rtr_facts['model'] = line.split()[1]

	# Set 'serial_number' if line contains 'Processor board ID'
	if 'Processor board ID' in line:
		rtr_facts['serial_number'] = line.split('Processor board ID ')[1]

	# Set 'uptime' if line contains ' uptime is '
	if ' uptime is ' in line:
		rtr_facts['uptime'] = line.split(' uptime is ')[1].strip()

print
pprint(rtr_facts.items())
print