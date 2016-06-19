#!/c/Python27/python
'''
2. Write a function that converts a list to a dictionary where the index of the list is used as the key to the new dictionary (the function should return the new dictionary).
'''
from pprint import pprint

my_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def func_list_to_dict(a_list=[]):
	if not type(a_list) == list:
		exit('Imput is not a list!')

	my_dict = {}

	for i,item in enumerate(a_list):
		my_dict[i] = item
	return my_dict

a = func_list_to_dict(my_list)
pprint(a)
