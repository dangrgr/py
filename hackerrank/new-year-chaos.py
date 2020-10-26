#!/bin/python3
import string
import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    bribes = 0
    for i, value in enumerate(q):
        # Firt check if current position number and value difference is greater than 2 (too chaotic); and return None of seen.
        if value > i+3:
            print("Too chaotic")
            return None
        # for each index position: count difference of position closer to 0 from next position. Each difference in position greater than 1 is a bribe.
        for j in range(max(value-2,0), i):
            if q[j] > value:
                bribes += 1
    print(bribes)

if __name__ == '__main__':
# test cases from sample input in alpha sequence
    test_cases = [
        [2, 1, 5, 3, 4],            # expect: 3
        [2, 5, 1, 3, 4],            # expect: Too chaotic
        [5, 1, 2, 3, 7, 8, 6, 4],   # expect: Too chaotic
        [1, 2, 5, 3, 7, 8, 6, 4],   # expect: 7
        [1, 2, 5, 3, 4, 7, 8, 6]    # expect: 4
    ]
    for test_case in test_cases:
        minimumBribes(test_case)
