#!/c/Python27/python
ip_net = raw_input("Please enter an IP network: ")
ip_net = ip_net.split('.')
ip_net = ip_net[0:3]
ip_net.append('0')

net_id = ".".join(ip_net)

first_octet_bin = bin(int(ip_net[0]))
second_octet_bin = bin(int(ip_net[0]))
third_octet_bin = bin(int(ip_net[0]))
fourth_octet_bin = bin(int(ip_net[0]))

first_octet_hex = hex(int(ip_net[0]))

print ''
print ''
print "%-20s %-20s %-20s" % ('NETWORK_NUMBER','FIRST_OCTET_BINARY','FIRST_OCTET_HEX')
print "%-20s %-20s %-20s" % (net_id,first_octet_bin,first_octet_hex) 
