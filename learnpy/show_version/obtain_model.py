#!/c/Python27/python
'''
A. Create three functions in three separate modules and put them in a show_version directory (in practice you wouldn't do this--you would just have them all in one file, but this will let you experiment with packages).
  3. Function3 = obtain_model -- process the show version output and return the model (881) else return None.
'''
import re

f = open("show_version.txt")
show_version = f.read()
f.close

def obtain_model(show_version):
	for line in show_version.split('\n'):
		match = re.search(r'Cisco (.+?) .+processor.+with.+bytes of memory.', line)
		if match:
			try:
				return match.group(1)
			except:
				return None
	return None

if __name__ == '__main__':
	a = obtain_model(show_version)
	if a:
		print a
	else:
		print "No Match"