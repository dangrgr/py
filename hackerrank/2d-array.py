#!/usr/bin/env python3
# https://www.hackerrank.com/challenges/2d-array/problem

input ="""
1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0
"""


# Complete the hourglassSum function below.
def hourglassSum(arr):
	# initiate hourglass_sums (list)
	hourglass_sums = []

	# extract hourglass values, collect hourglass sums
	col = 0
	row = 0
	while row < 4:
		col = 0
		while col < 4:
			hourglass_value = (arr[row][col:col+3]+[arr[row+1][col+1]]+arr[row+2][col:col+3])
			hourglass_sum = sum(x for x in hourglass_value)
			hourglass_sums.append(hourglass_sum)
			col += 1
		row +=1

	# return hourglass_sums max value
	return max(hourglass_sums)


# Not part of solution...
# Massage input so it matches Hacker rank list format:
input = input.strip().split("\n")
for i in range(len(input)):
	input[i] = [int(x) for x in input[i].split()]

# call solution function
print(hourglassSum(input))
