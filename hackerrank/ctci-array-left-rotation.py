#!/usr/bin/env python
# https://www.hackerrank.com/challenges/ctci-array-left-rotation

a = [1, 2, 3, 4, 5]
d = 4

# Complete the rotLeft function below.
def rotLeft(a, d):
    for i in range(d):
        popped = a.pop(0)
        a.append(popped)
    return a

print(rotLeft(a, d))
