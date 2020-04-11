#!/usr/bin/env python3
# https://www.hackerrank.com/challenges/repeated-string/

s = "aba"
n = 10

# Complete the repeatedString function below.
def repeatedString(s, n):

	# First try took too many loops to complete large value inputs for "n" in Hacker Rank
	#results_set = []
	#loop = True
	# while loop:
	# 	for i in range(0, len(s)):
	# 		if len(results_set) < n:
	# 			results_set.append(s[i])
	# 			loop = True
	# 		else:
	# 			loop = False
	#return(results_set.count("a"))

	# Better way: solve with math as seen on HackerRank forum
    base_count = s.count("a")
    mult = n // len(s)
    leftover = s[:n % len(s)].count("a")
    return base_count * mult + leftover


print(repeatedString(s, n))

# One Liner from HackerRank forum:
# print(s.count("a") * (n // len(s)) + s[:n % len(s)].count("a"))
