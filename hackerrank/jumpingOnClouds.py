#!/usr/bin/env python3
# From: https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

c = "0 0 0 1 0 0"

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):

# First try
    # clouds = list(map(int, c.split()))
    # remains = len(clouds)-1
    # hops = 0
    # while remains > 0:
    #     cloud = clouds[-remains]
    #     next_cloud = clouds[-(remains)]
    #     next_next = clouds[-(remains)+1]
    #     print(remains, next_cloud, next_next)
    #     if remains > 1 and next_cloud == 1 or next_next == 0:
    #         print("skip")
    #         hops += 1
    #         remains -= 2
    #     else:
    #         print("no skip")
    #         remains -= 1
    #         hops += 1

# Better way
    c = list(map(int, c.split()))
    n = len(c)
    hops = 0
    i = 0
    while i < n - 1:
        if i + 2 >=n or c[i + 2] == 1:   #not possible to jump 2 clouds
            #print("no skip")
            i += 1
            hops += 1
        else:
            #print("skip")
            i += 2
            hops += 1

    return hops


print(jumpingOnClouds(c))
