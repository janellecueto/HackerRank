#!/bin/python3

import os
import sys
import math

#
# Complete the getTotalX function below.
#
def getTotalX(a, b):
    #
    # Write your code here.
    #
    nums = set()
    for num in range(max(a), min(b)+1):
        isFine = True
        for x in a:
            if num % x != 0:
                isFine = False
                break
        if not isFine:
            continue
        isGood = True
        for y in b:
            if y % num != 0:
                isGood = False
                break
        if isGood:    
            nums.add(num)
    return len(nums)

#NOTE: there's a one-liner solution in Discussions tab

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    total = getTotalX(a, b)

    f.write(str(total) + '\n')

    f.close()
