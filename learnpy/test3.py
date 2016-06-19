#!/c/Python27/python

import fileinput 

for line in fileinput.input():
    line = line.strip() 
    print line.split(".")
