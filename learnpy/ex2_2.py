#!/c/Python27/python

ip_addr = raw_input('Please enter an IP address in dotted decimal format: ')

first_octet_hex = bin(int(ip_addr.split('.')[0]))
second_octet_hex = bin(int(ip_addr.split('.')[1]))
third_octet_hex = bin(int(ip_addr.split('.')[2]))
fourth_octet_hex = bin(int(ip_addr.split('.')[3]))

print ''
print ''
print "%-20s %-20s %-20s %-20s" % ('first_octet','second_octet','third_octet','fourth_octet')
print "%-20s %-20s %-20s %-20s" % (first_octet_hex,second_octet_hex,third_octet_hex,fourth_octet_hex)
