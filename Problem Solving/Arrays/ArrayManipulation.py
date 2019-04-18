#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    pass

if __name__ == '__main__':
    n,m = map(int, input().split())
    arr = [0] * (n+1)
    for _ in range(m):
        a,b,k = map(int, input().split())
        arr[a-1] += k
        if b <= (n+1):
            arr[b] -= k         # NOTE: This solution is from the Discussions tab
    mx = 0
    x = 0
    # print(arr)
    for a in arr:
        x += a
        if(mx < x):
            mx = x
    print(mx)
