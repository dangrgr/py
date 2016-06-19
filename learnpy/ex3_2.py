#!/c/Python27/python
show_ip_bgp = '''
*  1.0.192.0/18   157.130.10.233        0 701 38040 9737 i
*  1.1.1.0/24       157.130.10.233        0 701 1299 15169 i
*  1.1.42.0/24     157.130.10.233        0 701 9505 17408 2.1465 i
*  1.0.192.0/19   157.130.10.233        0 701 6762 6762 6762 6762 38040 9737 i
'''
show_ip_bgp = show_ip_bgp.split('\n')[1:-1]
ip = []
path = []

print "%-20s %-20s" % ('ip_prefix','as_path')

for i,ip_bgp in enumerate(show_ip_bgp):
	ip.append(ip_bgp.split()[1])
	path.append(ip_bgp.split()[4:-1])
	print "%-20s %-20s" % (ip[i],path[i])