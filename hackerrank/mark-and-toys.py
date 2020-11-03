#!/usr/bin/env python3
# https://www.hackerrank.com/challenges/mark-and-toys/

import math
import os
import random
import re
import sys

# Complete the maximumToys function below.
def maximumToys(prices, k):
	result = 0
	for price in sorted(prices):
		k -= price
		if k > 0:
			result += 1
	print(result)


k = 50
prices = [1, 12, 5, 111, 200, 1000, 10]
maximumToys(prices, k)