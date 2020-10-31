#!/usr/bin/env python
# https://www.hackerrank.com/challenges/alternating-characters/


# Complete the alternatingCharacters function below.
def alternatingCharacters(s):
	prev_char = "Z"
	del_count = 0
	for char in s:
		if char == prev_char:
			del_count += 1
		prev_char = char

	print(del_count)



alternatingCharacters('BBBBB')
#expected output = 4
