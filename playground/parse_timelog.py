import re
from datetime import datetime
from pprint import pprint


## TODO first excercise: https://code-maven.com/slides/perl/exercise-parse-log-file
"""
09:20-11:00 Introduction
11:00-11:15 Exercises
11:15-11:35 Break
11:35-12:30 Numbers and strings
12:30-13:30 Lunch Break
13:30-14:10 Exercises
14:10-14:30 Solutions
14:30-14:40 Break
14:40-15:40 Lists
15:40-17:00 Exercises
17:00-17:30 Solutions

09:30-10:30 Lists and Tuples
10:30-10:50 Break
10:50-12:00 Exercises
12:00-12:30 Solutions
12:30-12:45 Dictionaries
12:45-14:15 Lunch Break
14:15-16:00 Exercises
16:00-16:15 Solutions
16:15-16:30 Break
16:30-17:00 Functions
17:00-17:30 Exercises
"""

# Read fine to lines
with open("timelog.txt", 'r') as file:
	data = file.read()
lines = data.split("\n")

# Create ordered list of key-value pairs: activity, start time, finish time, duration
timelog = {}
for index,line in enumerate(lines):
	# parse start_time and activuty
	if line != '':
		timestamp = re.findall('[0-9][0-9]\:[0-9][0-9]', line)[0]
		activity = re.split('[0-9][0-9]\:[0-9][0-9]', line)[1].strip()
		timelog[index] = dict([('start_time',timestamp),('activity',activity)])
		# get end_time and duration
		if index > 0 and timelog[index-1]['start_time'] != None:
			last_start_time = datetime.strptime(timelog[index-1]['start_time'],"%H:%M")
			this_start_time = datetime.strptime(timelog[index]['start_time'],"%H:%M")
			difference = this_start_time - last_start_time
			min_in_day = 24 * 60
			timelog[index-1]['duration'] = divmod(difference.days * min_in_day + difference.seconds, 60)[0]
			timelog[index-1]['end_time'] = timestamp


	else:
		timelog[index] = dict([('start_time',None),('end_time',None),('activity',None),('duration',None)])

for index,entry in timelog.items():
	if 'end_time' in entry.keys():
		if entry['activity']:
			print(f"{entry['start_time']}-{entry['end_time']} {entry['activity']}")
		else:
			print("")

print('\n')


## TODO next excercise. Provide the following output after the abovce newline
"""
Break                      65 minutes    6%
Dictionaries               15 minutes    1%
Exercises                 340 minutes   35%
Functions                  30 minutes    3%
Introduction              100 minutes   10%
Lists                      60 minutes    6%
Lists and Tuples           60 minutes    6%
Lunch Break               150 minutes   15%
Numbers and strings        55 minutes    5%
Solutions                  95 minutes    9%
"""

# Summarize Timelog in a summary dict
timelog_summary = {}
for entry in timelog.values():
	if 'duration' in entry.keys() and entry['duration']:
		activity = entry['activity']
		duration = entry['duration']
		if activity in timelog_summary.keys():
			timelog_summary[activity] += duration
		else:
			timelog_summary[activity] = duration

# Calculate percentage from total time for each activity and display results
sum_duration = sum(timelog_summary.values())
keylist = list(timelog_summary.keys())
keylist.sort()
for activity in keylist:
	duration = timelog_summary[activity]
	percent = str(round((duration/sum_duration)*100)) + '%'
	duration = str(duration) + ' minutes'
	print(f'{activity:<30}{duration:<15}{percent}')
