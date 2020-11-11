#!/usr/bin/env python
# https://www.hackerrank.com/challenges/ctci-bubble-sort/

import math
import os
import random
import re
import sys

# Complete the countSwaps function below.
def countSwaps(a):
    n = len(a)
    swaps = 0
    for i in range(n-1):
        for j in range(0, n-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                swaps += 1
    print(f'Array is sorted in {swaps} swaps.')
    print(f'First Element: {a[0]}')
    print(f'Last Element: {a[-1]}')


# Unit Tests
if __name__ == "__main__":

    # Test 1
    a = [1,2,3]
    countSwaps(a)

    '''Output should be as follows:
    Array is sorted in 0 swaps.
    First Element: 1
    Last Element: 3
    '''

    # Test 2
    a = [3,2,1]
    countSwaps(a)

    '''Output should be as follows:
    Array is sorted in 3 swaps.
    First Element: 1
    Last Element: 3
    '''

    # Test 3
    a = [4,2,3,1]
    countSwaps(a)

    '''Output should be as follows:
    Array is sorted in 5 swaps.
    First Element: 1
    Last Element: 4
    '''