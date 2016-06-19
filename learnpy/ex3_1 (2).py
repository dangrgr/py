#!/c/Python27/python
import sys
args = sys.argv

if len(args) == 2:
	ip_addr = sys.argv.pop()
else:
	print 'Usage: ' + sys.argv[0].split('\\')[-1] + ' <ip address>'
	quit()

octets = ip_addr.split('.')
bin_octets = []

for i,octet in enumerate(octets):
	bin_octet = bin(int(octet)).split('b')[1]
	while len(bin_octet) < 8:
		bin_octet = '0' + bin_octet
	bin_octets.append(bin_octet)

print '\n%-15s %s' % ('Ip Address', 'Binary')
print '%-15s %s\n' % (ip_addr, '.'.join(bin_octet))