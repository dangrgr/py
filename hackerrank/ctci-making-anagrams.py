#!/usr/bin/env python3
# https://www.hackerrank.com/challenges/ctci-making-anagrams
import math
import os
import random
import re
import sys
import string

# Complete the makeAnagram function below.
def makeAnagram(a, b):
	solution = 0
	# Sort a and b
	a = sorted(a)
	b = sorted(b)
	# For each letter in the alphabet find and output intersections as solution
	for char in string.ascii_lowercase:
		a_count = a.count(char)
		b_count = b.count(char)
		# Throw out non-intersecting letters and count where deletion is required
		if a_count != b_count:
			solution += abs(a_count - b_count)

	print(solution)





makeAnagram('fcrxzwscanmligyxyvym', 'jxwtrhvujlmrpdoqbisbwhmgpmeoke')


''' Strat:
	sort a and b
	For each letter in the alphabet find and output intersections as solution
	Expected output: 30
'''