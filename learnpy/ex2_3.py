#!/c/Python27/python

entry1 = "*  1.0.192.0/18   157.130.10.233        0 701 38040 9737 i"
entry2 = "*  1.1.1.0/24       157.130.10.233        0 701 1299 15169 i"
entry3 = "*  1.1.42.0/24     157.130.10.233        0 701 9505 17408 2.1465 i"
entry4 = "*  1.0.192.0/19   157.130.10.233        0 701 6762 6762 6762 6762 38040 9737 i"

list1 = entry1.split()
list2 = entry2.split()
list3 = entry3.split()
list4 = entry4.split()

path1 = list1[4:-1]
path2 = list2[4:-1]
path3 = list3[4:-1]
path4 = list4[4:-1]

ip1 = list1[1]
ip2 = list2[1]
ip3 = list3[1]
ip4 = list4[1]

print "%-20s %-20s" % ('ip_prefix','as_path')
print "%-20s %-20s" % (ip1,path1)
print "%-20s %-20s" % (ip2,path2)
print "%-20s %-20s" % (ip3,path3)
print "%-20s %-20s" % (ip4,path4)
