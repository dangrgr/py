#!/usr/bin/env python
''' Fun with input'''

'''
# Basic input (Python 3)
a = input("What should we set the value of a to?")
print(f'You set the value of a to {a}')
'''

'''
# Input validation
while True:
    print('Enter your age:')
    age = input()
    try:
        age = int(age)
    except:
        print('Please use a numeric value to describe your age')
        continue

    if age <1:
        print('Please enter a positve number')
        continue
    break

print(f'Your age is {age}.')
'''
