#!/c/Python27/python
import sys
args = sys.argv
usage = 'Usage: ' + args[0].split('\\')[-1] + ' <ip address>'


if len(args) == 2:
	ip_addr = args[1]
else:
	print usage
	print '\nError: Please enter an IP address...'
	quit()


ip_octets = ip_addr.split('.')


if len(ip_octets) == 4:

	bin_octets = []

	for i,ip_octet in enumerate (ip_octets):
		bin_octet = (bin(int(ip_octet))).split('b').pop()
		while len(bin_octet) < 8:
			bin_octet = '0' + bin_octet
		bin_octets.append(bin_octet)

	bin_addr = ".".join(bin_octets)

	print '\n%-15s %s' % ('IP address','Binary')
	print '%-15s %s' % (ip_addr,bin_addr)

else:
	print usage
	print '\nError: Invalid IP address entered. Please try again...'