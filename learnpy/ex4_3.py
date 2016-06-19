#!/c/Python27/python
'''
III. Create a program that converts the following uptime strings to a time in seconds.
For each of these strings store the uptime in a dictionary using the device name as the key.
During this conversion process, you will have to convert strings to integers.  
For these string to integer conversions use try/except to catch any string to integer conversion exceptions.
For example:
int('5') works fine
int('5 years') generates a ValueError exception.
Print the dictionary to standard output.
'''

uptime1 = 'twb-sf-881 uptime is 6 weeks, 4 days, 2 hours, 25 minutes'
uptime2 = '3750RJ uptime is 1 hour, 29 minutes'
uptime3 = 'CATS3560 uptime is 8 weeks, 4 days, 18 hours, 16 minutes'
uptime4 = 'rtr1 uptime is 5 years, 18 weeks, 8 hours, 23 minutes'

rtr_dict = {}

for string in (uptime1, uptime2, uptime3, uptime4):
	string = string.split(' uptime is ')
	rtr_name = string[0]
	rtr_uptime = string[1].split(',')
	int_seconds = 0

	for elements in rtr_uptime:
		elements = elements.strip().split()
		counter = elements[1]
		time = elements[0]

		try:
			int_time = int(time)
		except ValueError, e:
			print "Failed to convert string to integer!"

		if counter == 'years':
			int_seconds += int_time*31536000
		elif counter == 'weeks':
			int_seconds += int_time*604800
		elif counter == 'days':
			int_seconds += int_time*86400
		elif counter == 'hours':
			int_seconds += int_time*3600
		elif counter == 'minutes':
			int_seconds += int_time*60
	
	rtr_dict[rtr_name] = int_seconds

print(rtr_dict)