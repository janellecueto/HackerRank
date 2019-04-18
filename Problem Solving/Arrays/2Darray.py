#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    hourglasses = []
    farr = [item for sublist in arr for item in sublist] #flatten array
    for i in range(22):
        if (i-1)%3 == 0 and (i-1)%6 >0:
            continue
        if (i-2)%3 == 0 and (i-2)%6 > 0:
            continue
        hourglasses.append([farr[x] for x in [i, i+1, i+2,i+7, i+12,i+13,i+14]])
    print(hourglasses)
    return sum(max(hourglasses, key=sum))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()