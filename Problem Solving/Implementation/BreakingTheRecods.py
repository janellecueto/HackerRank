#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    countmin, countmax = 0,0
    smin = scores[0]
    smax = scores[0]
    for s in scores:
        if s < smin:
            smin = s
            countmin += 1
        elif s > smax:
            smax = s
            countmax += 1
    return [countmax, countmin]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))
 
    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
