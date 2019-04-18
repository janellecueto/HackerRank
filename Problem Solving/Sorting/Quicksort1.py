#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the quickSort function below.
def quickSort(arr):
    p = arr[0]
    left, right, equal = [],[],[]
    equal.append(p)
    for a in arr[1:]:
        if a == p:
            equal.append(a)
        elif a < p:
            left.append(a)
        else:
            right.append(a)
    return left + equal + right

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = quickSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
