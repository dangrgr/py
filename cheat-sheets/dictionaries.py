#!/usr/bin/env python3

# dictionaries
# example
student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}

# get key using brackets:
print(student['name'])

# set key using brackets:
student['phone'] = '555-5555'
student['name'] = 'jane'
print(student)

# get method
# returns 'None' by default if key does not exist
# can specify optional default if key is not found as second param
print(student.get('age', 'Not Found'))

# update method
# Updates all keys in target dict with those defined in the update. Can add new keys if desired.
student.update({'name': 'Jane', 'age': 26, 'phone': '555-5555', 'hobbies': ['Hacking', 'Cooking', 'Kiddos']})
print(student)

# delete a key with del
del student['age']
print(student)
## putting age back
student.update({'age': 26})

# pop method: removes a key and returns its value.
age = student.pop('age')
print(age)
print(student)
## putting age back, again...
student.update({'age': 26})

# return number of keys in dict
print(len(student))

# keys method, return key names in dict
print(student.keys())

# values method, return values in dict
print(student.values())

# items method, returns pairs of keys and values as list of tuples; can be itterated with 'for k, v in student.items():'
print(student.items())


# Dictionary Comprehension Example
a_dict = {'name': 'John', 'age': '27', 'sex': 'Male'}

# convert dictionarty to list
def dict_to_list(dict):
	return ([(k,v) for k,v in dict.items()])

# convert list to dictionary
def list_to_dict(list):
	return {i:j for i,j in list}

a_list = dict_to_list(a_dict)
print(list_to_dict(a_list))


# Example of looping through dictionary in a for loop

# only returns the keys
for i in a_dict:
    print(i)

# returns key and value pairs
for k,v in a_dict.items():
    print(k + ':',v)