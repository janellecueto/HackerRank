#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the closestNumbers function below.
def closestNumbers(arr):
    arr.sort()
    mindiff = 10**7 * 2
    mins = []
    for i in range(len(arr)-1):
        if arr[i+1] - arr[i] < mindiff:
            mindiff = arr[i+1] - arr[i]
            mins.clear()
            mins.append(arr[i])
            mins.append(arr[i+1])
        elif arr[i+1] - arr[i] == mindiff:
            mins.append(arr[i]) 
            mins.append(arr[i+1])
    return mins


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
