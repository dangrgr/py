#!/usr/bin/env python3
# https://www.hackerrank.com/challenges/sherlock-and-anagrams

import math
import os
import random
import re
import sys

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):

	# Build dictonary of sorted, substrings in order to easily count total number of anagrams.
	list_subs = []
	end = 1
	for x in range(len(s)):
		for y in range(len(s)-x):
			y = y+end
			sub = s[x:y]
			list_subs.append(''.join(sorted(sub)))
		end +=1


	# brute force number of combinations??
	combos = 0
	for sub in list_subs:
		combos += list_subs.count(sub) - 1

	combos = int(combos/2)
	print(combos)


sherlockAndAnagrams('ifailuhkqq')
