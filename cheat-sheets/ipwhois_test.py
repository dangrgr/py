#!/usr/bin/env python3
from ipwhois import IPWhois
from pprint import pprint
import csv

# ipwhos: https://pypi.org/project/ipwhois/
# example: https://github.com/secynic/ipwhois/tree/master/ipwhois/examples/redis_cache

#ips.csv
'''
ip,count
1.1.1.1,23
4.2.2.2,450
8.8.8.8,74
'''

with open('ips.csv', 'r') as csvfile:
	dict_reader = csv.DictReader(csvfile)
	print('IP, ASN, CIDR, Description\n--- ---- ----- -----------')
	for row in dict_reader:
		ip = (row['ip'])
		ip_obj = IPWhois(ip)
		results = ip_obj.lookup_rdap()
		print(f"{ip}, {results['asn']}, {results['asn_cidr']}, {results['asn_description']}")



