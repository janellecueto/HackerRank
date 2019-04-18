#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the diagonalDifference function below.
def diagonalDifference(arr):
    l1 = []
    l2 = []
    i, j = 0, -1
    for a in arr:
        l1.append(a[i])
        l2.append(a[j])
        i += 1
        j -= 1
    return abs(sum(l1)-sum(l2))
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
