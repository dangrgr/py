#!/c/Python27/python

ipv6_address = 'FE80:0000:0000:0000:0101:A3EF:EE1E:1719'
print 'ipv6_address is:'
print ipv6_address

print 'splitting octetcs...'
 
octets = ipv6_address.split(':')
print 'the value of octects is:'
print octets

print 'joining octects again...'

joined_octets = ':'.join(octets)
print 'the value of joined_octets is:'
print joined_octets
