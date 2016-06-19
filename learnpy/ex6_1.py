#!/c/Python27/python
'''
1. Create a function that returns the multiplication product of three parameters--x, y, and z. z should have a default value of 1.
    a. Call the function with all positional arguments.
    b. Call the function with all named arguments.
    c. Call the function with a mix of positional and named arguments.
    d. Call the function with only two arguments and use the default value for z.
 '''


def func_product(x, y, z=1):
	return x*y*z

# a. Call the function with all positional arguments.
a = func_product(20, 30, 1)

# b. Call the function with all named arguments.
b = func_product(x=6, y=10, z=10)

# c. Call the function with a mix of positional and named arguments.
c = func_product(30, y=20)

# d. Call the function with only two arguments and use the default value for 
d = func_product(20, 30)

print a
print b
print c
print d



