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

MINUTE_SECONDS = 60
HOUR_SECONDS = MINUTE_SECONDS * 60
DAY_SECONDS = HOUR_SECONDS * 24
WEEK_SECONDS = DAY_SECONDS * 7
YEAR_SECONDS = DAY_SECONDS * 365

for uptime in (uptime1, uptime2, uptime3, uptime4):

	uptime_fields = uptime.split(',')

	(rtr_name,time_field_1) = uptime_fields[0].split(' uptime is ')
	uptime_fields[0] = time_field_1

	int_seconds = 0

	for time_field in uptime_fields:
		for string_pattern, time_factor in (('year', YEAR_SECONDS), ('week', WEEK_SECONDS), 
											('day', DAY_SECONDS), ('hour', HOUR_SECONDS),
											('minute', MINUTE_SECONDS)):
			if string_pattern in time_field:
				(time, discard) = time_field.split()
				
				try:
					int_seconds += int(time) * time_factor
				except ValueError:
					"String cannot be converted into integer!"
				
	rtr_dict[rtr_name] = int_seconds

print(rtr_dict)


#Little Practice, with nested for loop and string search:
for name, sometime in (rtr_dict.items()):
	for str_pattern, int_time in (('rtr', 0), ('1', 1)):
		if str_pattern in name:
			print name